import re

from bootstrap_modal_forms.forms import BSModalModelForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import *


## форма создания юзера
class CreateUserForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', "password1", "password2", "email", "stud_email", "phone")


## форма логина
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Учебная почта', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Учебная почта', 'type': 'text', "autocomplete": "stud_email"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Пароль', 'type': 'password'}))

