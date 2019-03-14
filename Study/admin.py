from django.contrib import admin
from .models import UserProfile, Lesson, Comment, Subject

# Register your models here.

admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Subject)
