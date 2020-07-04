from django.contrib import admin
from core.models.publication import *
from core.models.article import *


admin.site.register(Publication)
admin.site.register(Article)
