from django.contrib import admin

from .models import Blog, Author, Entry

admin.site.register([Blog, Author, Entry])
