from django.urls import path
from .views import index, services, contacts, about, appointment

app_name = 'pet_vet_app'

urlpatterns = [
    path('', index, name='index'),

    path('services/', services, name='services'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('appointment', appointment, name='appointment'),
]