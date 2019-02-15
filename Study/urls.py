from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html')),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html')),
    re_path(r'^articles/$', views.articles),
    re_path(r'^registration/$', views.registration),
    re_path(r'^', views.home),
]



