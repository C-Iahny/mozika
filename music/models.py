from django.contrib.auth.models import Permission, User
from django.db import models
from django.urls import reverse

class Album(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(upload_to='images/', max_length=1000)
    is_favorite = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(upload_to='musics/', default='')
    is_favorite = models.BooleanField(default=False)
    #time_length = models.DecimalField(blank=True, max_digits=20, decimal_places=2)

    def __str__(self):
        return self.song_title

"""
    def save(self, *args, **kwargs):
        if not self.time_length:
            # logic for getting music length here
            pass
        return super().save(*args, **kwargs)
"""
