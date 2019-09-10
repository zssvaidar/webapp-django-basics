from django.urls import path
from . import views

urlpatterns = [
    path('invoice/edit/<int:id>',               views.edit_inv_V,name='edit_invoice'),
    path('invoice/admin/delete/<int:id>/',      views.delete_inv_V,name='invoice_delete'),
    path('invoice/customer/delete/<int:id>/',   views.delete_inv_customer,name='invoice_delete_customer'),
    path('invoice/add/',                        views.add_inv_V,name='invoice_add'),
    path('addtocart/<int:item_id>/',            views.inv_GET,name='item_get'),
]
