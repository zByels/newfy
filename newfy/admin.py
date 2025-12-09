from django.contrib import admin
from . import models
from django.contrib.auth.models import User



class ArtistasMusicas(admin.StackedInline):
    model = models.User.musicas.through
    extra = 0


class MusicasAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    inlines = (ArtistasMusicas,)



admin.site.register(models.Musica, MusicasAdmin)

# Register your models here.
