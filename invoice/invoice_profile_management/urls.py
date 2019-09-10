from django.urls import path
from . import views_auth, views
urlpatterns = [
    path('profile/',                     views.profile_V,name='profile'),
    path('profile/update/',              views_auth.profile_UPDATE,name ='profile_update'),
    path('customer/',                    views.customer_PROF_V,name='customer_profile'),
    path('profile/delete/<int:id>/',     views.invoice_DELETE,name='invoice_delete_user'),
]
