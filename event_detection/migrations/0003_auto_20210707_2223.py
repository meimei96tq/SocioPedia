# Generated by Django 3.1.1 on 2021-07-07 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_detection', '0002_auto_20210126_0442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='user',
        ),
        migrations.RemoveField(
            model_name='twittertoken',
            name='user',
        ),
    ]
