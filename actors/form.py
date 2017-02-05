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

TYPES = (
    ('aziat', 'Азиатский'),
    ('evropeec', 'Европейский'),
    ('eastern', 'Восточный'),
)

COLOR = (
    ('brunet', 'Брюнет'),
    ('blondın', 'Блондин'),
    ('ryjıy', 'Рыжий'),
)

BODY = (
    ('small', 'худое'),
    ('normal', 'обычное'),
    ('big', 'плотное'),
)

READY_TO_GO = (
    ('Yes', 'Да'),
    ('No', 'Нет'),
)

CATEGORY_MOVIEMAKER = (
    ('professional', 'Профессионал'),
    ('normal', 'Любитель'),
    ('newer', 'Новичок'),
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
    category = forms.ChoiceField(choices=CATEGORY_MOVIEMAKER, required=False)
    types = forms.ChoiceField(required=False, choices=TYPES)
    hair_color = forms.ChoiceField(required=False, choices=COLOR)
    sex = forms.ChoiceField(choices=SEX_CHOICES, required=False)
    town = forms.ChoiceField(choices=TOWN_CHOICES, required=False)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=False)

    other = forms.CharField(widget=forms.Textarea, required=False)


class MovieMakerForm(forms.Form):
    minAge = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'от'}), required=False)
    maxAge = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'до'}), required=False)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=False)
    ready = forms.ChoiceField(choices=READY_TO_GO, required=False)
    category = forms.ChoiceField(choices=CATEGORY_MOVIEMAKER, required=False)


class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
    email = forms.EmailField(required=False)
    info = forms.CharField(max_length=255, required=False, widget=forms.Textarea)
