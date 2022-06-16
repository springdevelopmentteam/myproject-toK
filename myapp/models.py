from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    artist_image = models.ImageField()
    email = models.EmailField()
    created_at = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    album_name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    year_released = models.IntegerField()

    def __str__(self):
        return self.album_name

class Song(models.Model):
    song_name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    writer = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_image = models.ImageField()
    duration = models.DurationField()

    def __str__(self):
        return self.song_name

