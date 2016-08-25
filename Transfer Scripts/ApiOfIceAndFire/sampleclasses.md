
# Class Samples
mostly for reference. Will be removed soon

## Sample Of Character Class:
```python
class Character:
    titles = [u"Lord Commander of the Night's Watch"]
    name = u'Jon Snow'
    born = u'In 283 AC'
    url = u'http://anapioficeandfire.com/api/characters/583'
    gender: u'Male',
    father: u''
    
    allegiances = [u'http://anapioficeandfire.com/api/houses/362']
    
    povBooks = [u'http://anapioficeandfire.com/api/books/1', u'http://anapioficeandfire.com/api/books/2', u'http://anapioficeandfire.com/api/books/3', u'http://anapioficeandfire.com/api/books/8']
    
    culture = u'Northmen'
    playedBy = [u'Kit Harington']
    api = <anapioficeandfire.api.API object at 0x1006f4710>
    books = [u'http://anapioficeandfire.com/api/books/5']

    tvSeries = [u'Season 1', u'Season 2', u'Season 3', u'Season 4', u'Season 5', u'Season 6']

    mother = u''

    spouse = u''

    died = u''

    aliases = [u'Lord Snow', u"Ned Stark's Bastard", u'The Snow of Winterfell', u'The Crow-Come-Over', u"The 998th Lord Commander of the Night's Watch", u'The Bastard of Winterfell', u'The Black Bastard of the Wall', u'Lord Crow']
```

## Sample Of Book Class:
```python
class Book:
    numberOfPages = 768
    isbn = u'978-0553108033'
    name = u'A Clash of Kings'
    publisher= u'Bantam Books'
    url = u'http://anapioficeandfire.com/api/books/2 
    country = u'United States'
    povCharacters = [u'http://anapioficeandfire.com/api/characters/148', ...]
    mediaType = u'Hardcover'
    released = u'1999-02-02T00:00:00'
    api = <anapioficeandfire.api.API object at 0x101a04710>
    characters = [u'http://anapioficeandfire.com/api/characters/2', ...]
```

## Sample Of House Class:
```python
class House:
    overlord = u'http://anapioficeandfire.com/api/houses/16
    titles = [u"Lord of Storm's End", u'Lord Paramount of the Stormlands']
    name = u"House Baratheon of Storm's End"
    founder = u'http://anapioficeandfire.com/api/characters/797'
    url = u'http://anapioficeandfire.com/api/houses/17
    region = u'The Stormlands'
    heir = u'http://anapioficeandfire.com/api/characters/775'
    cadetBranches = [u'http://anapioficeandfire.com/api/houses/15', ...]
    founded = u'1 AC'
    diedOut = u''
    api = <anapioficeandfire.api.API object at 0x101904710>
    coatOfArms = u'A black crowned stag, on a gold field(Or, a stag salient, crowned, sable)
    words = u'Ours is the Fury'
    seats = [u"Storm's End", u'Dragonstone (House Baratheon of Dragonstone)']
    ancestralWeapons = []
    swornMembers = [u'http://anapioficeandfire.com/api/characters/110', ...]
    currentLord = u'http://anapioficeandfire.com/api/characters/1029'
```
    
