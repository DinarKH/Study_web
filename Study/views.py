from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash
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
            form.save()
            new_user=authenticate(requst,username=form.cleaned_data['username'],
                                  password=form.cleaned_data['password1'])
            login(requst,new_user)
            return redirect('/home/')
        else:
            return render(requst, 'registration.html', {
                'form': form,
            })
    else:
        return render(requst, 'registration.html', {
            'form': RegistrationForm,
        })

def changePassword(request):
    if request.method=='POST':
        form =PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/home/')
        else:
            return redirect('/change_password/')
    else:
        form=PasswordChangeForm(user=request.user)
        return render(request,'change_password.html',{
            'form':form,
        })
