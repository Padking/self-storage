from django import forms

from .models import Storage


class NumberThingsForm(forms.Form):
    NUMBER_OF_THINGS_CHOICES = [
        ('1', 'Одна'),
        ('2', 'Две'),
        ('3', 'Три'),
    ]

    number_of_things = forms.ChoiceField(label='Количество единиц хранения',
                                         choices=NUMBER_OF_THINGS_CHOICES,
                                         widget=forms.RadioSelect)


class StorageAddressForm(forms.Form):
    ADDRESSES_CHOICES = [
        # (place.address, place.address) for place in Storage.objects.all()
    ]

    address = forms.ChoiceField(label='Адрес склада',
                                choices=ADDRESSES_CHOICES,
                                widget=forms.RadioSelect)
