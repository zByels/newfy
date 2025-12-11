from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_posts, name="lista_posts"),
    path('signup/', views.signup, name='signup'),
    path('album/', views.ListarAlbum.as_view(), name="lista_album"),
    path('postar/', views.CriaAlbum.as_view(), name="postar"),
    path('criarmusica/', views.CriaMusica.as_view(), name='criarmusica'), 
    path('editar/<int:pk>', views.Editar.as_view(), name='editar'),
    path('delalbum/<int:pk>', views.DelAlbum.as_view(), name='delalbum'),
    path('delmusica/<int:pk>', views.DelMusica.as_view(), name='delmusica'),
    path('accounts/', include('django.contrib.auth.urls')),  
]