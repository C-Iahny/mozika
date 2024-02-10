#from django.conf.urls import url
from . import views
from django.urls import path, include

app_name = 'music'

urlpatterns = [

    path('', views.accueil, name='accueil'),

    path('searche_venues', views.search_venues, name='search-venues'),

    #path('searche_venues', views.list_venues, name='list-venues'),

    # /music/
    path('index/', views.IndexView.as_view(), name="index"),
    #url(r'^$', views.index, name='index'),

    #url(r'^register/$', views.UserFormView.as_view(), name='register'),
    path('register/', views.register, name='register'),

    path('login_user/', views.login_user, name='login_user'),

    path('create_album/', views.create_album, name='create_album'),


    # /music/<album_id>/
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

   path('(<album_id>[0-9]+)/', views.detail, name='detail'), 

    #url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    path('song/add/', views.create_song, name='song-add'),

   path('(<album_id>[0-9]+)/delete_song/(<song_id>[0-9]+)/', views.delete_song, name='delete-song'),

    path('(<album_id>[0-9]+)/create_song/', views.create_song, name='create_song'),

    path('album/(<pk>[0-9]+)/', views.AlbumUpdate.as_view(), name='album-update'),

    path('album/(<pk>[0-9]+)/delete/', views.AlbumDelete.as_view(), name='album-delete'),

    path('songs/(<filter_by>[a-zA_Z]+)/', views.songs, name='songs'),

    path('(<song_id>[0-9]+)/favorite/', views.favorite, name='favorite'),

    # /music/<album_id>/favorite
    path('(<album_id>[0-9]+)/favorite_album/', views.favorite_album, name='favorite_album'),


    path('logout_user/', views.logout_user, name='logout_user'),

    path('songpost/', views.songpost_view, name='songpost'),


    path('lecteur/<int:id>/', views.lecteur, name='lecteur'),



]
