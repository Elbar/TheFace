# coding=utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import smart_unicode

from actors.helper import transform

SEX = (('Мужской', 'Male'),
       ('Женский', 'Female'),
       )

READY_TO_GO = (
    ('Да', 'Yes'),
    ('Нет', 'No'),
)

READY_TO_MASS = (
    ('Да', 'Yes'),
    ('Нет', 'No'),
)

LANGUAGE_CHOICES = (
    ('Russian', 'Русский'),
    ('Enlish', 'Английский'),
    ('Deutch', 'Немецкий'),
    ('France', 'Французский'),
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

STATUS = (
    ('VIP', 'VIP'),
    ('BASIC', 'BASIC')
)

BODY = (
    ('худое', 'худое'),
    ('обычное', 'обычное'),
    ('плотное', 'плотное'),
)

CATEGORY_MOVIEMAKER = (
    ('Профессионал', 'Профессионал'),
    ('Любитель', 'Любитель'),
    ('Новичок', 'Новичок'),
)

NEWS_CATEGORY = (
    ('Советы', 'Советы'),
    ('Новости', 'Новости'),
    ('Кастинги', 'Кастинги'),
)

LOCATION_CATEGORY = (
    ('Priroda', 'Priroda'),
    ('Interyer', 'Interyer'),
)

PATH_ACTORS = 'actors/images'
PATH_MOVIEMAKER = 'moviemaker/images'
PATH_STUDIO = 'studio/images'
PATH_NEWS = 'news/images'
PATH_LOCATION = 'locations/images'


class Actor(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление Актеров'
        verbose_name = 'Добавление актеров'

    name = models.CharField(max_length=255, verbose_name='Имя Актера')
    surname = models.CharField(max_length=255, verbose_name='Фамилия Актера')
    age = models.IntegerField(verbose_name='Возраст')

    height = models.CharField(max_length=255, verbose_name='Рост')
    weight = models.CharField(max_length=255, verbose_name='Вес')

    identify = models.CharField(max_length=255, verbose_name='Идентификатор')
    phone_number = models.CharField(max_length=255, verbose_name='Номер Телефона')
    type_of_actor = models.CharField(max_length=255)
    staj = models.CharField(max_length=255, choices=READY_TO_GO, verbose_name='Опыт съемок')
    category = models.CharField(max_length=255, verbose_name='Категория')
    color = models.CharField(max_length=255, verbose_name='Цвет Волос')
    talent = models.CharField(max_length=255, verbose_name='Навыки')

    link = models.CharField(max_length=255, verbose_name='ссылка на youtube')
    sex = models.CharField(choices=SEX, verbose_name='Пол', max_length=255)
    town = models.CharField(choices=TOWN_CHOICES, max_length=255, null=True)
    language = models.CharField(verbose_name='Знание языков', max_length=255)

    ready_to_go = models.CharField(choices=READY_TO_GO, max_length=255, verbose_name='Готовность к выезду')
    ready_to_mass = models.CharField(choices=READY_TO_MASS, max_length=255, verbose_name='Готовность к массовым ролям')
    image = models.FileField(upload_to=transform(PATH_ACTORS), verbose_name='Фотография актера на главную страницу', blank=True)
    index_image = models.FileField(upload_to=transform(PATH_ACTORS), verbose_name='Главная фотография актера')
    status = models.CharField(choices=STATUS, max_length=255, verbose_name='Статус Актера')

    other_talent = models.CharField(max_length=255, verbose_name='Другие Навыки', blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)

    def get_absolute_url(self):
        return "/actors/%i/" % self.id


class ActorsImage(models.Model):
    class Meta:
        verbose_name_plural = 'Фотографии Актеров'
        verbose_name = 'Фотографии Актеров'

    actor = models.ForeignKey(Actor, verbose_name='Выберите актера')
    image = models.ImageField(upload_to=transform(PATH_ACTORS), verbose_name='Фотография Актера')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.actor.name)


class MovieMaker(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление кинематографистов'
        verbose_name = 'Добавление кинематографистов'

    firstname = models.CharField(max_length=255, verbose_name='Имя')
    lastname = models.CharField(max_length=255, verbose_name='Фамилия')
    surname = models.CharField(max_length=255, verbose_name='Отчество')
    job_type = models.CharField(max_length=255, verbose_name='Специализация')
    education = models.CharField(max_length=255, verbose_name='Образование')
    category = models.CharField(max_length=255, choices=CATEGORY_MOVIEMAKER)
    image = models.FileField(upload_to=transform(PATH_MOVIEMAKER), verbose_name='Фотография')
    languages = models.CharField(max_length=255, verbose_name='Знание Языков')
    ready_to_go = models.CharField(max_length=255, choices=READY_TO_GO)
    experience = models.IntegerField(default=0)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.firstname + ' ' + self.lastname)

    def get_absolute_url(self):
        return "/moviemakers/%i/" % self.id


class Studio(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление Студии'
        verbose_name = 'Добавление Студии'

    name = models.CharField(max_length=255, verbose_name='Название')
    about = models.TextField(verbose_name='Об Агенстве')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    apparat = models.CharField(max_length=255, verbose_name='Аппаратура')
    square = models.CharField(max_length=255, verbose_name='Площадь Студии')
    site = models.CharField(max_length=255, verbose_name='Сайт')
    number = models.CharField(max_length=255, verbose_name='Номер')
    email = models.EmailField(verbose_name='Почта')
    image = models.FileField(upload_to=transform(PATH_STUDIO), verbose_name='Фотография')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)

    def get_absolute_url(self):
        return "/studio/%i" % self.id


class ProjectStudio(models.Model):
    class Meta:
        verbose_name = 'Добавить Проект Studio'
        verbose_name_plural = 'Добавление Проекта Studio'

    title = models.CharField(max_length=255, verbose_name='Название проекта')
    project = models.ForeignKey(Studio, verbose_name='Выберите studio')
    image = models.ImageField(upload_to=transform(PATH_MOVIEMAKER), verbose_name='Загрузить Картинку')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class StudioImage(models.Model):
    class Meta:
        verbose_name_plural = 'Фотосессии Студий'
        verbose_name = 'Фотосессии Студий'

    studio = models.ForeignKey(Studio, verbose_name='Выберите Студию')
    image = models.FileField(upload_to=transform(PATH_STUDIO), verbose_name='Фотографии')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class StudioLink(models.Model):
    class Meta:
        verbose_name_plural = 'Video Студий'
        verbose_name = 'Video Студий'

    studio = models.ForeignKey(Studio, verbose_name='Выберите Студию')
    link = models.CharField(max_length=255, verbose_name='Вставьте линк')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class News(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление новостей'
        verbose_name = 'Добавление новостей'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.CharField(max_length=1000, verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст поста')
    category = models.CharField(choices=NEWS_CATEGORY, max_length=255)
    image = models.ImageField(upload_to=transform(PATH_NEWS), verbose_name='картинка')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)

    def get_absolute_url(self):
        return "/news/%i/" % self.id


class Location(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление Локаций'
        verbose_name = 'Добавление Локаций'

    name = models.CharField(max_length=255, verbose_name='Название')
    region = models.CharField(max_length=255, verbose_name='Регион')
    category = models.CharField(max_length=255, choices=LOCATION_CATEGORY)
    image = models.ImageField(upload_to=transform(PATH_LOCATION), verbose_name='Картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)

    def get_absolute_url(self):
        return "/locations/%id" % self.id


class LocationImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки локаций'
        verbose_name = 'Картинки локаций'

    location = models.ForeignKey(Location, verbose_name='выберите Название Локации')
    image = models.ImageField(upload_to=transform(PATH_LOCATION), verbose_name='картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.location.name)


class Project(models.Model):
    class Meta:
        verbose_name = 'Добавить Проект'
        verbose_name_plural = 'Добавление Проекта'

    title = models.CharField(max_length=255, verbose_name='Название проекта')
    project = models.ForeignKey(MovieMaker, verbose_name='Выберите кинематографиста')
    image = models.ImageField(upload_to=transform(PATH_MOVIEMAKER), verbose_name='Загрузить Картинку')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class FormFile(models.Model):
    class Meta:
        verbose_name = 'Картинки с формы'
        verbose_name_plural = 'Картинки с формы'

    name = models.CharField(max_length=255)
    image = models.FileField(upload_to=transform(PATH_MOVIEMAKER), verbose_name='Images')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)
