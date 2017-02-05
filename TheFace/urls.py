"""TheFace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.conf.urls.static import static
from django.contrib import admin

from TheFace import settings

urlpatterns = patterns('',
                       url(r'^admin/', admin.site.urls),
                       url(r'^$', 'actors.views.index_view', name='index'),
                       url(r'^actors/', 'actors.views.actor_view', name='actor'),
                       url(r'^result/', 'actors.views.filter_actor', name='filter'),
                       url(r'^result_movimaker/', 'actors.views.moviemaker_result_view', name='filter_moviemaker'),
                       url(r'^beactor/', 'actors.views.become_an_actor_view', name='beactor'),
                       url(r'^moviemakers/', 'actors.views.moviemaker_view', name='moviemaker'),
                       url(r'^sendmail/', 'actors.views.send_mail', name='sendmail'),
                       url(r'^news/', 'actors.views.news_view', name='news'),
                       url(r'^get_studio/', 'actors.views.get_studio', name='get_studio'),
                       url(r'^locations/', 'actors.views.location_view', name='location'),
                       url(r'^studio/', 'actors.views.studio_view', name='studio'),
                       url(r'^studios/(?P<id>\d+)/$', 'actors.views.single_studio', name='single_studio'),
                       url(r'^about/', 'actors.views.about_view', name='about'),
                       url(r'^new/(?P<id>\d+)/$', 'actors.views.singleNews', name='single_news'),
                       url(r'^ajax/actors/get/(?P<id>\d+)', 'actors.views.ajax_actor_view', name='ajax_actor_get'),
                       url(r'^ajax/moviemakers/get/(?P<id>\d+)', 'actors.views.ajax_moviemakers_view',
                           name='ajax_moviemaker_get'),
                       url(r'^application/', 'actors.views.send_application', name='application'),
                       )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
