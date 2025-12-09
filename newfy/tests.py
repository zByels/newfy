from django.test import TestCase
from .models import Musica
import pytest

@pytest.mark.django_db
def test_musica():
    musica = Musica.objects.create(titulo = 'Musica 1', album = 'Album 1', ano = '2025', duracao = '3:33')
    assert hasattr(musica, 'titulo')
    assert hasattr(musica, 'album')
    assert hasattr(musica, 'ano')
    assert hasattr(musica, 'duracao')