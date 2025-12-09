from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_posts, name="lista_posts"),
    path('signup/', views.signup, name='signup'),
    path('postar/', views.postar_view, name="postar"),
    path('', include('django.contrib.auth.urls')),

]