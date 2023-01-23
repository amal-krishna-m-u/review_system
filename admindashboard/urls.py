from django.urls import path

from django.urls import path
from .views import add_user, remove_user

urlpatterns = [
    path('add_user/', add_user, name='add_user'),
    path('remove_user/<str:username>', remove_user, name='remove_user'),
]
