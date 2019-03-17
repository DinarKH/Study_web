from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.core.paginator import Paginator
from .forms import RegistrationForm, LessonForm, LessonEditForm, CommentForm, SearchForm, UserProfileEditForm
from .models import Lesson, Comment, Subject, User


def home(request):
    return render(request, 'home.html', )


def lessons(request):
    search = request.GET.get('search_query')
    subject_search = request.GET.get('subject_search')
    if search is None:
        lessons_list = Lesson.objects.all()
        page_link = "?p="
    else:
        if search == '':
            print(subject_search)
            lessons_list = Lesson.objects.filter(subject=subject_search)
        else:
            lessons_list = Lesson.objects.filter(name__contains=search, subject=subject_search)
        page_link = '?search_query=' + search + "&subject_search=" + subject_search + "&p="
    page_limit = 2
    paginator = Paginator(lessons_list, page_limit)
    page = request.GET.get('p')
    page = paginator.get_page(page)
    return render(request, 'lessons.html',
                  {
                      'lessons_list': lessons_list,
                      'page': page,
                      'paginator': paginator,
                      'search_form': SearchForm,
                      'page_link': page_link,
                  })


def lessons_detail(request, number):
    instance = get_object_or_404(Lesson, id=number)
    comment_list = Comment.objects.filter(lesson=number)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.lesson_id = number
            form.instance.name = request.user.username
            form.save()
            return HttpResponseRedirect(request.path_info)
        else:
            return render(request, 'lesson_detail.html',
                          {
                              'instance': instance,
                              'form': CommentForm,
                          })
    return render(request, 'lesson_detail.html',
                  {
                      'instance': instance,
                      'form': CommentForm,
                      'comment_list': comment_list,
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
    try:
        user_name = request.GET.get('user')
        user_instance = User.objects.get(username=user_name)
        user_lessons = Lesson.objects.filter(user=user_instance)
        return render(request, 'user_profile.html', {
            'user': user_instance,
            'lessons': user_lessons,
        })
    except:
        return render(request, 'user_profile.html', {
        })


def addLesson(request):
    if request.method == 'POST':
        form = LessonForm(data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(request.path_info)
        else:
            return render(request, 'add_lesson.html', {
                'form': LessonForm,
            })
    else:
        return render(request, 'add_lesson.html', {
            'form': LessonForm,
        })


def editLesson(request, number):
    if request.method == 'POST':
        current_lesson = Lesson.objects.get(id=number)
        form = LessonEditForm(data=request.POST, instance=current_lesson)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(request.path_info)
        else:
            return render(request, 'edit_lesson.html', {
                'form': LessonEditForm,
            })
    else:
        return render(request, 'edit_lesson.html', {
            'form': LessonEditForm,
        })


def userProfileEdit(request):
    user_profile = request.user.profile

    if request.method == 'POST':
        form = UserProfileEditForm(data=request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
        else:
            return render(request, 'user_profile_edit.html', {
                'form': UserProfileEditForm,
            })
    else:
        return render(request, 'user_profile_edit.html', {
            'form': UserProfileEditForm,
        })
