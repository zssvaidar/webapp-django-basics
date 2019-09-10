from django import forms
from .models import Book, Author, Publisher, Category, bookRibbon

class BookForm(forms.ModelForm):
    description = forms.CharField( widget=forms.Textarea(attrs={'rows': 6, 'cols': 54}))
    class Meta:
        model = Book
        fields = '__all__'
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
class RibbonForm(forms.ModelForm):
    class Meta:
        model = bookRibbon
        fields = '__all__'
