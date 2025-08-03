from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(label='Введите текст с картинки')
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]