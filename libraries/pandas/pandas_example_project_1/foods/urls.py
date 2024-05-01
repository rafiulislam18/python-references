from django.urls import path
from .views import show_food_list

urlpatterns = [
    path('', show_food_list, name='show_food_list'),
]