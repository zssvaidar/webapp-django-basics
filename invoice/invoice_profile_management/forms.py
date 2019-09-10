from django import forms
from django.contrib.auth.models import User
from invoice_management.models import iv_customer, iv_cart
from django.contrib.auth.forms import UserChangeForm
class Userform(forms.ModelForm):

        username=           forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'username'}), label='Username:')
        first_name=         forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Fist name'}), label=('Name:'))
        last_name=          forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Last Name'}), label=('Last name:'))
        email=              forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Email'}), label=('Email:'))
        class Meta:
            model = User
            fields = '__all__'
            exclude = ['is_staff','is_active','date_joined']
        # def __init__(self, *args, **kwargs):
        #     # username = kwargs.pop('username', None)
        #     first_name = kwargs.pop('first_name', None)
        #     last_name = kwargs.pop('last_name', None)
        #     email = kwargs.pop('email', None)
        #     # password = kwargs.pop('password', None)y
        #     super(Userform, self).__init__( **kwargs)
        #     # self.fields['username'].initial = username
        #     self.fields['first_name'].initial = first_name
        #     self.fields['last_name'].initial = last_name
        #     self.fields['email'].initial = email
        #     # self.fields['password'].initial = password

class CustomerForm(forms.ModelForm):

        business_name =         forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Name:')
        business_email =        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Email:')
        business_address =      forms.CharField(widget=forms.Textarea(attrs={'rows': 2,'cols': 30}), label='Address:')
        city =                  forms.CharField(widget=forms.TextInput(attrs={'class': 'cty form-control'}), label='Email:')
        country =               forms.CharField(widget=forms.TextInput(attrs={'class': 'ctry form-control'}), label='Country:')
        fax =                   forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='FAX:')
        class Meta:
            model = iv_customer
            fields = '__all__'
            exclude = ['user']

class CartForm(forms.ModelForm):
        quantitity = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '  Quantity'}))
        class Meta:
            model = iv_cart
            fields = ['quantitity']
            exclude = ['customer_fk','item_fk','date_invoice']

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email', 'password'}
        exclude = ['is_staff','is_active','date_joined']

class EditAdminForm(UserChangeForm):
    class Meta:
        model = User
        fields = {'username','first_name', 'last_name', 'email', 'password'}
        exclude = ['is_staff','is_active','date_joined']
