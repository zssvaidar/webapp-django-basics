from                 django.shortcuts  import render, redirect
from              django.contrib.auth  import authenticate, login, logout
from       django.contrib.auth.models  import User
from        django.contrib.auth.forms  import UserCreationForm, AuthenticationForm, UserChangeForm
from        invoice_management.models  import iv_items, iv_item_specification, iv_cart
from invoice_profile_management.forms  import EditUserForm, EditAdminForm

def login_V(request):

        form = AuthenticationForm(data = request.POST)
        if(form.is_valid()):
            user = form.get_user()
            login(request, user)
            return redirect('invoices_page')
        form = AuthenticationForm()

        return render(request, 'registration/login.html',{'form':form})
def reg_V(request):

        if(request.method == 'POST'):
            form = UserCreationForm(request.POST)
            if(form.is_valid()):
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                user = authenticate(username = username, password = password)
                if(request.user.is_superuser):
                    return redirect('invoices_page')
                else:
                    login(request, user)
                    return redirect('invoices_page')
        form = UserCreationForm()
        return render(request, 'registration/register.html',{'form' : form})

def logout_V(request):
        logout(request)
        return redirect('invoices_page')

def profile_UPDATE(request):

        if(request.method == 'POST'):
            if(request.user.is_staff):
                form = EditAdminForm(request.POST, instance = request.user)
            else:
                form = EditUserForm(request.POST, instance = request.user)
            if(form.is_valid()):
                form.save()

        return redirect('invoice_profile_management:profile')
