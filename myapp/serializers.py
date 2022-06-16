
from dataclasses import fields
from pyexpat import model
from .models import *
from rest_framework import serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','artist_name','nickname','artist_image','email','created_at','bio']

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['id','album_name','artist','year_released']


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id','song_name','album','writer','artist','song_image','duration']
