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
    ('France', 'Французский'),
    ('France', 'Французский'),
    ('France', 'Французский'),
    ('France', 'Французский'),
    ('France', 'Французский'),
)

TYPES = (
    ('brunet', 'Brunet'),
    ('waten', 'waten'),
    ('some', 'some'),
    ('type', 'type'),
)

BODY = (
    ('small', 'маленькое'),
    ('normal', 'среднее'),
    ('big', 'большое'),
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
    birthday = forms.CharField(required=False)
    body = forms.ChoiceField(required=False, choices=BODY)
    height = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)
    number = forms.CharField(required=False)

    types = forms.ChoiceField(required=False, choices=TYPES)
    sex = forms.ChoiceField(choices=SEX_CHOICES, required=False)
    town = forms.ChoiceField(choices=TOWN_CHOICES, required=False)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=False)

    other = forms.CharField(widget=forms.Textarea, required=False)


class MovieMakerForm(forms.Form):
    minAge = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'от'}), required=False)
    maxAge = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'до'}), required=False)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=False)


class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
    email = forms.EmailField(required=False)
    info = forms.CharField(max_length=255, required=False, widget=forms.Textarea)
