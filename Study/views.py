from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegistrationForm
# from .models import Article
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html',)


def articles(request):
    return render(request, 'login.html')
    # article_list=Article.objects.all()
    # return render(request, 'articles.html',
    #               {
    #                   'articles':article_list,
    #               })


def login(request):
    return render(request, 'login.html',
        {
        'form': AuthenticationForm
    })


def registration(requst):
    if requst.method == 'POST':
        form = RegistrationForm(requst.POST)
        if form.is_valid():
            form.save()
            return redirect('/logim/')
        else:
            return render(requst, 'registration.html', {
                'form': form,
            })
    else:
        return render(requst, 'registration.html', {
            'form': RegistrationForm,
        })
