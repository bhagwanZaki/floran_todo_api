# Generated by Django 4.0.4 on 2022-10-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0007_auto_20211104_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, default='Description'),
        ),
    ]
