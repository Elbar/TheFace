from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Actor
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
    context = {}
    template = 'moviemakers.html'

    return render(request, template, context)


def news_view(request):
    context = {}
    template = 'news.html'

    return render(request, template, context)
