from dateutil.relativedelta import relativedelta

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .managers import DisplayCostQuerySet

from phonenumber_field.modelfields import PhoneNumberField


class Storage(models.Model):
    address = models.TextField(
        'адрес',
        help_text='ул. Манчестерская, д. 7, кв. 1'
    )
    longitude = models.FloatField('долгота')
    latitude = models.FloatField('широта')
    phone = PhoneNumberField("телефон склада", blank=True, db_index=True)
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

    def count_min_box_price(self):
        min_box_price = self.boxes.aggregate(models.Min('month_rent_price'))['month_rent_price__min']

        return min_box_price

    def count_squares_meters_count(self):
        squares_meters_count = self.boxes.aggregate(models.Sum('size'))['size__sum']

        return squares_meters_count

    def count_free_squares_meters_count(self):
        rented_squares_meters_count = self.boxes.filter(is_rented=True).aggregate(models.Sum('size'))['size__sum']
        free_squares_meters_count = self.count_squares_meters_count() - rented_squares_meters_count

        return free_squares_meters_count

    def __str__(self):
        return f'{self.alias}'


class Box(models.Model):
    storage = models.ForeignKey(
        Storage,
        on_delete=models.CASCADE,
        verbose_name='склад',
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
    is_rented = models.BooleanField('Бокс арендован', blank=True, default=False)

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
        verbose_name = 'бокс',
        related_name='orders'
    )
    rent_term = models.IntegerField(
        'срок аренды бокса в месяцах',
        validators=[MinValueValidator(1), MaxValueValidator(12)],
    )
    rent_start = models.DateField('начало срока аренды бокса', auto_now_add=True)
    rent_end = models.DateField('конец срока аренды бокса', null=True)
    tenant = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='арендатор',
        related_name='box_orders'
    )

    def save(self, *args, **kwargs):
        self.box.is_rented = True
        self.box.save()

        super().save(*args, **kwargs)

        self.rent_end = self.rent_start + relativedelta(months=self.rent_term)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.box} на {self.rent_term} месяцев'


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
