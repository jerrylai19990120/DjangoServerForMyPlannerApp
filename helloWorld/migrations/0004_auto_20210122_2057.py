# Generated by Django 3.1.5 on 2021-01-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0003_task_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.TextField(),
        ),
    ]