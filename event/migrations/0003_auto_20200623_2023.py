# Generated by Django 3.0.6 on 2020-06-23 14:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20200621_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EventEndTime',
            field=models.TimeField(default=datetime.datetime(2020, 6, 23, 14, 53, 28, 903285, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventStartTime',
            field=models.TimeField(default=datetime.datetime(2020, 6, 23, 14, 53, 28, 903285, tzinfo=utc)),
        ),
    ]
