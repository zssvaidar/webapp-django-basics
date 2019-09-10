from django.urls import path
from . import views
app_name="bookstore_managment"
urlpatterns = [
    path('addBook/',views.addBook, name = 'addBook'),
]
