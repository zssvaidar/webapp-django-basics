from                  django.contrib  import admin
from                     django.conf  import settings
from                     django.urls  import path, include
from              invoice_management  import views
from      invoice_profile_management  import views_auth
from         django.conf.urls.static  import static
from django.contrib.staticfiles.urls  import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('invoice_management.urls','invoice_management'),namespace='invoice_management')),
    path('',include(('invoice_profile_management.urls','invoice_profile_management'),namespace='invoice_profile_management')),
    path('',                    views.main_V,name='invoices_page'),
    path('invpage/login/',      views_auth.login_V,name='login'),
    path('invpage/logout/',     views_auth.logout_V,name='logout'),
    path('invpage/register/',   views_auth.reg_V,name='register'),
]
if(settings.DEBUG):
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    # urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
