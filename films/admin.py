from django.contrib import admin
from .models import Category, Trailer, Film


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'creator', 'name', 'parent', 'is_active', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'parent', 'is_active']


admin.site.register(Category, CategoryAdmin)

admin.site.register(Trailer)
admin.site.register(Film)
