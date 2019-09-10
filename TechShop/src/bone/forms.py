from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import customer, product_category, product_type,  product, product_option, product_attribute, product_description

class product_categoryForm(forms.ModelForm):
        title = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control'}), label='Category:')
        class Meta:
            model = product_category
            fields = '__all__'

class product_typeForm(forms.ModelForm):
        title = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), label='Type:')
        category_id = forms.ModelChoiceField(queryset=product_category.objects.all(), widget = forms.Select(attrs={'class':'form-control'}),label='Category:')
        class Meta:
            model = product_type
            fields = '__all__'

class productForm(forms.ModelForm):
        name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), label='Product:')
        product_type_id = forms.ModelChoiceField(queryset=product_type.objects.all(), widget = forms.Select(attrs={'class':'form-control'}),label='Product Type:')
        desc_qtty = forms.IntegerField(initial=3, widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Qtty'}),label='Description Qtty:')
        class Meta:
            model = product
            fields = '__all__'

class product_optionForm(forms.ModelForm):
        name_id = forms.ModelChoiceField(queryset=product.objects.all(), widget = forms.Select(attrs={'class':'form-control'}),label='Product')
        price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Price'}),label='Price:')
        class Meta:
            model = product_option
            fields = '__all__'
            exclude = ['image']

class product_attributeForm(forms.ModelForm):
        name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), label='Attribute name:')
        class Meta:
            model = product_attribute
            fields = '__all__'

class product_descriptionForm(forms.ModelForm):
    product_option_id = forms.ModelChoiceField(queryset=product_option.objects.all(), widget = forms.Select(attrs={'class':'form-control'}), label='Option')
    product_attribute_id = forms.ModelChoiceField(queryset=product_attribute.objects.all(), widget = forms.Select(attrs={'class':'form-control'}), label='Attribute')
    value = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Value'}), label='Value:')
    class Meta:
        model = product_description
        fields = '__all__'
class customerForm(forms.ModelForm):
        username = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'username'}), label='Username:')
        phone = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'username'}), label='Phone:')
        class Meta:
            model = customer
            fields = '__all__'
            exclude = ['is_staff','is_active','date_joined']
class StuForm(forms.ModelForm):

        class Meta:
            model = User
            fields = '__all__'
            exclude = ['is_staff','is_active','date_joined']

class AdminForm(UserChangeForm):
    class Meta:
        model = User
        fields = {'username','first_name', 'last_name', 'email', 'password'}
        exclude = ['is_staff','is_active','date_joined']
