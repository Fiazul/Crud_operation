# Generated by Django 5.0.6 on 2024-05-16 09:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='registration_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
