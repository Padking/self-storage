from django.db import models

from core.managers import DisplayCostQuerySet


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
