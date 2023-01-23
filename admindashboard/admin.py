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


from django.contrib.auth.models import User

def add_user(username, password, is_admin=False):
    user = User.objects.create_user(username=username, password=password)
    user.is_admin = is_admin
    user.save()
    return user


def remove_user(username):
    user = User.objects.get(username=username)
    user.delete()



