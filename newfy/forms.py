from django.forms import ModelForm, inlineformset_factory
from . import models

class PostForm(ModelForm):
    class Meta():
        model = models.Musica
        exclude = ['aprovado']

class AlbumForm(ModelForm):
    class Meta():
        model = models.Album
        exclude = ['aprovado']
    
BookFormSet = inlineformset_factory(models.Album, models.Musica, fields=('titulo',), extra=1)
