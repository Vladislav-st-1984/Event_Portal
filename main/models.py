# TODO: Вход по студ. меилу. Добавить проверку, является ли данная почта разрешенной.
#  Загрузку разрешенный почт сделать, как загрузку учителей

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class Users(AbstractUser):
    username = None
    email = models.EmailField("Почта", unique=True, blank=False)
    stud_email = models.EmailField("Учебная почта", unique=True, blank=False)
    first_name = models.CharField("Имя", max_length=250, blank=False)
    last_name = models.CharField("Фамилия", max_length=250, blank=False)
    # avatar = models.ImageField('Аватар', upload_to='avatar/%Y/%m/%d/', default='avatar/default/kot.png')
    middle_name = models.CharField('Отчество', max_length=250, blank=True, null=True)
    phone = PhoneNumberField("Номер телефон", null=True, blank=True)

    USERNAME_FIELD = "stud_email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Event(models.Model):
    date = models.DateField('День')
    time = models.CharField('Время', max_length=50, null=True, blank=True)
    address = models.CharField('Адрес', max_length=250, default="")
    title = models.CharField('Заголовок', max_length=250, default="")
    information = models.TextField('Информация о мероприятии', null=True, blank=True, default="")


    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return f"{self.title}"

