from django.contrib import admin
from .models import *

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['artist_name', 'nickname', 'artist_image','email','created_at','bio']
    list_filter = ['artist_name', 'nickname']

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_name','artist','year_released']
    list_filter = ['album_name','artist','year_released']

class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name','album','writer','artist','song_image','duration']
    list_filter = ['song_name','album','writer','artist']

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
