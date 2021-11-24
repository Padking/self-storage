from django import forms


CHOICES = [
    ('1', 'Одна'),
    ('2', 'Две'),
    ('3', 'Три'),
]


class NumberThingsForm(forms.Form):
    number_of_things = forms.ChoiceField(label='Количество единиц хранения',
                                         choices=CHOICES,
                                         widget=forms.RadioSelect)
