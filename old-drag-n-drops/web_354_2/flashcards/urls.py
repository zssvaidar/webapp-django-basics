from django.urls import path
from . import views


urlpatterns = [
    path('registerForm', views.registerForm, name = 'registerForm'),
    path('', views.createUser, name = 'createUser')

]
