from django.urls import path
from . import views as myinfo_views

app_name = 'myinfo'

urlpatterns = [
    path('contact', myinfo_views.contact, name='contact'),
    path('income', myinfo_views.income, name='income'),
    path('personal', myinfo_views.personal, name='personal'),
    path('other', myinfo_views.other, name='other'),
]