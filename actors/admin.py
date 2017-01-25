from django.contrib import admin

from .models import Actor, ActorsImage, MovieMaker, Studio


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


admin.site.register(Studio, StudioAdmin)

admin.site.register(MovieMaker, MovieMakerAdmin)

admin.site.register(Actor, ActorAdmin)

admin.site.register(ActorsImage, ActorsImageAdmin)
