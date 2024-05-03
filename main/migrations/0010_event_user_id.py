# Generated by Django 5.0.3 on 2024-04-27 11:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_event_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='user_id',
            field=models.ManyToManyField(related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]