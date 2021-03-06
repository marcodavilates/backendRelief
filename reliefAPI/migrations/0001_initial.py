# Generated by Django 3.2.6 on 2021-08-12 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videoLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('urlVideo', models.URLField()),
                ('bookmark', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
