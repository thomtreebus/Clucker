# Generated by Django 3.2.5 on 2021-11-12 21:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblogs', '0002_auto_20211015_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='followees', to=settings.AUTH_USER_MODEL),
        ),
    ]
