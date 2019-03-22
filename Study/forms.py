from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Lesson, Comment, CommentExample, \
    Subject, UserProfile, Example


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
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "write a comment...", 'rows': "3"}))

    class Meta:
        model = Lesson
        fields = ['name', 'description', 'subject', 'price']


class LessonEditForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "write a comment...", 'rows': "3"}))

    class Meta:
        model = Lesson
        fields = ['name', 'description', 'subject', 'price']


class ExampleForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "write a comment...", 'rows': "3"}))

    class Meta:
        model = Example
        fields = ['name', 'text',]


class ExampleEditForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "write a comment...", 'rows': "3"}))

    class Meta:
        model = Example
        fields = ['name', 'text', 'access']


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "write a comment...", 'rows': "3"}))

    class Meta:
        model = Comment
        fields = {'text'}
        exclude = ('lesson',)


class CommentExampleForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "write a comment...", 'rows': "3"}))

    class Meta:
        model = CommentExample
        fields = {'text'}
        exclude = ('example',)


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject_search = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.Select)


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('description', 'money')
