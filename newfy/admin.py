from django.contrib import admin
from . import models
from django.contrib.auth.models import User


@admin.register(models.Musica)
class AdminMusica(admin.ModelAdmin):
    model = models.Musica
    extra = 0

    class ArtistaInline(admin.TabularInline):
        model = models.Musica.artistas.through
        extra = 0
    
    inlines = [ArtistaInline,]


@admin.register(models.Album)
class AlbumMusica(admin.ModelAdmin):
    model = models.Album
    extra = 0

    class MusicaInline(admin.TabularInline):
        model = models.Musica
        extra = 0
    
    inlines = [MusicaInline,]


# Register your models here.
