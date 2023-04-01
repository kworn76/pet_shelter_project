from django.db import models


class Appointment(models.Model):
    client_name = models.CharField(max_length=150, verbose_name='Клиент')
    email = models.EmailField(max_length=150, )
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    pet_type = models.CharField(max_length=150, verbose_name='Животное')
    date = models.DateField(verbose_name='День приёма')

    class Meta:
        verbose_name = 'Приём'
        verbose_name_plural = 'Приёмы'


class Animals(models.Model):
    types = models.CharField(max_length=150,verbose_name='Вид')

    class Meta:
        verbose_name='Животное'
        verbose_name_plural = 'Животные'
