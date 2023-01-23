"""review_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from admindashboard.views import index, add_category, edit_category, delete_category, add_user, remove_user
import admindashboard 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add/', add_category, name='add_category'),
    path('edit/<int:pk>/', edit_category, name='edit_category'),
    path('delete/<int:pk>/', delete_category, name='delete_category'),
    path('add_user/', add_user, name='add_user'),
    path('remove_user/<str:username>', remove_user, name='remove_user')
]

