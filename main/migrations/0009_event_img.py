# Generated by Django 5.0.3 on 2024-04-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_stage_img_users_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='img',
            field=models.ImageField(default='EventsImg/default/kot.png', upload_to='EventsImg/%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]