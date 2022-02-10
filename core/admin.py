from django.contrib import admin
from core.models.category import Category
from core.models.person import Person, Group

admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Group)
