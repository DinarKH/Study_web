from django.contrib import admin
from .models import UserProfile, Lesson, Comment, Subject, Example, CommentExample

# Register your models here.

admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Subject)
admin.site.register(Example)
admin.site.register(CommentExample)

