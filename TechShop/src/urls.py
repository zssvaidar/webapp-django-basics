from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from src.bone import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('src.bone.urls', 'bone'), namespace='bone')),
    path('', views.main, name='main'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.Register, name='register'),

    # path('', include('src.bone.urls'))
]
if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
