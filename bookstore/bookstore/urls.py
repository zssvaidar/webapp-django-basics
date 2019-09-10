from django.urls import path
from . import views

urlpatterns = [
    path('',views.bookShelf, name = 'bookShelf'),
    path('book/<int:id>/',views.bookPage, name = 'bookPage'),
    path('section/<int:id>',views.Section, name = 'Section'),
    path('addtocart/<int:id>',views.addtoCart, name = 'addtocart'),
    path('deletefromcart/<int:id>',views.deletefCart, name = 'deletefromcart'),
    path('cart', views.cartPage, name = 'cartPage'),
]
