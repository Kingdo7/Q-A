# Generated by Django 4.0.3 on 2022-03-28 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_question_votelist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='author',
            new_name='profile',
        ),
    ]
