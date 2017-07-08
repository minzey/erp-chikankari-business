from django import forms
from . import models
from django.forms.widgets import Select

class KarigarForm(forms.ModelForm):
    class Meta:
        model = models.Karigar
        fields = [
            'name',
            'profile',
            'address',
            'phone',
            'pan',
            'photo'
        ]


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['prodid'].label='Product ID'
        self.fields['cost_stitch'].label = 'Cost of Stitching'
        self.fields['cost_block'].label = 'Cost of Blocking'
        self.fields['cost_emb'].label = 'Cost of Embroidering'
        self.fields['cost_wash'].label = 'Cost of Washing'
        self.fields['cost_addon'].label = 'Cost of Addon'


    class Meta:
        model = models.Product
        fields = [
            'prodid',
            'fabric',
            'colour',
            'photo',
            'cost_stitch',
            'cost_block',
            'cost_emb',
            'cost_wash',
            'cost_addon'
        ]


class AssignForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        #CHOICES = models.Product.objects.all()
        fields = [

            'product',
            'qty'
        ]
        widgets = {
            #'product' : Select(choices=((x.prodid) for x in CHOICES )),
        }


AssignFormSet = forms.modelformset_factory(
    models.Assignment,
    form=AssignForm,
    extra=3,
)


