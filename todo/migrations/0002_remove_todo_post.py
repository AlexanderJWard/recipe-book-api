# Generated by Django 3.2.20 on 2023-07-30 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='post',
        ),
    ]
