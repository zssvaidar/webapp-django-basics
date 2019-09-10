from django import forms
from .models import iv_items, iv_item_specification
class ItemForm(forms.ModelForm):
        qr=                 forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), label='QR:')
        product_name=       forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Name'}), label='Product name:')
        quantitity=         forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Quantity'}))
        price=              forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Price'}))
        specification_fk=   forms.ModelChoiceField(queryset=iv_item_specification.objects.all(), widget = forms.Select(attrs={'class':'form-control'}))
        class Meta:
            model = iv_items
            fields = '__all__'

class SpecificationForm(forms.ModelForm):
        name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
        class Meta:
            model = iv_item_specification
            fields = '__all__'
