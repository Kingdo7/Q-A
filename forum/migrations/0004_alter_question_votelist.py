# Generated by Django 4.0.3 on 2022-03-28 16:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0003_rename_author_question_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='votelist',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
