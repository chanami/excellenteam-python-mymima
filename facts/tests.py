from django.test import TestCase
from facts.models import Artist, Fact, Song


class FactsTestCase(TestCase):

    def setUp(self):
        Artist.objects.create(fullName="Maroon 5")
        Artist.objects.create(fullName="Bob Marley")
        Artist.objects.create(fullName="Frank Sinatra")
        Artist.objects.create(fullName="Leonard Cohen")

        Song.objects.create(title="Sugar", sArtistID=Artist.objects.get(fullName="Maroon 5"))
        Song.objects.create(title="She Will Be Loved", sArtistID=Artist.objects.get(fullName="Maroon 5"))
        Song.objects.create(title="A Lalala Long", sArtistID=Artist.objects.get(fullName="Bob Marley"))
        Song.objects.create(title="No Woman No Cry", sArtistID=Artist.objects.get(fullName="Bob Marley"))
        Song.objects.create(title="My Way", sArtistID=Artist.objects.get(fullName="Frank Sinatra"))
        Song.objects.create(title="New York", sArtistID=Artist.objects.get(fullName="Frank Sinatra"))
        Song.objects.create(title="Hallelujah", sArtistID=Artist.objects.get(fullName="Leonard Cohen"))

        Fact.objects.create(author="Adam Levin",
                            content="New song Sugar!!! \" Available Now!",
                            fSongID=Song.objects.get(title="Sugar"))
        Fact.objects.create(author="Adam Levin & Band",
                            content="It's a good song and new song\" check it out \"***** SUGAR *****!",
                            fSongID=Song.objects.get(title="Sugar"))
        Fact.objects.create(author="Bob Marley",
                            content="Smoking frees the soul. He believed that smoking cannabis freed the soul. ...!",
                            fSongID=Song.objects.get(title="A Lalala Long"))
        Fact.objects.create(author="Frank Sinatra fan",
                            content="is son, Frank Sinatra, Jr., was kidnapped and held for ransom.",
                            fSongID=Song.objects.get(title="My Way"))
        Fact.objects.create(author="Leonard Cohen fan",
                            content="What a song!!\" Hallelujah ",
                            fSongID=Song.objects.get(title="Hallelujah"))

    def test_basic_model(self):
        leonard_cohen = Artist.objects.get(fullName="Leonard Cohen")
        no_woman = Song.objects.get(title="No Woman No Cry")
        frank_fact = Fact.objects.get(author="Frank Sinatra fan")

        self.assertEqual(Artist.objects.count(), 4)
        self.assertEqual(Song.objects.count(), 7)
        self.assertEqual(Fact.objects.count(), 5)

        self.assertEqual(leonard_cohen.fullName, "Leonard Cohen")
        self.assertEqual(no_woman.title, "No Woman No Cry")
        self.assertEqual(frank_fact.content, "is son, Frank Sinatra, Jr., was kidnapped and held for ransom.")
