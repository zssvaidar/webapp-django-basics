from django.urls import path
from . import views
urlpatterns = [
    path('store/<str:category>/', views.category_section, name='category'),
    path('store/<str:category>/<str:type>/', views.type_section, name='type'),
    path('store/option/<int:id>/', views.product_section, name='product'),
    path('account/', views.account, name='account'),
    path('account/admin/addCategory/', views.addCategory, name='add_cat'),
    path('account/admin/addType/', views.addType,     name='add_type'),
    path('account/admin/addProduct/', views.addPoduct,  name='add_prod'),
    path('account/admin/addOption/', views.addOption,   name='add_opt'),
    path('account/admin/addAttribute/', views.addAttr,   name='add_attr'),
    path('account/admin/addDescription/', views.addDesc,   name='add_desc'),
]
