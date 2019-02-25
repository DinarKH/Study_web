from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login
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


def loginView(request):
    return render(request, 'login.html',
        {
        'form': AuthenticationForm
    })


def registration(requst):
    if requst.method == 'POST':
        form = RegistrationForm(requst.POST)
        if form.is_valid():
            new_user=form.save()
            new_user=authenticate(requst,username=form.cleaned_data['username'],
                                  password=form.cleaned_data['password1'])
            login(requst,new_user)
            return redirect('/logim/')
        else:
            return render(requst, 'registration.html', {
                'form': form,
            })
    else:
        return render(requst, 'registration.html', {
            'form': RegistrationForm,
        })
