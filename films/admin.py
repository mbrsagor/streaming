from django.contrib import admin
from .models import Category, Trailer, Film, Purchase


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'creator', 'name', 'parent', 'is_active', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'parent', 'is_active']


admin.site.register(Category, CategoryAdmin)


class TrailerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'trailer_url', 'is_publish']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'is_publish']


admin.site.register(Trailer, TrailerAdmin)


class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'director', 'release_date', 'price', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price']


admin.site.register(Film, FilmAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'item', 'customer', 'quantity', 'payment', 'status', 'created_at']
    list_display_links = ['id', 'item']
    search_fields = ['item', 'status']


admin.site.register(Purchase, PurchaseAdmin)
