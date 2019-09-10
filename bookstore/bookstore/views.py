from django.shortcuts import render, redirect
from .models import Book, Author, Publisher, bookRibbon, Category, Cart
from .forms import BookForm , AuthorForm, PublisherForm, CategoryForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
'''
custom bookstore's admin system
'''
def adminPage(request):
        form = BookForm(request.POST)
        form1 = AuthorForm(request.POST)
        form2 = PublisherForm(request.POST)
        form3 =  CategoryForm(request.POST)
        context = {
        'form' : form,
        'form1' : form1,
        'form2' : form2,
        'form3' : form3,
        }
        return render(request, 'bookstore/adminPage.html', context)
'''
book shelf filtered by category
'''
def Section(request, id):
        category_qset = Category.objects.all()
        bookRibbon_qset = bookRibbon.objects.filter(title_fk = id)
        context =  {
            'categories' : category_qset,
            'shelf' : bookRibbon_qset,
        }
        return render(request, 'bookstore/Section.html', context)
'''
django's builtin usermanagment system
'''
def login_view(request):
        if(request.method == 'POST'):

            form = AuthenticationForm(data = request.POST)
            print(form)
            if(form.is_valid()):
                user = form.get_user()
                login(request, user)
                return redirect('bookstore:bookShelf')
        form = AuthenticationForm()
        category_qset = Category.objects.all()
        context = {
            'form' : form,
            'categories' : category_qset,
        }
        return render(request, 'registration/login.html', context)
def logout_view(request):
        if(request.method == 'POST'):
             logout(request)
        return redirect('bookstore:bookShelf')
def register_view(request):
        if(request.method == 'POST'):
            form = UserCreationForm(request.POST)
            if(form.is_valid()):
            #     print("****")
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('bookstore:bookShelf')

        form = UserCreationForm()


        category_qset = Category.objects.all()
        context =  {
            'form' : form,
            'categories' : category_qset,
        }
        return render(request, 'registration/register.html', context)
'''
Main book store page
'''
def bookShelf(request):
        bookRibbon_qset = bookRibbon.objects.all()
        category_qset = Category.objects.all()
        context = {
            'shelf' : bookRibbon_qset,
            'categories' : category_qset,
        }
        return render(request, 'bookstore/bookStoreMain.html', context)
'''
Book order, description page
'''
def bookPage(request, id):
        book_qset = Book.objects.get(id=id)
        intt = str(int(13+id))
        category_qset = Category.objects.all()

        context = {
            'book' : book_qset,
            'categories' : category_qset,
            # 3h.aaidar@gmail.com
        }
        return render(request, 'bookstore/bookPage.html', context)
'''
Cart Page System
'''
def addtoCart(request, id):
        current_user = request.user
        current_book =  Book.objects.get(id=id)
        newcartRow = Cart(user_fk = current_user, book_fk = current_book)
        newcartRow.save()
        return redirect('bookstore:bookPage', id=id)
def deletefCart(request, id):
        dQuery = Cart.objects.get(id=id).delete()
        return redirect('bookstore:cartPage')
def cartPage(request):
        category_qset = Category.objects.all()
        current_user = request.user
        cartbooks =  Cart.objects.filter(user_fk = current_user)
        context = {
        'cartbooks' : cartbooks,
        'user' : current_user,
        'categories' : category_qset,
        }
        return render(request, 'bookstore/cartPage.html', context)
