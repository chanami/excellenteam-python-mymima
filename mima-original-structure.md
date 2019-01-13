# Original Website Structure: mima.co.il

## Pages
* Home page: https://www.mima.co.il/
* artists results page: https://www.mima.co.il/artists_letter?letter=zzzz
* songs results page: https://www.mima.co.il/songs_letter?letter=zzzz
* search results page: https://www.mima.co.il/search?word=zzzz
* Artist page: https://www.mima.co.il/artist?id=zzzz
* Song page: https://www.mima.co.il/song?id=zzzz

## Entities and Relationships

### Artist
* id (number)
* FullName (string)

### Song
* id (number)
* ArtistId (number)
* Title (string)

### Fact
* id (number)
* songId (number)
* content (string)
* writtenBy (string)
