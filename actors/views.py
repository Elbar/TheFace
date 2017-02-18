# coding=utf-8
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import Context
from django.template import Template
from django.views.decorators.csrf import csrf_exempt
from TheFace.settings import BASE_DIR
from .models import *
from actors.form import *


def index_view(request):
    actors = Actor.objects.all()[0:5]
    actors1 = Actor.objects.all()[5:11]
    actors2 = Actor.objects.all()[11:16]
    form = ApplicationForm
    context = {"actors": actors, "actors1": actors1, "actors2": actors2, 'location': 'index', "form": form}
    template = 'main/index.html'

    return render(request, template, context)


@csrf_exempt
def send_application(request):
    form = ApplicationForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            number = request.POST.get('number')
            info = form.cleaned_data['info']

            import os
            f = open(os.path.join(BASE_DIR, "templates/application.html"))

            content = f.read()
            f.close()
            context = Context(
                dict(name=name, number=number, info=info))
            template = Template(content)
            mail = EmailMessage('Заявка на Подборку', template.render(context), to=['thefacekg@gmail.com'])
            mail.content_subtype = 'html'
            mail.send()

            actors = Actor.objects.all()[0:5]
            actors1 = Actor.objects.all()[5:11]
            actors2 = Actor.objects.all()[11:16]

            context = {"actors": actors, "actors1": actors1, "actors2": actors2, 'location': 'index', "form": form,
                       "message": "success"}
            template = 'main/index.html'

            return render(request, template, context)

        else:

            actors = Actor.objects.all()[0:5]
            actors1 = Actor.objects.all()[5:11]
            actors2 = Actor.objects.all()[11:16]

            context = {"actors": actors, "actors1": actors1, "actors2": actors2, 'location': 'index', "form": form,
                       "message": "error"}
            template = 'main/index.html'

            return render(request, template, context)


@csrf_exempt
def actor_view(request):
    filter_form = FilterForm
    template = 'actors.html'
    actors_list = Actor.objects.all()
    paginator = Paginator(actors_list, 100)

    page = request.GET.get('page')

    try:
        actors = paginator.page(page)

    except PageNotAnInteger:
        actors = paginator.page(1)

    except EmptyPage:
        actors = paginator.page(paginator.num_pages)

    context = {"actors": actors, "form": filter_form, 'location': 'actor'}
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

            actors_list = Actor.objects.filter(sex=sex, town=town)
            paginator = Paginator(actors_list, 100)

            page = request.GET.get('page')

            try:
                actors = paginator.page(page)

            except PageNotAnInteger:
                actors = paginator.page(1)

            except EmptyPage:
                actors = paginator.page(paginator.num_pages)
        else:
            print form.errors
    else:
        actors_list = Actor.objects.all()
        paginator = Paginator(actors_list, 100)

        page = request.GET.get('page')

        try:
            actors = paginator.page(page)

        except PageNotAnInteger:
            actors = paginator.page(1)

        except EmptyPage:
            actors = paginator.page(paginator.num_pages)

    context = {"actors": actors, "form": filter_form, 'location': 'actor'}
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
def ajax_location_view(request, id):
    location = Location.objects.get(id=id)
    location_images = LocationImage.objects.filter(location=location)
    response = render_to_response('partial/_location_popup.html',
                                  dict(location=location, location_images=location_images))

    return response


@csrf_exempt
def send_mail(request):
    form = ActorForm(request.POST)

    russian = None
    english = None
    deutch = None
    france = None
    spanish = None
    kazakh = None
    korean = None
    japan = None
    chinese = None
    dance = None
    ballet = None
    vokal = None
    wrestling = None
    swimming = None
    box = None
    judo = None
    football = None
    gymnastic = None
    music = None
    staj = None

    english_check = request.POST.get('english')

    if english_check != None:
        english = "English"

    russian_check = request.POST.get('russian')

    if russian_check != None:
        russian = "Russian"

    deutch_check = request.POST.get('deutch')

    if deutch_check != None:
        deutch = "Deutch"

    france_check = request.POST.get('france')

    if france_check != None:
        france = "France"

    spanich_check = request.POST.get('spanish')

    if spanich_check != None:
        spanish = "Spanish"

    kazakh_check = request.POST.get('kazakh')

    if kazakh_check != None:
        kazakh = "Kazakh"

    korean_check = request.POST.get('korean')

    if korean_check != None:
        korean = "Korean"

    japan_check = request.POST.get('japan')

    if japan_check != None:
        japan = "Japan"

    chinese_check = request.POST.get('chinese')

    if chinese_check != None:
        chinese = "Chinese"

    dance_check = request.POST.get('dance')

    if dance_check != None:
        dance = "Dance"

    ballet_check = request.POST.get('ballet')

    if ballet_check != None:
        ballet = "Ballet"

    vokal_check = request.POST.get('vokal')

    if vokal_check != None:
        vokal = "Vokal"

    wrestling_check = request.POST.get('wrestling')

    if wrestling_check != None:
        wrestling = "Wrestling"

    judo_check = request.POST.get('judo')

    if judo_check != None:
        judo = "Judo"

    football_check = request.POST.get('football')

    if football_check != None:
        football = "Football"

    gymnastic_check = request.POST.get('gymnastic')

    if gymnastic_check != None:
        gymnastic = "Gymnastic"

    music_check = request.POST.get('music')

    if music_check != None:
        music = "Music"

    staj_check = request.POST.get('staj')

    if staj_check != None:
        staj = "Staj"

    vokal_check = request.POST.get('vokal')

    if vokal_check != None:
        vokal = "Vokal"

    if request.method == 'POST':

        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            birthday = form.cleaned_data['birthday']
            body = form.cleaned_data['body']
            height = form.cleaned_data['height']
            email = form.cleaned_data['email']
            number = request.POST.get('number')

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
                     number=number, types=types, sex=sex, town=town, language=language, other=other,
                     english=english, russian=russian, deutch=deutch, france=france, spanish=spanish, kazakh=kazakh,
                     korean=korean, japan=japan, chinese=chinese, dance=dance, ballet=ballet, vokal=vokal,
                     wrestling=wrestling, swimming=swimming, box=box, judo=judo, football=football, gymnastic=gymnastic,
                     music=music, staj=staj
                     ))
            template = Template(content)
            mail = EmailMessage('Заявка на Кастинг', template.render(context), to=['thefacekg@gmail.com'])
            mail.content_subtype = 'html'
            mail.send()

            actor_form = ActorForm

            context1 = {"form": actor_form, "location": "become_an_actor", "message": "success"}
            template1 = 'become_an_actor.html'

            return render(request, template1, context1)

        else:
            actor_form = ActorForm

            context1 = {"form": actor_form, "location": "become_an_actor", "message": "error"}
            template1 = 'become_an_actor.html'

            return render(request, template1, context1)


@csrf_exempt
def become_an_actor_view(request):
    actor_form = ActorForm

    context = {"form": actor_form, "location": "become_an_actor"}
    template = 'become_an_actor.html'

    return render(request, template, context)


def moviemaker_view(request):
    form_file = FormFile
    form = MovieMakerForm
    moviemaker_list = MovieMaker.objects.all()

    paginator = Paginator(moviemaker_list, 10)

    page = request.GET.get('page')

    try:
        moviemaker = paginator.page(page)

    except PageNotAnInteger:

        moviemaker = paginator.page(1)

    except EmptyPage:

        moviemaker = paginator.page(paginator.num_pages)

    context = {"moviemaker": moviemaker, 'location': 'moviemaker', "form": form, "form_file": form_file}
    template = 'moviemakers.html'

    return render(request, template, context)


@csrf_exempt
def moviemaker_result_view(request):
    form = MovieMakerForm(request.POST)

    filter_form = MovieMakerForm
    template = 'moviemakers.html'
    moviemakers = None
    if request.method == 'POST':
        print request.method
        if form.is_valid():
            ready = form.cleaned_data['ready']
            minAge = form.cleaned_data['minAge']
            maxAge = form.cleaned_data['maxAge']
            category = form.cleaned_data['category']
            language = form.cleaned_data['language']

            moviemakers = MovieMaker.objects.filter(ready_to_go=ready, category=category, languages=language)
        else:
            print form.errors
    else:
        moviemakers = MovieMaker.objects.all()

    context = {"moviemaker": moviemakers, "form": filter_form, 'location': 'moviemaker'}
    return render(request, template, context)


def news_view(request):
    news_list = News.objects.all()

    paginator = Paginator(news_list, 10)

    page = request.GET.get('page')

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)

    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {"news": news, 'location': 'news'}
    template = 'news.html'

    return render(request, template, context)


def singleNews(request, id):
    try:
        news = News.objects.get(id=id)

        context = {"news": news, 'location': 'news'}
        template = 'single_post.html'

        return render(request, template, context)

    except News.DoesNotExist:
        raise Http404


def location_view(request):
    locations_list = Location.objects.all()

    paginator = Paginator(locations_list, 10)

    page = request.GET.get('page')

    try:
        locations = paginator.page(page)

    except PageNotAnInteger:

        locations = paginator.page(1)

    except EmptyPage:

        locations = paginator.page(paginator.num_pages)

    context = {"locations": locations, "location": "location"}
    template = 'locations.html'

    return render(request, template, context)


def studio_view(request):
    studio_list = Studio.objects.all()

    paginator = Paginator(studio_list, 10)

    page = request.GET.get('page')

    try:
        studio = paginator.page(page)

    except PageNotAnInteger:

        studio = paginator.page(1)

    except EmptyPage:

        studio = paginator.page(paginator.num_pages)

    context = {"studio": studio, 'location': 'studio'}
    template = 'studio.html'

    return render(request, template, context)


def single_studio(request, id):
    studio = Studio.objects.get(id=id)
    studio_image = StudioImage.objects.filter(studio=studio)
    studio_link = StudioLink.objects.filter(studio=studio)
    context = {"studio": studio, 'location': 'studio', "images": studio_image, "links": studio_link}
    template = 'studio_single.html'

    return render(request, template, context)


def about_view(request):
    context = {'location': 'about'}
    template = 'about_us.html'

    return render(request, template, context)


@csrf_exempt
def get_studio(request):
    name = request.POST.get('studio')
    town = request.POST.get('select-name')
    from_area = request.POST.get('from_area')
    to_area = request.POST.get('to_area')
    contacts_name = request.POST.get('name')
    surname = request.POST.get('surname')
    fotoset = request.POST.get('fotoset')
    ad_video = request.POST.get('ad_video')
    original_music = request.POST.get('original_music')
    music_clip = request.POST.get('music_clip')
    record_song = request.POST.get('record_song')
    interyer = request.POST.get('interyer')
    film = request.POST.get('film')
    social_clip = request.POST.get('social_clip')
    aranjirovka = request.POST.get('aranjirovka')
    audio_ad = request.POST.get('audio_ad')
    ozvuchka = request.POST.get('ozvuchka')
    info = request.POST.get('info')
    info_apparatura = request.POST.get('info_apparatura')
    project_name = request.POST.get('project_name')
    video_link = request.POST.get('video_link')
    address = request.POST.get('address')
    number = request.POST.get('number')
    site_link = request.POST.get('site_link')
    email = request.POST.get('email')
    contacts_phone = request.POST.get('contacts_phone')
    contacts_email = request.POST.get('contacts_email')

    import os
    f = open(os.path.join(BASE_DIR, "templates/studio_application.html"))

    content = f.read()
    f.close()
    context = Context(
        dict(name=name, town=town, from_area=from_area, to_area=to_area, contacts_name=contacts_name,
             surname=surname,
             fotoset=fotoset, ad_video=ad_video, original_music=original_music, music_clip=music_clip,
             record_song=record_song, interyer=interyer, film=film, social_clip=social_clip,
             aranjirovka=aranjirovka,
             audio_ad=audio_ad, ozvuchka=ozvuchka, info=info, info_apparatura=info_apparatura,
             project_name=project_name, video_link=video_link, address=address, number=number, site_link=site_link,
             email=email, contacts_phone=contacts_phone, contacts_email=contacts_email
             ))
    template = Template(content)
    mail = EmailMessage('Заявка на Studio', template.render(context), to=['thefacekg@gmail.com'])
    mail.content_subtype = 'html'
    mail.send()

    studio_list = Studio.objects.all()

    paginator = Paginator(studio_list, 10)

    page = request.GET.get('page')

    try:
        studio = paginator.page(page)

    except PageNotAnInteger:

        studio = paginator.page(1)

    except EmptyPage:

        studio = paginator.page(paginator.num_pages)

    context1 = {"studio": studio, 'location': 'studio', "message": "success"}
    template1 = 'studio.html'

    return render(request, template1, context1)


@csrf_exempt
def result_studio(request):
    studio_list = Studio.objects.all()

    paginator = Paginator(studio_list, 10)

    page = request.GET.get('page')

    try:
        studio = paginator.page(page)

    except PageNotAnInteger:

        studio = paginator.page(1)

    except EmptyPage:

        studio = paginator.page(paginator.num_pages)

    context = {"studio": studio, 'location': 'studio'}
    template = 'studio.html'

    return render(request, template, context)


@csrf_exempt
def location_application(request):
    name_location = request.POST.get('name_location')
    location_type = request.POST.get('location_type')
    location_state = request.POST.get('location_state')
    information = request.POST.get('information')
    photo_comments = request.POST.get('photo')
    contacts_name = request.POST.get('contacts_name')
    surname = request.POST.get('surname')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')

    if request.POST:
        file_link = request.FILES['file_link']

        FormFile.objects.create(name=contacts_name, image=file_link)

    import os
    f = open(os.path.join(BASE_DIR, "templates/location_application.html"))

    content = f.read()
    f.close()
    context = Context(dict(
        name_location=name_location, location_type=location_type, location_state=location_state,
        information=information, photo_comments=photo_comments, contacts_name=contacts_name, surname=surname,
        phone_number=phone_number, email=email
    ))
    template = Template(content)
    mail = EmailMessage('Заявка на Location', template.render(context), to=['thefacekg@gmail.com'])
    mail.content_subtype = 'html'
    mail.send()

    locations_list = Location.objects.all()

    paginator = Paginator(locations_list, 10)

    page = request.GET.get('page')

    try:
        locations = paginator.page(page)

    except PageNotAnInteger:

        locations = paginator.page(1)

    except EmptyPage:

        locations = paginator.page(paginator.num_pages)

    context1 = {"locations": locations, "location": "location", "message": "success"}
    template1 = 'locations.html'

    return render(request, template1, context1)


@csrf_exempt
def moviemakers_application(request):
    kyrgyz = None
    france = None
    korean = None
    russian = None
    deutche = None
    japan = None
    spanish = None
    english = None
    director = None
    operator = None
    scenarist = None
    hudojnik_costume = None
    compositor = None
    postanovshik = None
    assistent = None
    music_director = None
    line_producer = None
    main_producer = None
    second_director = None
    kaskader = None
    rekvizitor = None
    stilist = None
    osvetitel = None
    grimer = None
    montajer = None
    casting_director = None
    photographer = None
    uzbek = None
    turkish = None
    kazakh = None

    casting_director_check = request.POST.get('casting')

    if casting_director_check != None:
        casting_director = "Cating Director"

    montajer_check = request.POST.get('montajer')

    if montajer_check != None:
        montajer = "Montajer"

    grimer_check = request.POST.get('grimer')

    if grimer_check != None:
        grimer = "Grimer"

    stilist_check = request.POST.get('stilist')

    if stilist_check != None:
        stilist = "Stilist"

    rekvizitor_check = request.POST.get('rekvizitor')

    if rekvizitor_check != None:
        rekvizitor = "Rekvizitor"

    music_director_check = request.POST.get('recorder')

    if music_director_check != None:
        music_director = "Music Director"

    uzbek_check = request.POST.get('uzbek')

    if uzbek_check != None:
        uzbek = "Uzbek"

    photographer_check = request.POST.get('photographer')

    if photographer_check != None:
        photographer = "Photographer"

    scenarist_check = request.POST.get('scenarist')

    if scenarist_check != None:
        scenarist = "scenarist"

    hudojnik_costume_check = request.POST.get('hudojnik-costume')

    if hudojnik_costume_check != None:
        hudojnik_costume = "hudojnik_costume"

    compositor_check = request.POST.get('musician')

    if compositor_check != None:
        compositor = "Compositor"

    postanovshik_check = request.POST.get('art-director')

    if postanovshik_check != None:
        postanovshik = 'Hudojnik postanovshik'

    assistent_check = request.POST.get('assistent')

    if assistent_check != None:
        assistent = "Assistent"

    operator_check = request.POST.get('operator')

    if operator_check != None:
        operator = "Operator"

    line_producer_check = request.POST.get('producer-lineinyi')

    if line_producer_check != None:
        line_producer = 'line_producer'

    kaskader_check = request.POST.get('kaskader')

    if kaskader_check != None:
        kaskader = 'kaskader'

    main_producer_check = request.POST.get('producer-main')

    if main_producer_check != None:
        main_producer = 'main_producer'

    kyrgyz_check = request.POST.get('kyrgyz')

    if kyrgyz_check != None:
        kyrgyz = "Kyrgyz"

    france_check = request.POST.get('france')

    if france_check != None:
        france = "France"

    korean_check = request.POST.get('korean')

    if korean_check != None:
        korean = "Korean"

    russian_check = request.POST.get('russian')

    if russian_check != None:
        russian = "Russian"

    deutche_check = request.POST.get('deutche')

    if deutche_check != None:
        deutche = "Deutche"

    japan_check = request.POST.get('japan')

    if japan_check != None:
        japan = "Japan"

    spanish_check = request.POST.get('spanish')

    if spanish_check != None:
        spanish = "Spanish"

    english_check = request.POST.get('english')

    if english_check != None:
        english = "English"

    director_check = request.POST.get('director')

    if director_check != None:
        director = "Director"

    second_director_check = request.POST.get('second-director')

    if second_director_check != None:
        second_director = "Second Director"

    lighter_check = request.POST.get('lighter')

    if lighter_check != None:
        osvetitel = "Osvetitel"

    turkish_check = request.POST.get('turkish')

    if turkish_check != None:
        turkish = "Turkish"

    kazakh_check = request.POST.get('kazakh')

    if kazakh_check != None:
        kazakh = "Kazakh"

    name = request.POST.get('name')
    project = request.POST.get('project')
    surname = request.POST.get('surname')
    staj = request.POST.get('select-staj')
    education = request.POST.get('education')
    phone_number = request.POST.get('phone')
    email = request.POST.get('email')
    video_link = request.POST.get('video_link')

    if request.POST:
        file_link = request.FILES['file_link']
        FormFile.objects.create(name=name, image=file_link)

    import os
    f = open(os.path.join(BASE_DIR, "templates/moviemakers_application.html"))

    content = f.read()
    f.close()
    context = Context(
        dict(kyrgyz=kyrgyz, france=france, korean=korean, japan=japan, russian=russian, deutche=deutche,
             spanish=spanish, english=english, director=director, second_director=second_director, osvetitel=osvetitel,
             name=name, surname=surname, staj=staj, education=education, phone_number=phone_number, email=email,
             video_link=video_link, scenarist=scenarist, hudojnik_costume=hudojnik_costume, compositor=compositor,
             postanovshik=postanovshik, assistent=assistent, operator=operator, line_producer=line_producer,
             kaskader=kaskader, main_producer=main_producer, project=project, photographer=photographer, uzbek=uzbek,
             kazakh=kazakh, turkish=turkish, music_director=music_director, rekvizitor=rekvizitor, stilist=stilist,
             grimer=grimer, montajer=montajer, casting_director=casting_director
             )
    )
    template = Template(content)
    mail = EmailMessage('Заявка на Moviemaker', template.render(context), to=['thefacekg@gmail.com'])
    mail.content_subtype = 'html'
    mail.send()

    form_file = FormFile
    form = MovieMakerForm
    moviemaker_list = MovieMaker.objects.all()

    paginator = Paginator(moviemaker_list, 10)

    page = request.GET.get('page')

    try:
        moviemaker = paginator.page(page)

    except PageNotAnInteger:

        moviemaker = paginator.page(1)

    except EmptyPage:

        moviemaker = paginator.page(paginator.num_pages)

    context1 = {"moviemaker": moviemaker, 'location': 'moviemaker', "form": form, "form_file": form_file,
                "message": "success"}
    template1 = 'moviemakers.html'

    return render(request, template1, context1)


@csrf_exempt
def search_location(request):
    search = request.POST.get('search')

    print search

    locations = Location.objects.filter(name__contains=search)
    context = {'query': search, 'locations': locations, "location": "location"}
    template = 'locations.html'

    return render(request, template, context)
