from django.contrib import admin

from .models import Actor, ActorsImage


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


admin.site.register(Actor, ActorAdmin)

admin.site.register(ActorsImage, ActorsImageAdmin)
