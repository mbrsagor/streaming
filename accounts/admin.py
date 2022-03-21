from django.contrib import admin
from .models import User, Profile


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'email', 'role', 'created_at']
    list_display_links = ['id', 'name']
    list_filter = ['name', 'email', 'phone_number']
    search_fields = ['email', 'phone_number']


admin.site.register(User, UserModelAdmin)


class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'auth', 'date_of_birth', 'address', 'created_at']
    list_display_links = ['id', 'auth']
    list_filter = ['auth', 'date_of_birth']
    search_fields = ['auth', 'date_of_birth']


admin.site.register(Profile, ProfileModelAdmin)
