from django.contrib import admin
from django.urls import re_path, path, include
from django.conf import settings
from myinfo import urls as myinfo_urls
from myinfo import views as myinfo_views
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda req: redirect('myinfo:contact')),
    path('admin/', admin.site.urls),
    path('myinfo/', include(myinfo_urls)),
    path('login', myinfo_views.login_view, name='login'),
    path('callback', myinfo_views.auth_callback, name='auth-callback'),
]