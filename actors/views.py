from django.shortcuts import render

from .models import Actor


def index_view(request):
    actors = Actor.objects.all()[0:5]
    actors1 = Actor.objects.all()[5:11]
    actors2 = Actor.objects.all()[11:16]
    context = {"actors": actors, "actors1": actors1, "actors2": actors2}
    template = 'main/index.html'

    return render(request, template, context)


def actor_view(request):
    actors = Actor.objects.all()
    context = {"actors": actors}
    template = 'actors.html'

    return render(request, template, context)
