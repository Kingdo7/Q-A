# Generated by Django 4.0.3 on 2022-03-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('forum', '0005_alter_question_votelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='votelist',
            field=models.ManyToManyField(related_name='votequestionlist', to='account.profile'),
        ),
    ]