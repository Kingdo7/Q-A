# Generated by Django 4.0.3 on 2022-04-04 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='profile',
        ),
    ]
