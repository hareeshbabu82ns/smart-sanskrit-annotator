# Generated by Django 2.0.6 on 2018-06-11 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotatorapp', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='end_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='init_time',
            field=models.CharField(max_length=100),
        ),
    ]
