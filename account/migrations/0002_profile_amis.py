# Generated by Django 4.0.3 on 2022-03-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='amis',
            field=models.ManyToManyField(to='account.profile'),
        ),
    ]