# Generated by Django 5.0.3 on 2024-04-04 19:15

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта для связи'),
        ),
        migrations.AddField(
            model_name='event',
            name='contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Номер телефон для связи'),
        ),
        migrations.AddField(
            model_name='event',
            name='contact_website',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Вебсайт мероприятия'),
        ),
    ]
