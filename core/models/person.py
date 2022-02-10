from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return self.name
