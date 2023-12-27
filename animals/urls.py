from django.urls import path
from .views import *


urlpatterns = [
    path('', view_animals_list, name='animal_main'),
    path('add', add_animal_breed),
    path('type/add', add_animal_type)
]