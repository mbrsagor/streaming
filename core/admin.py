from django.contrib import admin
from core.models.article import Article
from core.models.category import Category

admin.site.register(Article)
admin.site.register(Category)
