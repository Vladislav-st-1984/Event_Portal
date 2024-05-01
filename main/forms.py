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

class BsClassStyleForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super(BsClassStyleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UpdateProfile(ClassStyleForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'middle_name', "email", "stud_email", "phone", 'avatar']


class UpdateEventsForm(BsClassStyleForm):
    class Meta:
        model = Event
        fields = ['date', 'time', 'address', 'title', 'information', 'contact_phone', 'contact_email', 'contact_website', 'googleMap_address_link', 'img']
        widgets = {
            "date": forms.DateInput(attrs={'class': 'form-control datepicker mr-2', 'id': 'datepicker', }),
        }

    def clean_time(self):
        number = self.cleaned_data['time']
        tpl = "^([0-1]?[0-9]|2[0-3]):[0-5][0-9]-([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
        print(number)
        if re.match(tpl, number) is not None:
            return number
        else:
            raise forms.ValidationError("Формат времени обязан быть XX:XX-XX:XX")


class UpdateStageForm(BsClassStyleForm):
    class Meta:
        model = Stage
        fields = ['title', 'date', 'time', 'contact_email', 'event', 'information', 'img']
        widgets = {
            "date": forms.DateInput(attrs={'class': 'form-control datepicker mr-2', 'id': 'datepicker', }),
        }

    def clean_time(self):
        number = self.cleaned_data['time']
        tpl = "^([0-1]?[0-9]|2[0-3]):[0-5][0-9]-([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
        print(number)
        if re.match(tpl, number) is not None:
            return number
        else:
            raise forms.ValidationError("Формат времени обязан быть XX:XX-XX:XX")
