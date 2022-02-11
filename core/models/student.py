from django.db import models


class Module(models.Model):
    module_name = models.CharField(max_length=120)
    class_room = models.CharField(max_length=20, blank=True, null=True)
    module_desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.module_name


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return self.name
