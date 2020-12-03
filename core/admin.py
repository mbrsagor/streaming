from django.contrib import admin
from core.models.publication import Publication
from core.models.article import Article


admin.site.register(Publication)
admin.site.register(Article)
