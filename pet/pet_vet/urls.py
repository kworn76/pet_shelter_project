from django.urls import path
from .views import index, services, shop, contacts, about, appointment

urlpatterns = [
    path('', index, name='index'),
    path('vet/', index, name='index'),
    path('services/', services, name='services'),
    path('appointment/', appointment, name='appointment'),
    path('shop/', shop, name='shop'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
]