from django.shortcuts  import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm, UserChangeForm
from .models  import customer, product_category, product_type, product, product_option, product_attribute, product_description
from .forms  import product_categoryForm, product_typeForm, productForm, product_optionForm, product_attributeForm, product_descriptionForm
import random
def main(request):
    if(not request.POST):
        promo_id =[]
        times = round(product_option.objects.all().count())
        for i in range(times):
            r_numb = random.randint(0, product_option.objects.all().count())
            if(r_numb not in promo_id):
                promo_id.append(r_numb)
        context = {
            'form' : AuthenticationForm(),
            'categories' : product_category.objects.all(),
            'types' : product_type.objects.all(),
            'products' : product_option.objects.all(),
            'range' : int(product_option.objects.all().count()),
            'promo' : product_option.objects.filter(id__in=promo_id).exclude(image='')
        }
        return render(request, 'bone/main.html', context)
    else:
        form = AuthenticationForm(data = request.POST)
        if(form.is_valid()):
            user = form.get_user()
            login(request, user)
            if(request.user.is_superuser):
                context = {
                    'obj_prod_cat' : product_category.objects.all(),
                    'obj_prod_type' : product_type.objects.all(),
                    'obj_prod' : product.objects.all(),
                    'obj_prod_optn' : product_option.objects.all(),
                    'obj_prod_attr' : product_attribute.objects.all(),
                    'obj_prod_desc' : product_description.objects.all(),
                        'prod_cat' : product_categoryForm(),
                        'prod_type' : product_typeForm(),
                        'prod' : productForm(),
                        'prod_optn': product_optionForm(),
                        'prod_attr': product_attributeForm(),
                        'prod_desc': product_descriptionForm(),
                        'staff ' : User.objects.exclude(is_superuser=True)
                }
                return render(request,'bone/profile.html', context)
            elif(request.user.is_staff):
                context = {
                'prod_attr': product_attributeForm(),
                'prod_desc': product_descriptionForm(),
                'users ' : User.objects.all().exclude(is_staff=True)
                }
                return render(request,'bone/profile.html', context)

                return redirect ('main')
        else:
            return redirect('main')
def category_section(request, category):

    context = {
        'products' : product_option.objects.filter(name_id__product_type_id__category_id__title = category),
        'categories' : product_category.objects.all(),
        'types' : product_type.objects.all(),
        'range' : int(product_option.objects.all().count())
    }
    return render(request, 'bone/main.html', context)
def type_section(request, category, type):
    context = {
        'products' : product_option.objects.filter(name_id__product_type_id__title = type),
        'categories' : product_category.objects.all(),
        'types' : product_type.objects.all(),
        'range' : int(product_option.objects.all().count())
    }
    return render(request, 'bone/main.html', context)
def product_section(request, id):
    context = {
        'product' : product_option.objects.get(pk = id),
        'categories' : product_category.objects.all(),
        'types' : product_type.objects.all(),
        'range' : int(product_option.objects.all().count())
    }
    return render(request, 'bone/prod.html', context)
def addCategory(request):
    if(request.method == 'POST'):
        data = product_categoryForm(request.POST)
        if(data.is_valid()):
            title = data.cleaned_data["title"]
            data_obj = product_category(title = title)
            data_obj.save()
    return redirect('bone:account')
def addType(request):
    if(request.method == 'POST'):
        data = product_typeForm(request.POST)
        if(data.is_valid()):
            title = data.cleaned_data["title"]
            category_id = data.cleaned_data["category_id"]
            data_obj = product_type(title = title, category_id = category_id)
            data_obj.save()
    return redirect('bone:account')
def addPoduct(request):
    if(request.method == 'POST'):
        data = productForm(request.POST)
        if(data.is_valid()):
            name = data.cleaned_data["name"]
            product_type_id = data.cleaned_data["product_type_id"]
            desc_qtty = data.cleaned_data["desc_qtty"]
            data_obj = product(name = name, product_type_id = product_type_id, desc_qtty = desc_qtty)
            data_obj.save()

    return redirect('bone:account')
def addOption(request):
    if(request.method == 'POST'):
        data = product_optionForm(request.POST)
        if(data.is_valid()):
            name_id = data.cleaned_data["name_id"]
            price = data.cleaned_data["price"]
            data_obj = product_option(name_id = name_id, price = price, image = '')
            data_obj.save()
    return redirect('bone:account')
def addAttr(request):
    if(request.method == 'POST'):
        data = product_attributeForm(request.POST)
        if(data.is_valid()):
            name = data.cleaned_data["name"]
            data_obj = product_attribute(name = name)
            data_obj.save()
    return redirect('bone:account')
def addDesc(request):
    if(request.method == 'POST'):
        data = product_descriptionForm(request.POST)
        if(data.is_valid()):
            product_option_id = data.cleaned_data["product_option_id"]
            product_attribute_id = data.cleaned_data["product_attribute_id"]
            value = data.cleaned_data["value"]
            data_obj = product_description(product_option_id = product_option_id, product_attribute_id = product_attribute_id, value = value)
            data_obj.save()
    return redirect('bone:account')
def Logout(request):
    logout(request)
    return redirect('main')

def account(request):
    if(not request.POST):
        if(request.user.is_superuser):
            context = {
                'obj_prod_cat' : product_category.objects.all(),
                'obj_prod_type' : product_type.objects.all(),
                'obj_prod' : product.objects.all(),
                'obj_prod_optn' : product_option.objects.all(),
                'obj_prod_attr' : product_attribute.objects.all(),
                'obj_prod_desc' : product_description.objects.all(),
                    'prod_cat' : product_categoryForm(),
                    'prod_type' : product_typeForm(),
                    'prod' : productForm(),
                    'prod_optn': product_optionForm(),
                    'prod_attr': product_attributeForm(),
                    'prod_desc': product_descriptionForm(),
                    'staff ' : User.objects.exclude(is_superuser=True)
            }
            return render(request,'bone/profile.html', context)
        elif(request.user.is_staff):
            context = {
                'obj_prod_optn' : product_option.objects.all(),
                'prod_optn': product_optionForm(),
                'prod_attr': product_attributeForm(),
                'prod_desc': product_descriptionForm(),
                'users ' : User.objects.all().exclude(is_staff=True)
            }
            return render(request,'bone/profile.html', context)

            return redirect ('main')
    else:
        return redirect ('main')
def Register(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            if(request.user.is_superuser):
                user.is_staff=True
                user.save()
                return redirect('bone:account')
            else:
                login(request, user)
    return redirect('main')
