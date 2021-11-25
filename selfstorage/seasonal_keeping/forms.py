from django import forms

from core.models import Place


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
        (place.address, place.address) for place in Place.objects.all()
    ]

    address = forms.ChoiceField(label='Адрес склада',
                                choices=ADDRESSES_CHOICES,
                                widget=forms.RadioSelect)
