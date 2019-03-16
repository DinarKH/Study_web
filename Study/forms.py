from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Lesson, Comment, Subject


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email",)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'text'}
        exclude = ('lesson',)


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)
    subject_search = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.Select)
