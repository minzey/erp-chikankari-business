from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
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
                return HttpResponseRedirect('/karigars_all/')
    return render(request,'loginapp.html')

@login_required(login_url='/login/')

def homepage(request):
    return render(request, '../templates/homepage.html')



def new_karigar(request):
    form = forms.KarigarForm()
    if request.method == 'POST':
        form = forms.KarigarForm(request.POST,request.FILES)
        if form.is_valid():
            karigar = form.save()
            messages.success(request, "New Karigar added.")
            return HttpResponseRedirect('../../karigars_all/')
    return render(request, '../templates/newkarigar_form.html', {'form':form})

def edit_karigar(request,name_pk):
    karigar = get_object_or_404(models.Karigar,pk=name_pk)
    form = forms.KarigarForm(instance=karigar)
    if request.method == 'POST':
        form = forms.KarigarForm(request.POST, request.FILES, instance=karigar)
        if form.is_valid():
            karigaredit = form.save()
            messages.success(request,"Karigar information updated.")
            return HttpResponseRedirect('../../karigars_all/')
    return render(request, '../templates/newkarigar_form.html', {'form': form})

def delete_karigar(request,name_pk):
    models.Assignment.objects.filter(karigar=name_pk).delete()
    models.Karigar.objects.filter(pk=name_pk).delete()

    messages.success(request,"All records of "+name_pk+" deleted!")
    return HttpResponseRedirect('../../karigars_all/')


def new_product(request):
    form = forms.ProductForm()
    if request.method == 'POST':
        form = forms.ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.fabric = product.fabric.lower()
            product.colour = product.colour.lower()
            product.save()
            messages.success(request,"New product added.")
            return HttpResponseRedirect('../../products_all/')
    return render(request, '../templates/newproduct_form.html', {'form':form})

def edit_product(request, id_pk):
    product = get_object_or_404(models.Product,pk=id_pk)
    form = forms.ProductForm(instance=product)
    if request.method == 'POST':
        form = forms.ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request,"Product information updated.")
            return HttpResponseRedirect('../../products_all/')
    return render(request, '../templates/newproduct_form.html', {'form':form})

def delete_product(request,id_pk):
    product = get_object_or_404(models.Product,pk=id_pk)
    models.Assignment.objects.filter(product=product).delete()
    models.Product.objects.filter(pk=id_pk).delete()

    messages.success(request,"All records of "+id_pk+" deleted!")
    return HttpResponseRedirect('../../products_all/')


def assign_product(request,name_pk):
    karigar = get_object_or_404(models.Karigar,pk=name_pk)
    formset = forms.AssignFormSet(queryset=models.Assignment.objects.none())
    errors = []

    for form in formset:
        form.fields['product'].queryset = models.Product.objects.all()
    if request.method == 'POST':

        formset = forms.AssignFormSet(request.POST,
                                      queryset=models.Assignment.objects.none())
        if formset.has_changed(): #atleast one form entry found, validate Challan, Date and Process field
            if not request.POST['challan_id']:
                errors.append("Challan ID is required!")
            if not request.POST['date_assignment']:
                errors.append("Assignment date is required!")
            if request.POST.get('ck',None) == None:
                errors.append("Process selection [Issue / Receive / Reissue] is required!")

        if formset.is_valid() and errors == []: #check validity of product and qty field
            assignments = formset.save(commit=False)
            count_form=0
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

    return render(request, '../templates/assignment_form.html', {
        'formset': formset,
        'karigar': karigar,
        'errors': errors,
    })



def karigars_all(request):
    reset_connection()
    karigars = models.Karigar.objects.all().order_by('name')
    for karigar in karigars:
        karigar.photo = "/media/"+str(karigar.photo)
    return render(request, '../templates/karigar_list.html', {'karigars': karigars})

def products_all(request):
    reset_connection()
    products = models.Product.objects.all()
    for product in products:
        product.photo = "/media/"+str(product.photo)
    return render(request, '../templates/product_list.html', {'products': products})



def overview_karigars(request):
    reset_connection()
    klist = models.Karigar.objects.all()
    return render(request, 'overview_karigar.html',{'klist': klist})




def getTableKarigar(request):

    name_pk = request.GET['karigar_name']
    karigar = get_object_or_404(models.Karigar, pk=name_pk)
    resultset = models.Assignment.objects.filter(karigar=karigar).values('product').annotate(
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
        q1 = karigar.assignment_set.filter(product=result['product']).filter(process='issue')
        if not q1:
            result['issue_transactions'] = 'No transactions'
        else:
            result['issue_transactions']= serializers.serialize('json',q1, fields=('challanid','assignmentdate','qty'))
            #result['issue_transactions'] =q1
        q2 = karigar.assignment_set.filter(product=result['product']).filter(process='receive')
        if not q2:
            result['receive_transactions']= 'No transactions'
        else:
            result['receive_transactions'] = serializers.serialize('json',q2, fields=('challanid','assignmentdate','qty'))
            #result['receive_transactions'] =q2
        q3 = karigar.assignment_set.filter(product=result['product']).filter(process='reissue')
        if not q3:
            result['reissue_transactions']= 'No transactions'
        else:
            result['reissue_transactions'] =serializers.serialize('json',q3, fields=('challanid','assignmentdate','qty'))
            #result['reissue_transactions'] =q3
    data = json.dumps(list(resultset))
    #data = serializers.serialize("json", list(resultset), fields=('product','total_issued','sum_received','sum_reissued'))
    return HttpResponse(data, content_type='application/json')


def overview_products(request):
    reset_connection()
    plist = models.Product.objects.all()
    return render(request, 'overview_product.html', {'plist': plist})


def getTableProduct(request):

    product_pk = request.GET['product_id']
    product = get_object_or_404(models.Product, pk=product_pk)
    resultset = models.Assignment.objects.filter(product=product).values('karigar').annotate(
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
    #data = serializers.serialize("json", list(resultset), fields=('product','total_issued','sum_received','sum_reissued'))
    return HttpResponse(data, content_type='application/json')


def overview_challans(request):
    reset_connection()
    clist = models.Assignment.objects.all().values('challanid').distinct()
    return render(request, 'overview_challan.html', {'clist': clist})

def getTableChallan(request):
    challan_id = request.GET['challan_id']
    if challan_id == 'all':
        q = models.Assignment.objects.all().order_by('-assignment_id')
    else:
        q = models.Assignment.objects.filter(challanid=challan_id)
    data = serializers.serialize('json',q)
    #data = json.dumps(list(q))
    return HttpResponse(data, content_type='application/json')

def deleteAssignment(request):
    challan_id = request.GET['challan_id']
    product = request.GET['product']
    qty = request.GET['qty']
    karigar = request.GET['karigar']
    q = models.Assignment.objects.filter(challanid=challan_id).filter(product=product).filter(karigar=karigar).filter(qty=qty)
    data = serializers.serialize('json',q)
    models.Assignment.objects.filter(challanid=challan_id).filter(product=product).filter(karigar=karigar).filter(qty=qty).delete()

    return HttpResponse(data, content_type='application/json')


def overview_dates(request):
    return render(request, 'overview_date.html')

def getTableDate_ActiveProducts(request):
    start_date = request.GET['start_date']
    end_date = request.GET['end_date']
    active_products = models.Assignment.objects.exclude(process='issue').filter(assignmentdate__range=[start_date,end_date]).values('karigar__profile','product').annotate(
        sum_received=Sum(
            Case(When(process='receive', then='qty'), default=Value(0), output_field=IntegerField())),
        sum_reissued=Sum(
            Case(When(process='reissue', then='qty'), default=Value(0), output_field=IntegerField())),
    ).order_by('product')

    data = json.dumps(list(active_products))
    return HttpResponse(data, content_type='application/json')

def getTableData_Process(request):
    start_date = request.GET['start_date']
    end_date = request.GET['end_date']
    product = request.GET['product']
    process = request.GET['process']
    resultset = models.Assignment.objects.exclude(process='issue').filter(assignmentdate__range=[start_date,end_date]).\
        filter(karigar__profile=process).filter(product=product).order_by('karigar')
    data = serializers.serialize('json',resultset)
    return HttpResponse(data, content_type='application/json')



