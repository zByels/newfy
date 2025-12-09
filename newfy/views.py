from django.shortcuts import redirect, render
from newfy import models
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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
