from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from bookstore import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminPage/', views.adminPage, name = 'adminPage'),
    path('', include(('bookstore.urls','bookstore'),namespace = 'bookstore')),
    path('adminPage/', include('bookstore_managment.urls', namespace='booksotre_managment')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.login_view, name = 'login'),
    path('accounts/register/',views.register_view, name='register'),
    path('logout/', views.logout_view, name = 'logout'),
]
if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
