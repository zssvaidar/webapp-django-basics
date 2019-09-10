from           django.shortcuts  import render, redirect
from django.contrib.auth.models  import User
from                     .forms  import Userform, CustomerForm, EditUserForm
from  invoice_management.models  import iv_customer, iv_cart
from     django.core.exceptions  import ObjectDoesNotExist
def profile_V(request):
    form = Userform()
    current_user = request.user
    current_user_id=request.user.id-1
    form.fields['username'].initial=        User.objects.all()[current_user_id].username
    form.fields['first_name'].initial=      User.objects.all()[current_user_id].first_name
    form.fields['last_name'].initial=       User.objects.all()[current_user_id].last_name
    form.fields['email'].initial=           User.objects.all()[current_user_id].email

    if(current_user.is_staff):
        if(current_user.is_superuser):
            users = User.objects.all()
            return render(request, 'invoice_profile_management/profile.html', {'user_data':current_user,'form':form,'users':users})
        else:
            return render(request, 'invoice_profile_management/profile.html', {'user_data':current_user,'form':form})
    else:
        try:
            qr = iv_customer.objects.get(user = request.user)
        except ObjectDoesNotExist:
            qr = None
        if(qr):
            cust_qry=           iv_customer.objects.get(user = request.user)
            cart=               iv_cart.objects.filter(customer_fk = cust_qry)
            okc=                iv_customer.objects.get(user = current_user)
            cart=               iv_cart.objects.filter(customer_fk = okc)
            cust_id=            iv_customer.objects.filter(user = current_user)
            qr=                 iv_customer.objects.filter(user = current_user)
            customer_edit = CustomerForm()
            customer_edit.fields['business_address'].initial=   '%s %s' %("  ",qr[0].business_address)
            customer_edit.fields['business_name'].initial=      qr[0].business_name
            customer_edit.fields['business_email'].initial=     qr[0].business_email
            customer_edit.fields['city'].initial=               qr[0].city
            customer_edit.fields['country'].initial=            qr[0].country
            customer_edit.fields['fax'].initial=                qr[0].fax

            return render(request, 'invoice_profile_management/profile.html', {'customer_edit':customer_edit,'user_data':current_user,'form':form,'cart':cart})

        else:
            customer = CustomerForm()
            return render(request, 'invoice_profile_management/profile.html', {'user_data':current_user,'form':form,'customer':customer})

def customer_PROF_V(request):
    form=           Userform()
    customer_edit=  CustomerForm()
    current_user = request.user
    form.fields['username'].initial=      current_user.username
    form.fields['first_name'].initial=    current_user.first_name
    form.fields['last_name'].initial=     current_user.last_name
    form.fields['email'].initial=         current_user.email
    try:
        cust_qry = iv_customer.objects.get(user = request.user)
    except ObjectDoesNotExist:
        cust_qry = None
    if(cust_qry):
        cart = iv_cart.objects.filter(customer_fk = cust_qry)
        context = {'customer_edit':customer_edit,'user_data':current_user,'form':form,'cart':cart}
    else:
        context = {'customer_edit':customer_edit,'user_data':current_user,'form':form}
    if(request.method == 'POST'):
        form = CustomerForm(request.POST)
        if(form.is_valid()):
            form.save(commit=False)
            business_name=         form.cleaned_data["business_name"]
            business_email=        form.cleaned_data["business_email"]
            business_address=      form.cleaned_data["business_address"]
            city=                  form.cleaned_data["city"]
            country=               form.cleaned_data["country"]
            fax=                   form.cleaned_data["fax"]

            customer = iv_customer(               user=current_user,
            business_name=business_name,          business_email=business_email,
            business_address=business_address,    city=city,
            country=country,                      fax=fax)
            customer.save()
            context = {'customer_edit':customer_edit,'user_data':current_user,'form':form}
    if(request.method == 'GET'):
        customer_form = CustomerForm(request.GET)
        if(customer_form.is_valid()):
            customer_form.save(commit=False)
            qry_customer = iv_customer.objects.filter(user = current_user)
            if(qry_customer):
                business_name=          customer_form.cleaned_data["business_name"]
                business_email=         customer_form.cleaned_data["business_email"]
                business_address=       customer_form.cleaned_data["business_address"]
                city=                   customer_form.cleaned_data["city"]
                country=                customer_form.cleaned_data["country"]
                fax=                    customer_form.cleaned_data["fax"]
                qry_customer[0].business_name=      business_name
                qry_customer[0].business_email=     business_email
                qry_customer[0].business_address=   business_address
                qry_customer[0].city=     city
                qry_customer[0].country=  country
                qry_customer[0].fax=      fax
                qry_customer[0].save()
                return render(request, 'invoice_profile_management/profile.html', {'customer_edit':customer_form,'user_data':current_user,'form':form,'cart':cart})

    return render(request, 'invoice_profile_management/profile.html', context)
def invoice_DELETE(request, id):
    current_user =  request.user
    User.objects.get(id = id).delete()
    return redirect('profile')
