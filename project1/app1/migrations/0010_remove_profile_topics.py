# Generated by Django 4.1.2 on 2022-10-16 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_profile_topics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='topics',
        ),
    ]