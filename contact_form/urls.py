from django.urls import path
from .views import *


urlpatterns = [
    path('',  add_contact_form, name='contact_form'),
    path('success',  success_page, name='contact_form_success'),
    path('not_success',  not_success_page, name='contact_form_not_success'),
]