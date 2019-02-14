from django.contrib import admin
from .models import UserProfile,Lesson,Comment

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(UserProfile)
