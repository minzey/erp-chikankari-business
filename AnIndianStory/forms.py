from django import forms
from django.core.exceptions import ValidationError

from . import models
from django.forms.widgets import Select

class KarigarForm(forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise ValidationError("Special characters not allowed in Karigar name. Please use A-Z only.")
        return str.capitalize(name)

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
    class Meta:
        model = models.Product
        fields = [
            'prodid',
            'company',
            'fabric',
            'colour',
            'photo',
            'cost_stitch',
            'cost_block',
            'cost_emb',
            'cost_wash',
            'cost_addon'
        ]
        labels = {
            'prodid': 'Product Name',
            'cost_stitch': 'Cost of Stitching per pc',
            'cost_block': 'Cost of Blocking per pc',
            'cost_emb': 'Cost of Embroidery per pc',
            'cost_wash': 'Cost of Washing per pc',
            'cost_addon': 'Cost of Addon per pc'
        }


class AssignForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = [

            'product',
            'size',
            'qty'
        ]


AssignFormSet = forms.modelformset_factory(
    models.Assignment,
    form=AssignForm,
    extra=6,
)


class EditAssignmentForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = [
            'challanid',
            'process',
            'karigar',
            'product',
            'size',
            'qty',
            'assignmentdate'
        ]
        widgets = {
            'assignmentdate': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'type':'date'}),
            'process': forms.Select(choices=(('issue','issue'), ('reissue','reissue'), ('receive','receive')))
        }