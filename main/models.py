from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Users(AbstractUser):
    email = models.EmailField("Почта", unique=True, blank=False)
    stud_email = models.EmailField("Учебная почта", unique=True, blank=False)
    first_name = models.CharField("Имя", max_length=250, blank=False)
    last_name = models.CharField("Фамилия", max_length=250, blank=False)
    # avatar = models.ImageField('Аватар', upload_to='avatar/%Y/%m/%d/', default='avatar/default/kot.png')
    middle_name = models.CharField('Отчество', max_length=250, blank=True, null=True)
    phone = PhoneNumberField("Номер телефон", null=True, blank=True)

    def __str__(self):
        return self.email