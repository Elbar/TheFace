from django.contrib import admin

from .models import Actor, ActorsImage, MovieMaker, Studio, Location, News, StudioImage, StudioLink, Project


class ActorAdmin(admin.ModelAdmin):
    search_fields = ['identify']
    list_display = ['identify']
    list_filter = ['sex', 'timestamp', 'age', 'weight', 'height']
    readonly_fields = ['updated', 'timestamp']

    class Meta:
        model = Actor


class ActorsImageAdmin(admin.ModelAdmin):
    class Meta:
        model = ActorsImage


class MovieMakerAdmin(admin.ModelAdmin):
    class Meta:
        model = MovieMaker


class StudioAdmin(admin.ModelAdmin):
    class Meta:
        model = Studio


class NewsAdmin(admin.ModelAdmin):
    class Meta:
        model = News


class LocationAdmin(admin.ModelAdmin):
    class Meta:
        model = Location


class StudioImageAdmin(admin.ModelAdmin):
    class Meta:
        model = StudioImage


class StudioLinkAdmin(admin.ModelAdmin):
    class Meta:
        model = StudioLink


class ProjectMovieMakerAdmin(admin.ModelAdmin):
    class Meta:
        model = Project


admin.site.register(Project, ProjectMovieMakerAdmin)

admin.site.register(StudioLink, StudioLinkAdmin)

admin.site.register(StudioImage, StudioImageAdmin)

admin.site.register(Location, LocationAdmin)

admin.site.register(News, NewsAdmin)

admin.site.register(Studio, StudioAdmin)

admin.site.register(MovieMaker, MovieMakerAdmin)

admin.site.register(Actor, ActorAdmin)

admin.site.register(ActorsImage, ActorsImageAdmin)
