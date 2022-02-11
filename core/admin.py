from django.contrib import admin
from core.models.category import Category
from core.models.student import Module, Student

admin.site.register(Category)
admin.site.register(Module)
admin.site.register(Student)
