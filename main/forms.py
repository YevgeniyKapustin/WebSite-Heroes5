from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from main.models import Report


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['victory', 'myself', 'opponent', 'fraction_myself', 'fraction_opponent']
        widgets = {
            'myself': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'fraction_myself': forms.Select(attrs={'class': 'form-control'}),
            'fraction_opponent': forms.Select(attrs={'class': 'form-control'})
        }
