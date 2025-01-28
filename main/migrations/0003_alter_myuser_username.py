# Generated by Django 5.1.5 on 2025-01-28 11:43

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_myuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=1, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
    ]
