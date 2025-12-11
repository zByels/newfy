from django.shortcuts import redirect, render
from newfy import models
from .forms import AlbumForm, PostForm, BookFormSet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib import messages
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mestre')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class ListarAlbum(ListView):
    model = models.Album
    template_name = 'lista_album.html'
    context_object_name = 'posts'



class MusicaInline(InlineFormSetFactory):
    model = models.Musica
    fields = ['titulo']

class CriaAlbum(LoginRequiredMixin, CreateWithInlinesView):
    model = models.Album
    template_name = 'album.html'
    fields = ['capa', 'nome', 'ano']
    success_url = reverse_lazy('lista_posts')
    permission_denied_message = 'Por favor, entre ou crie uma conta'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.WARNING, self.permission_denied_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)   

class CriaMusica(LoginRequiredMixin, CreateView):
    model = models.Musica
    template_name = 'postar.html'
    fields=['titulo', 'duracao', 'artistas', 'album']
    success_url = reverse_lazy('lista_posts')

class Editar(LoginRequiredMixin, UpdateWithInlinesView):
    model = models.Album
    template_name = 'editar.html'
    inlines = [MusicaInline,]
    fields=['capa', 'nome', 'ano']
    success_url = reverse_lazy('lista_posts')

class DelAlbum(LoginRequiredMixin, DeleteView):
    model = models.Album
    success_url = reverse_lazy('lista_posts')

class DelMusica(LoginRequiredMixin, DeleteView):
    model = models.Musica
    success_url = reverse_lazy('lista_posts')
    

@login_required(login_url='/contas/login')
def postar_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lista_posts")
    else:
        form = PostForm()

    return render(request, "postar.html", {"form": form})

def lista_posts(req):
    posts = models.Musica.objects.all()
    return render(req, "lista_posts.html", {"posts": posts})
