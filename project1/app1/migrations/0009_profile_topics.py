# Generated by Django 4.1.2 on 2022-10-16 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_topic_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='topics',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.topic'),
        ),
    ]
