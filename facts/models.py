from django.db import models


class Artist(models.Model):
    artistID = models.AutoField(primary_key=True)
    fullName = models.TextField()

    def __str__(self):
        return self.fullName
    

class Song(models.Model):
    songID = models.AutoField(primary_key=True)
    sArtistID = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Fact(models.Model):
    factID = models.AutoField(primary_key=True)
    fSongID = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.TextField()

    def __str__(self):
        return self.content





