from django.shortcuts import render, redirect
from bookstore.forms import BookForm, AuthorForm, PublisherForm, CategoryForm, RibbonForm
from django.db import transaction
'''

'''
def addBook(request):
    if(request.method == 'POST'):
        Category_form = CategoryForm(request.POST)
        Author_form = AuthorForm(request.POST)
        Publisher_form = PublisherForm(request.POST)
        Book_form = BookForm(request.POST, request.FILES)
        Ribbon_form = RibbonForm()
        if(Author_form.is_valid and Publisher_form.is_valid and Book_form.is_valid and Category_form.is_valid):
            with transaction.atomic():
                category = Category_form.save()
                author = Author_form.save()
                publisher = Publisher_form.save()
                book = Book_form.save(commit=False)
                book.author_fk = author
                book.publisher_fk = publisher
                book.save()
                ribbon = Ribbon_form.save(commit=False)
                ribbon.title_fk = category
                ribbon.book_fk = book
                ribbon.save()

    return redirect('adminPage')
