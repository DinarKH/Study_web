from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.core.paginator import Paginator
from .forms import RegistrationForm
from .models import Lesson


def home(request):
    return render(request, 'home.html', )


def lessons(request):
    lessons_list = Lesson.objects.all()
    paginator = Paginator(lessons_list, 2)
    page = request.GET.get('p')
    page = paginator.get_page(page)
    return render(request, 'lessons.html',
                  {
                      'lessons': lessons_list,
                      'page': page,
                      'paginator': paginator,
                  })


def lessons_detail(request, number):
    instance = get_object_or_404(Lesson, id=number)
    return render(request, 'lesson_detail.html',
                  {
                      'instance': instance
                  })


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
            new_user = authenticate(requst, username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(requst, new_user)
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
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/home/')
        else:
            return redirect('/change_password/')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'change_password.html', {
            'form': form,
        })

def userProfile(request):
    return render(request, 'user_profile.html',{
    })
