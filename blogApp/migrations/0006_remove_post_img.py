# Generated by Django 3.1.12 on 2021-08-28 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
    ]
