from django.db import models

from seasonal_keeping.models import Thing


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
    cost = models.DecimalField('стоимость аренды за 1 кв.м.',
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
