from django.urls import path, re_path, include
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView,
)
from . import views

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(template_name='login.html')),
    re_path(r'^logout/$', LogoutView.as_view(template_name='logout.html')),
    re_path(r'^articles/$', views.articles),
    re_path(r'^registration/$', views.registration),
    re_path(r'^change_password/$', views.changePassword),
    re_path(r'^password_reset/$', PasswordResetView.as_view(),name='password_reset'),
    re_path(r'^password_reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^', views.home),
]
