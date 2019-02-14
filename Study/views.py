from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
# from .models import Article
from django.http import HttpResponse


def home(request):
    print(request.user)
    return render(request, 'home.html',{
        'user':request.user,
    })


def articles(request):
    return render(request, 'login.html')
    # article_list=Article.objects.all()
    # return render(request, 'articles.html',
    #               {
    #                   'articles':article_list,
    #               })


def login(request):
    args = {
        'form': AuthenticationForm
    }
    return render(request, 'login.html', args)
