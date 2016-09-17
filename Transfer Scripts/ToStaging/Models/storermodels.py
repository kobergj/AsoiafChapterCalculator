
class CharInChapter:
    def __init__(self, charfirstname, charsurname, chaptername):
        self.charfirstname = charfirstname
        self.charsurname = charsurname
        self.chaptername = chaptername

class Chapter:
    def __init__(self, chaptername, chapternumber, bookname):
        self.name = chaptername
        self.number = chapternumber
        self.bookname = bookname

class Character:
    def __init__(self, first, sur, gender, born, died, culture, fatherfirst,
            fathersur, motherfirst, mothersur, spousefirst, spousesur):
        self.firstname = first
        self.surname = sur

        self.gender = gender
        self.born = born
        self.died = died

        self.culture = culture

        self.fatherfirst = fatherfirst
        self.fathersur = fathersur

        self.motherfirst = motherfirst
        self.mothersur = mothersur

        self.spousefirst = spousefirst
        self.spousesur = spousesur

class House:
    def __init__(self, name, seat, founderfirst, foundersur, heirfirst, heirsur,
            lordfirst, lordsur, overlord, overlordseat, region, founded, diedout, words, coatofarms):
        self.name = name
        self.seat = seat

        self.founderfirst = founderfirst
        self.foundersur = foundersur

        self.heirfirst = heirfirst
        self.heirsur = heirsur

        self.lordfirst = lordfirst
        self.lordsur = lordsur

        self.overlord = overlord
        self.overlordseat = overlordseat

        self.region = region

        self.founded = founded
        self.diedout = diedout

        self.words = words
        self.coatofarms = coatofarms

class Possession:
    def __init__(self, description, house, branch, charfirst, charsur):
        self.description = description

        self.house = house
        self.branch = branch

        self.charfirst = charfirst
        self.charsur = charsur

class CharHouseRelation:
    def __init__(self, first, sur, house, branch):
        self.first = first
        self.sur = sur

        self.house = house
        self.branch = branch

class CadetBranch:
    def __init__(self, master, masterbranch, cadet, cadetbranch):
        self.master = master
        self.masterbranch = masterbranch

        self.cadet = cadet
        self.cadetbranch = cadetbranch
