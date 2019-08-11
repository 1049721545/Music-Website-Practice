from django.conf.urls import url
from . import views


app_name = 'music'

urlpatterns = [
    # /music/register/
    url(r'^register/$', views.register, name='register'),

    # /music/user_login/
    url(r'^user_login/$', views.login_user, name='login_user'),

    # /music/user_logout/
    url(r'^user_logout/$', views.logout_user, name='logout_user'),

    # /music/
    url(r'^$', views.index, name='index'),

    # /music/album_pk/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/create_album/
    url(r'^create_album/$', views.create_album, name='create_album'),

    # /music/album_pk/delete/
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),

    # /music/album/favorite_album/
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),

    # music/songs/song_pk
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),

    # /music/album_pk/create_song/
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),

    # /music/album/pk/delete_song/
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),

    # /music/song_pk/favorite/
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
