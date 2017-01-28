from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt

from .models import *
from actors.form import FilterForm, ActorForm


def index_view(request):
    actors = Actor.objects.all()[0:5]
    actors1 = Actor.objects.all()[5:11]
    actors2 = Actor.objects.all()[11:16]
    context = {"actors": actors, "actors1": actors1, "actors2": actors2, 'location': 'index'}
    template = 'main/index.html'

    return render(request, template, context)


def actor_view(request):
    form = FilterForm(request.POST)
    filter_form = FilterForm
    template = 'actors.html'
    actors = None
    if request.method == 'POST':
        print request.method
        if form.is_valid():
            sex = form.cleaned_data['sex']
            minAge = form.cleaned_data['minAge']
            maxAge = form.cleaned_data['maxAge']
            town = form.cleaned_data['town']
            language = form.cleaned_data['language']

            actors = Actor.objects.filter(sex=sex, town=town, language=language, age__range=(minAge, maxAge))
        else:
            print form.errors
    else:
        actors = Actor.objects.all()

    context = {"actors": actors, "form": filter_form, 'location': 'actors'}
    return render(request, template, context)


@csrf_exempt
def ajax_actor_view(request, id):
    actor = Actor.objects.get(id=id)
    actor_images = ActorsImage.objects.filter(actor=actor)

    response = render_to_response('partial/_actors_popup.html', dict(actor=actor, actor_images=actor_images))
    return response


@csrf_exempt
def become_an_actor_view(request):
    form = ActorForm(request.POST)
    actor_form = ActorForm

    if request.method == 'POST':
        print request.method
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            birthday = form.cleaned_data['birthday']
            body = form.cleaned_data['body']
            height = form.cleaned_data['height']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']

            types = form.cleaned_data['types']
            sex = form.cleaned_data['sex']
            town = form.cleaned_data['town']
            language = form.cleaned_data['language']

            other = form.cleaned_data['other']

            print name, surname, birthday, body, height, email, number, types, sex, town, language, other

        else:
            print form.errors

    context = {"form": actor_form}
    template = 'become_an_actor.html'

    return render(request, template, context)


def moviemaker_view(request):
    moviemaker = MovieMaker.objects.all()
    context = {"moviemaker": moviemaker}
    template = 'moviemakers.html'

    return render(request, template, context)


def news_view(request):
    big_news = News.objects.get(news_type='Big')
    small_news = News.objects.get(news_type='Small')
    normal_news = News.objects.get(news_type='Normal')
    context = {"big_news": big_news, "small_news": small_news, "normal_news": normal_news}
    template = 'news.html'

    return render(request, template, context)


def location_view(request):
    locations = Location.objects.all()
    context = {"locations": locations}
    template = 'locations.html'

    return render(request, template, context)


def studio_view(request):
    studio = Studio.objects.all()
    context = {"studio": studio}
    template = 'studio.html'

    return render(request, template, context)


def about_view(request):
    context = {}
    template = 'about_us.html'

    return render(request, template, context)
