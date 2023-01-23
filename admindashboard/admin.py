from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, User

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','is_admin','created_at', 'updated_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
