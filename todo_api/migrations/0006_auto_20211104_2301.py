# Generated by Django 3.2.4 on 2021-11-04 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0005_alter_todo_date_completed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_at',
            field=models.DateField(default=datetime.date(2021, 11, 4)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_completed_by',
            field=models.DateField(default=datetime.date(2021, 11, 4)),
        ),
    ]
