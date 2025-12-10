
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Album(models.Model):
    capa = models.ImageField(upload_to="posts/", blank=True, null=True)
    nome = models.CharField()
    ano = models.IntegerField()

    def __str__(self):
        return self.nome



class Musica(models.Model):
    titulo = models.CharField()
    duracao = models.TimeField()
    artistas = models.ManyToManyField(
        to=User, through="Compositores", through_fields=("Musica", "Artista"), related_name="musicas"
    )

    album = models.ForeignKey(
        to=Album,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.titulo

class Compositores(models.Model):


    Musica = models.ForeignKey(
        to=Musica,
        on_delete=models.SET_NULL,
        null=True,
    )

    Artista = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
    )

