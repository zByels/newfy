from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Musica(models.Model):
    titulo = models.CharField()
    album = models.CharField()
    capa = models.ImageField(upload_to="posts/", blank=True, null=True)
    ano = models.IntegerField()
    duracao = models.TimeField()
    artistas = models.ManyToManyField(
        to=User, through="Compositores", through_fields=("Musica", "Artista"), related_name="musicas"
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