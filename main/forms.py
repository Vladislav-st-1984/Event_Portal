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

class ClassStyleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClassStyleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
class UpdateProfile(ClassStyleForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'middle_name', "email", "stud_email", "phone"]
