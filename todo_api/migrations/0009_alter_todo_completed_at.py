# Generated by Django 4.0.4 on 2023-06-13 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0008_todo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_at',
            field=models.DateField(blank=True),
        ),
    ]
