from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()  # Par exemple, de 1 à 100.

    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    github = models.URLField()
    facebook = models.URLField()

    def __str__(self):
        return self.email
