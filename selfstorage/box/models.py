from django.contrib.auth.models import User
from django.db import models

from .managers import DisplayCostQuerySet


class Thing(models.Model):
    name = models.CharField('название', max_length=200)
    min_storage_time = models.PositiveIntegerField('минимальное время хранения, сут.')
    max_storage_time = models.PositiveIntegerField('максимальное время хранения, сут.')
    storage_cost = models.DecimalField('стоимость за минимальное время хранения',
                                       max_digits=5, decimal_places=2)

    objects = DisplayCostQuerySet.as_manager()

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField('картинка')
    thing = models.OneToOneField(Thing, on_delete=models.CASCADE,
                                 primary_key=True, verbose_name='относится к вещи')

    def __str__(self):
        return f'{self.thing.name}'


class Place(models.Model):
    address = models.TextField('адрес', help_text='ул. Манчестерская, д. 7, кв. 1')
    longitude = models.FloatField('долгота')
    latitude = models.FloatField('широта')

    def __str__(self):
        return f'{self.address}'


class Storage(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE,
                                 primary_key=True,
                                 verbose_name='расположен по адресу')
    alias = models.CharField('запоминающееся название', max_length=128)
    cost = models.DecimalField('стоимость аренды, руб/кв.м.',
                               max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.alias}'


class Box(models.Model):
    storages = models.ManyToManyField(Storage, blank=True,
                                      related_name='boxes'
                                      )
    things = models.ManyToManyField(Thing, blank=True,
                                    related_name='assosiated_boxes'
                                    )

    def __str__(self):
        return f'Бокс №{self.id}'


class Order(models.Model):
    things_names = models.CharField('названия вещей', max_length=200)
    number_of_things = models.PositiveIntegerField('кол-во единиц вещей', default=1)
    storage_address = models.TextField('адрес склада',
                                       default='ул. Манчестерская, д. 7, кв. 1')

    tenant = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='orders')
