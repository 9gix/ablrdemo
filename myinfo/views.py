from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import UserProfile
from django.urls import reverse
from django.core.serializers.json import DjangoJSONEncoder
import json
from myinfo.client import MyInfoClient
from django.contrib.auth.decorators import login_required


def login_view(request):
    url = MyInfoClient.get_authorise_url(state="blahblah", callback_url=request.build_absolute_uri(reverse('auth-callback')))
    print(url)
    print(request.build_absolute_uri(reverse('auth-callback')))
    return redirect(url)

def auth_callback(request):
    user = authenticate(code=request.GET['code'])
    if user:
        login(request, user)
    return redirect('myinfo:contact')


@login_required
def income(request):
    return render(request, 'myinfo/income.html')

@login_required
def contact(request):
    profile_data = UserProfile.objects.filter(user=request.user).values()[0]
    context = {
        "contact_info": json.dumps({
            "email": request.user.email,
            **profile_data
        }, cls=DjangoJSONEncoder)
    }
    return render(request, 'myinfo/contact.html', context)


@login_required
def personal(request):
    profile_data = UserProfile.objects.filter(user=request.user).values()[0]
    context = {
        "personal_info": json.dumps({
            "name": request.user.first_name,
            **profile_data
        }, cls=DjangoJSONEncoder)
    }

    return render(request, 'myinfo/personal.html', context)


@login_required
def other(request):
    return render(request, 'myinfo/other.html')