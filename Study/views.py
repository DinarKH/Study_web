from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def login(request):
    args={
        'form':AuthenticationForm
    }
    return render(request,'login.html',args)