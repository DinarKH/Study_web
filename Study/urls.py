from django.urls import path,re_path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    re_path(r'^login/',auth_views.LoginView.as_view(template_name='login.html')),
    re_path(r'^logining/', views.login),
    path('',views.home),
]