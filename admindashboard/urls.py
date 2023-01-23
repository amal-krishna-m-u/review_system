from django.urls import path
from .views import index, add_category, edit_category, delete_category

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_category, name='add_category'),
    path('edit/<int:pk>/', edit_category, name='edit_category'),
    path('delete/<int:pk>/', delete_category, name='delete_category'),
]
