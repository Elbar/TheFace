# coding=utf-8
from django import forms

SEX_CHOICES = (
    ('Male', 'Мужчина'),
    ('Female', 'Женщина')
)

TOWN_CHOICES = (
    ('Bishkek', 'Бишкек'),
    ('Osh', 'Ош'),
    ('Karakol', 'Каракол'),
    ('Djalal-Abad', 'Джалал Абад'),
    ('Cholpon-Ata', 'Чолпон-Ата'),
    ('Talas', 'Талас'),
    ('Batken', 'Баткен'),
    ('Karakol', 'Каракол'),
    ('Balykchy', 'Балыкчы'),
)

LANGUAGE_CHOICES = (
    ('Russian', 'Русский'),
    ('Enlish', 'Английский'),
    ('Deutch', 'Немецкий'),
    ('France', 'Французский'),
)


class FilterForm(forms.Form):
    sex = forms.ChoiceField(choices=SEX_CHOICES, required=False)
    minAge = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'от'}), required=False)
    maxAge = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'до'}), required=False)
    town = forms.ChoiceField(choices=TOWN_CHOICES, required=False)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=False)


class ActorForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
    surname = forms.CharField(max_length=255, required=False)
    birthday = forms.DateField()

    sex = forms.ChoiceField(choices=SEX_CHOICES, required=False)
    town = forms.ChoiceField(choices=TOWN_CHOICES, required=False)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=False)
