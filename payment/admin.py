from django.contrib import admin
from .models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'item', 'customer', 'quantity', 'payment', 'status', 'created_at']
    list_display_links = ['id', 'item']
    search_fields = ['item', 'status']


admin.site.register(Purchase, PurchaseAdmin)
