from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class RegisterUserForm(UserCreationForm):
    FIO = forms.CharField(label='Фамилия имя отчество', widget=forms.TextInput(attrs={'class': 'form-input'}))
    number = forms.IntegerField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    # password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    required_css_class = "field"
    error_css_class = "error"

    class Meta:
        model = customuser
        fields = ("email", "FIO", "number")

class LoginUserForm(AuthenticationForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class AddbackConnection(forms.ModelForm):
    # FIO = forms.Charfield(max_length=120)
    class Meta:
        model = back_connection
        fields = '__all__'


