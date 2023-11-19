# myapp/urls.py

from django.urls import path
from .views import item_list, item_create

urlpatterns = [
    path('items/', item_list, name='item-list'),
    path('items/create/', item_create, name='item-create'),
]
