# Generated by Django 3.2.6 on 2021-08-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reliefAPI', '0004_remove_videolink_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videolink',
            name='id',
        ),
        migrations.AlterField(
            model_name='videolink',
            name='urlVideo',
            field=models.URLField(primary_key=True, serialize=False),
        ),
    ]
