from django.shortcuts import render

from .models import Actor
from actors.form import FilterForm


def index_view(request):
    actors = Actor.objects.all()[0:5]
    actors1 = Actor.objects.all()[5:11]
    actors2 = Actor.objects.all()[11:16]
    context = {"actors": actors, "actors1": actors1, "actors2": actors2}
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
            print sex
            actors = Actor.objects.filter(sex=sex)
        else:
            print form.errors
    else:
        actors = Actor.objects.all()

    context = {"actors": actors, "form": filter_form}
    return render(request, template, context)
