# Generated by Django 3.1.5 on 2021-01-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('desc', models.TextField()),
                ('date', models.DateField()),
                ('finished', models.BooleanField()),
            ],
        ),
    ]
