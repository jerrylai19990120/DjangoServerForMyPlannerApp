from django.db import models

# Create your models here.
class User(models.Model):

    username = models.TextField()

    password = models.TextField()

class Task(models.Model):

    owner = models.TextField(default="owner")

    title = models.TextField()

    desc = models.TextField()

    date = models.TextField()

    finished = models.BooleanField()
