# Generated by Django 3.2.6 on 2021-08-12 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reliefAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videolink',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
