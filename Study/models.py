from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Example(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    access = models.BooleanField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class CommentExample(models.Model):
    example = models.ForeignKey(Example, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    money = models.IntegerField(default=100)
    description = models.CharField(max_length=200)
    subscribe = models.ManyToManyField(Lesson, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
