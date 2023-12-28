from django.urls import path
from .views import *


urlpatterns = [
    path('', view_animals_list, name='animal_main'),
    path('add', add_animal_breed),
    path('breed/<int:breed_id>', animal_detail),
    path('type/add', add_animal_type)
]