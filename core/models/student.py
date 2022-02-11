from django.db import models


class Module(models.Model):
    module_name = models.CharField(max_length=120)
    class_room = models.CharField(max_length=20)
    module_desc = models.TextField()

    def __str__(self):
        return self.module_name


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return self.name
