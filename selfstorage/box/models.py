from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .managers import DisplayCostQuerySet


class Storage(models.Model):
    address = models.TextField(
        'адрес',
        help_text='ул. Манчестерская, д. 7, кв. 1'
    )
    longitude = models.FloatField('долгота')
    latitude = models.FloatField('широта')
    alias = models.CharField(
        'запоминающееся название',
        max_length=128,
        blank=True
    )
    first_square_meter_price = models.DecimalField(
        'стоимость аренды за первый квадратный метр, руб/кв.м.',
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=599
    )
    rest_square_meters_price = models.DecimalField(
        'стоимость аренды за все последующие квадратные метры кроме первого, руб/кв.м.',
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=150
    )

    def __str__(self):
        return f'{self.address}'


class Thing(models.Model):
    name = models.CharField('название', max_length=200)
    image = models.ImageField('картинка')
    min_storage_time = models.PositiveIntegerField('минимальное время хранения, сут.')
    max_storage_time = models.PositiveIntegerField('максимальное время хранения, сут.')
    storage_cost = models.DecimalField(
        'стоимость за минимальное время хранения',
        max_digits=5,
        decimal_places=2
    )

    objects = DisplayCostQuerySet.as_manager()

    def __str__(self):
        return self.name


class Box(models.Model):
    storage = models.ForeignKey(
        Storage,
        on_delete=models.CASCADE,
        related_name='boxes'
    )
    size = models.IntegerField(
        'размер бокса в квадратных метрах',
        validators=[MinValueValidator(1), MaxValueValidator(20),]
    )
    month_rent_price = models.IntegerField(
        'стоимость аренды на месяц',
        blank=True
    )
    things = models.ManyToManyField(
        Thing,
        blank=True,
        related_name='assosiated_boxes'
    )

    def count_month_rent_price(self):
        first_meter_price = self.storage.first_square_meter_price
        rest_meters_price = self.storage.rest_square_meters_price

        total_price = first_meter_price + (self.size - 1) * rest_meters_price

        return total_price

    def save(self, *args, **kwargs):
        self.month_rent_price = self.count_month_rent_price()

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Бокс №{self.id}'


class BoxOrder(models.Model):
    box = models.ForeignKey(
        Box,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    box_rent_term = models.IntegerField(
        'срок аренды бокса',
        validators=[MinValueValidator(1), MaxValueValidator(12)],
    )
    tenant = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='box_orders'
    )

    def __str__(self):
        return f'{self.box} на {self.box_rent_term}'


class SeasonalKeepingOrder(models.Model):
    things_names = models.CharField(
        'названия вещей',
        max_length=200
    )
    number_of_things = models.PositiveIntegerField(
        'кол-во единиц вещей',
        default=1
    )
    tenant = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='seasonal_keeping_orders'
    )
