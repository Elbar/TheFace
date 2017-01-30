# coding=utf-8
from django.core.mail import EmailMessage
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.template import Context
from django.template import Template
from django.views.decorators.csrf import csrf_exempt

from TheFace.settings import BASE_DIR
from .models import *
from actors.form import FilterForm, ActorForm


def index_view(request):
    actors = Actor.objects.all()[0:5]
    actors1 = Actor.objects.all()[5:11]
    actors2 = Actor.objects.all()[11:16]
    context = {"actors": actors, "actors1": actors1, "actors2": actors2, 'location': 'index'}
    template = 'main/index.html'

    return render(request, template, context)


@csrf_exempt
def actor_view(request):
    filter_form = FilterForm
    template = 'actors.html'
    actors = Actor.objects.all()

    context = {"actors": actors, "form": filter_form, 'location': 'actors'}
    return render(request, template, context)


@csrf_exempt
def filter_actor(request):
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

            actors = Actor.objects.filter(sex=sex, town=town)
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
def ajax_moviemakers_view(request, id):
    moviemaker = MovieMaker.objects.get(id=id)
    response = render_to_response('partial/_moviemakers_popup.html', dict(moviemaker=moviemaker))

    return response


@csrf_exempt
def send_mail(request):
    form = ActorForm(request.POST)

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

            import os
            f = open(os.path.join(BASE_DIR, "templates/mail.html"))

            content = f.read()
            f.close()
            context = Context(
                dict(name=name, surname=surname, birthday=birthday, body=body, height=height, email=email,
                     number=number, types=types, sex=sex, town=town, language=language, other=other))
            template = Template(content)
            mail = EmailMessage('Заявка на Кастинг', template.render(context), to=['thefacekg@gmail.com'])
            mail.content_subtype = 'html'
            mail.send()

            return JsonResponse(dict(result='Message send'))


@csrf_exempt
def become_an_actor_view(request):
    actor_form = ActorForm

    context = {"form": actor_form}
    template = 'become_an_actor.html'

    return render(request, template, context)


def moviemaker_view(request):
    moviemaker = MovieMaker.objects.all()
    context = {"moviemaker": moviemaker}
    template = 'moviemakers.html'

    return render(request, template, context)


def news_view(request):
    news = News.objects.all()
    context = {"news": news}
    template = 'news.html'

    return render(request, template, context)


def singleNews(request, id):
    try:
        news = News.objects.get(id=id)

        context = {"news": news}
        template = 'single_post.html'

        return render(request, template, context)

    except News.DoesNotExist:
        raise Http404


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
