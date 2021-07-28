import traceback
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Case, Value, When, Sum, IntegerField, Count
from django.template.response import TemplateResponse
from . import forms
from . import models
from itertools import chain
import json
from django.core import serializers
# Create your views here.

from django.http import HttpResponse
from django.db import IntegrityError

def get_active_company(request):
    return request.session.get('active_company_id', 1)

def get_active_company_name(request):
    return request.session.get('active_company_name', "")

def set_active_company(request, company_id=1):
    request.session['active_company_id'] = company_id
    try:
        request.session['active_company_name'] = models.Company.objects.get(id=company_id).name
    except models.Company.DoesNotExist:
        pass

def reset_connection():
    from django.db import connection
    connection.close()

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                set_active_company(request)
                return HttpResponseRedirect('/karigars_all/')
    return render(request,'loginapp.html')

def redirect_root(request):
    return HttpResponseRedirect('/homepage/')

def homepage(request):
    return render(request, '../templates/homepage.html')

def new_karigar(request):
    form = forms.KarigarForm()
    if request.method == 'POST':
        form = forms.KarigarForm(request.POST, request.FILES)
        if form.is_valid():
            karigar = form.save()
            messages.success(request, "New Karigar added.")
            return HttpResponseRedirect('../../karigars_all/')
    return render(request, '../templates/newkarigar_form.html', {'form':form})

def edit_karigar(request, pk):
    karigar = get_object_or_404(models.Karigar,pk=pk)
    form = forms.KarigarForm(instance=karigar)
    if request.method == 'POST':
        form = forms.KarigarForm(request.POST, request.FILES, instance=karigar)
        if form.is_valid():
            karigaredit = form.save()
            messages.success(request,"Karigar information updated.")
            return HttpResponseRedirect('../../karigars_all/')
    return render(request, '../templates/newkarigar_form.html', {'form': form})

def delete_karigar(request, pk):
    karigar_name = models.Karigar.objects.get(pk=pk).name
    models.Assignment.objects.filter(karigar=pk).delete()
    models.Karigar.objects.filter(pk=pk).delete()

    messages.success(request,"All records of "+karigar_name+" deleted!")
    return HttpResponseRedirect('../../karigars_all/')


def new_product(request):
    product_form = forms.ProductForm(initial = {'company': get_active_company(request)})
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.fabric = product.fabric.lower()
            product.colour = product.colour.lower()
            product.save()
            messages.success(request, "New product added.")
            return HttpResponseRedirect('../../products_all/')
    return render(request, '../templates/newproduct_form.html', {'form':product_form})

def edit_product(request, id_pk):
    product = get_object_or_404(models.Product,pk=id_pk)
    form = forms.ProductForm(instance=product)
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request,"Product information updated.")
            return HttpResponseRedirect('../../products_all/')
    return render(request, '../templates/newproduct_form.html', {'form':form})


def edit_assignment(request, id_pk):
    assignment = get_object_or_404(models.Assignment, pk=id_pk)
    form = forms.EditAssignmentForm(instance=assignment)
    form.fields['product'].queryset = models.Product.objects.filter(company=get_active_company(request))
    errors=[]
    if request.method == 'POST':
        form = forms.EditAssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            assignment = form.save()
            messages.success(request,'Transaction edited successfully!')
            return HttpResponseRedirect('../../overview_challans/')
        else:
            errors.append("Please check values again!")
            return render(request, '../templates/edit_assignment_form.html', {'form': form, 'errors': errors})

    return render(request, '../templates/edit_assignment_form.html', {'form': form})


def delete_product(request, id_pk):
    product = get_object_or_404(models.Product, pk=id_pk)
    product_name = product.prodid
    models.Assignment.objects.filter(product=product).delete()
    models.Product.objects.filter(pk=id_pk).delete()
    messages.success(request,"All records of "+product_name+" deleted!")
    return HttpResponseRedirect('../../products_all/')


def assign_product(request,name_pk):
    karigar = get_object_or_404(models.Karigar,pk=name_pk)
    formset = forms.AssignFormSet(queryset=models.Assignment.objects.none())
    errors = []
    challan_id = ""
    date_of_assignment = datetime.now().strftime("%Y-%m-%d")
    for form in formset:
        form.fields['product'].queryset = models.Product.objects.filter(company=get_active_company(request))


    if request.method == 'POST':

        formset = forms.AssignFormSet(request.POST,
                                      queryset=models.Assignment.objects.none())
        if formset.has_changed(): #atleast one form entry found, validate Challan, Date and Process field
            if not request.POST['challan_id']:
                errors.append("Challan ID is required!")
            challan_id = request.POST['challan_id']
            if not request.POST['date_assignment']:
                errors.append("Assignment date is required!")
            date_of_assignment = request.POST['date_assignment']
            if request.POST.get('ck',None) == None:
                errors.append("Process selection [Issue / Receive / Reissue] is required!")

        if formset.is_valid() and errors == []: #check validity of product and qty field
            try:
                assignments = formset.save(commit=False)
                count_form=0
                product_size_obj=[]
                product_names=[]
                for assignment in assignments: #check for duplicate product names in formset
                    if {assignment.product,assignment.size} in product_size_obj:
                        errors.append('DUPLICATE ENTRY for '+str(assignment.product)+' '+assignment.size+' not allowed!')
                        return render(request, '../templates/assignment_form.html', {
                            'formset': formset,
                            'karigar': karigar,
                            'errors': errors,
                            'challan_id': challan_id,
                            'date_of_assignment': date_of_assignment,

                        })
                    product_names.append(assignment.product)

                for assignment in assignments:
                    count_form = count_form+1
                    assignment.challanid = request.POST['challan_id']
                    assignment.assignmentdate = request.POST['date_assignment']
                    assignment.process = request.POST['ck']
                    assignment.karigar = karigar
                    assignment.save()
                if count_form == 1:
                    trans = 'transaction'
                else:
                    trans = 'transactions'
                messages.success(request, str(count_form)+" "+trans+" added.")
                if request.POST.get('save'):
                    return HttpResponseRedirect('../../karigars_all/')
                elif request.POST.get('save_overview'):
                    return HttpResponseRedirect('../../overview_karigars/')
            except IntegrityError as e:
                return render(request, '../templates/assignment_form.html', {
                    'formset': formset,
                    'karigar': karigar,
                    'errors': e.__cause__,
                    'challan_id': challan_id,
                    'date_of_assignment': date_of_assignment,

                })

    return render(request, '../templates/assignment_form.html', {
        'formset': formset,
        'karigar': karigar,
        'errors': errors,
        'challan_id': challan_id,
        'date_of_assignment': date_of_assignment,
    })


def karigars_all(request):

    try:
        karigars = models.Karigar.objects.all().order_by('name')
        return render(request, '../templates/karigar_list.html', {'karigars': karigars})
    except Exception as e:
        print(f"Error in listing karigars: {e} \nTraceback: {traceback.format_exc()}")
        return render(request, '../templates/server_error.html')

def products_all(request):
    try:
        products = models.Product.objects.filter(company=get_active_company(request))
        return render(request, '../templates/product_list_new.html', {'products': products})
    except Exception as e:
        print(f"Error in listing all products: {e} \nTraceback: {traceback.format_exc()}")
        return render(request, '../templates/server_error.html')



def overview_karigars(request):

    try:
        klist = models.Karigar.objects.all()
        return render(request, 'overview_karigar.html',{'klist': klist})
    except:
        return render(request, 'server_error.html')




def getTableKarigar(request):
    pk = request.GET['karigar_id']
    karigar = get_object_or_404(models.Karigar, pk=pk)
    resultset = models.Assignment.objects.filter(karigar=karigar).values('product', 'product__prodid', 'size').annotate(
        total_issued=Sum(
            Case(When(process='issue', then='qty'), default=Value(0), output_field=IntegerField())),
        sum_received=Sum(
            Case(When(process='receive', then='qty'), default=Value(0), output_field=IntegerField())),
        sum_reissued=Sum(
            Case(When(process='reissue', then='qty'), default=Value(0), output_field=IntegerField())),

    )

    for result in resultset:
        result['total_received'] = result['sum_received'] - result['sum_reissued']
        result['pending'] = result['total_issued'] - result['total_received']
        q1 = karigar.assignment_set.filter(product=result['product']).filter(process='issue').filter(size=result['size'])
        if not q1:
            result['issue_transactions'] = 'No transactions'
        else:
            result['issue_transactions']= serializers.serialize('json',q1, fields=('challanid','assignmentdate','qty'))
            #result['issue_transactions'] =q1
        q2 = karigar.assignment_set.filter(product=result['product']).filter(process='receive').filter(size=result['size'])
        if not q2:
            result['receive_transactions']= 'No transactions'
        else:
            result['receive_transactions'] = serializers.serialize('json',q2, fields=('challanid','assignmentdate','qty'))
            #result['receive_transactions'] =q2
        q3 = karigar.assignment_set.filter(product=result['product']).filter(process='reissue').filter(size=result['size'])
        if not q3:
            result['reissue_transactions']= 'No transactions'
        else:
            result['reissue_transactions'] =serializers.serialize('json',q3, fields=('challanid','assignmentdate','qty'))
            #result['reissue_transactions'] =q3
    data = json.dumps(list(resultset))
    #data = serializers.serialize("json", list(resultset), fields=('product','total_issued','sum_received','sum_reissued'))
    return HttpResponse(data, content_type='application/json')


def overview_products(request):

    try:
        plist = models.Product.objects.filter(company=get_active_company(request))
        return render(request, 'overview_product.html', {'plist': plist})
    except:
        return render(request, 'server_error.html')


def getTableProduct(request):

    pk = request.GET['product_id']
    product = get_object_or_404(models.Product, pk=pk)
    resultset = models.Assignment.objects.filter(product=product).values('karigar', 'karigar__name').annotate(
        total_issued=Sum(
            Case(When(process='issue', then='qty'), default=Value(0), output_field=IntegerField())),
        sum_received=Sum(
            Case(When(process='receive', then='qty'), default=Value(0), output_field=IntegerField())),
        sum_reissued=Sum(
            Case(When(process='reissue', then='qty'), default=Value(0), output_field=IntegerField())),

    )
    #print resultset
    for result in resultset:
        result['total_received'] = result['sum_received'] - result['sum_reissued']
        result['pending'] = result['total_issued'] - result['total_received']
        result['profile'] = get_object_or_404(models.Karigar,pk=result['karigar']).profile
        q1 = product.assignment_set.filter(karigar=result['karigar']).filter(process='issue')
        if not q1:
            result['issue_transactions'] = 'No transactions'
        else:
            result['issue_transactions']= serializers.serialize('json',q1, fields=('challanid','assignmentdate','qty'))
            #result['issue_transactions'] =q1
        q2 = product.assignment_set.filter(karigar=result['karigar']).filter(process='receive')
        if not q2:
            result['receive_transactions']= 'No transactions'
        else:
            result['receive_transactions'] = serializers.serialize('json',q2, fields=('challanid','assignmentdate','qty'))
            #result['receive_transactions'] =q2
        q3 = product.assignment_set.filter(karigar=result['karigar']).filter(process='reissue')
        if not q3:
            result['reissue_transactions']= 'No transactions'
        else:
            result['reissue_transactions'] =serializers.serialize('json',q3, fields=('challanid','assignmentdate','qty'))
            #result['reissue_transactions'] =q3
    data = json.dumps(list(resultset))
    print(f"returning data : {data}")
    #data = serializers.serialize("json", list(resultset), fields=('product','total_issued','sum_received','sum_reissued'))
    return HttpResponse(data, content_type='application/json')


def overview_challans(request):
    #reset_connection()
    try:
        return render(request, 'overview_challan.html')
    except Exception as e:
        return render(request,'server_error.html')

def getTableChallan(request):
    try:
        challan_id = request.GET['challan_id']
        challans_active_company = models.Assignment.objects.filter(product__company=get_active_company(request))
        if challan_id == 'all':
            q = challans_active_company.order_by('-assignment_id')[:500]
        else:
            q = challans_active_company.filter(challanid__icontains=challan_id).order_by('-assignment_id')[:500]
        data = serializers.serialize('json', q, use_natural_foreign_keys=True)

        return HttpResponse(data, content_type='application/json')
    except Exception as e:
        print(e)

def deleteAssignment(request):
    assignment_id = request.GET['assignment_id']
    q = models.Assignment.objects.filter(assignment_id=assignment_id)
    data = serializers.serialize('json', q, use_natural_foreign_keys=True)
    print(f"Deleting Assignemnt {data}")
    q.delete()
    return HttpResponse(data, content_type='application/json')


def overview_dates(request):
    try:
        return render(request, 'overview_date.html')
    except:
        return render(request, 'server_error.html')

def getTableDate_ActiveProducts(request):
    start_date = request.GET['start_date']
    end_date = request.GET['end_date']
    active_products = models.Assignment.objects.exclude(process='issue').filter(assignmentdate__range=[start_date,end_date], product__company=get_active_company(request)).values('karigar__profile','product', 'product__prodid').annotate(
        sum_received=Sum(
            Case(When(process='receive', then='qty'), default=Value(0), output_field=IntegerField())),
        sum_reissued=Sum(
            Case(When(process='reissue', then='qty'), default=Value(0), output_field=IntegerField())),
    ).order_by('product')

    data = json.dumps(list(active_products))
    print(data)
    return HttpResponse(data, content_type='application/json')

def getTableData_Process(request):
    start_date = request.GET['start_date']
    end_date = request.GET['end_date']
    product = request.GET['product']
    process = request.GET['process']
    resultset = models.Assignment.objects.exclude(process='issue').filter(assignmentdate__range=[start_date,end_date]).\
        filter(karigar__profile=process).filter(product__prodid=product).order_by('karigar')
    data = serializers.serialize('json',resultset)
    return HttpResponse(data, content_type='application/json')


def switch_company(request):
    if request.method == "GET":
        companies = models.Company.objects.all()
        active_company = get_active_company(request)
        print(active_company)
        return render(request, 'company_context.html', {'companies': companies, 'active_company_id': active_company})

    elif request.method == "POST":
        selected_company_id = request.POST.get('company-dropdown', 1)
        set_active_company(request, selected_company_id)
        response = HttpResponseRedirect('../../products_all/')
        messages.success(request, f"Switched to {get_active_company_name(request)}")
        return response





