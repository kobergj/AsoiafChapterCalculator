import basicmappers as bsc

def map_charname(charcomplete):
    nameparts = charcomplete.split(' ')

    if len(nameparts) == 1:
        return None, None

    if len(nameparts) == 2:
        return nameparts[0], nameparts[1]

    if len(nameparts) == 3:
        return nameparts[0] + ' ' + nameparts[1], nameparts[2]

    return ' '.join(nameparts), ''

def map_housename(housecomplete):
    nameparts = housecomplete.split(' ')

    if len(nameparts) == 1:
        return None, None

    if len(nameparts) == 2:
        return nameparts[1], None

    return nameparts[1], ' '.join(nameparts[2:])

def map_date(rawdate):
    date = ''.join(i for i in rawdate if i.isdigit())

    if not date:
        return None

    if len(date) <= 3:
        return int(date)

    if len(date) <= 5:
        return (int(date[:2]) + int(date[2:])) / 2

    if len(date) == 6:
        return (int(date[:3]) + int(date[3:])) / 2

    return int(date)

def map_asis(rawstring):
    if not rawstring:
        return None

    return rawstring


class CharacterMapper(bsc.Mapper):
    def __call__(self, apicharacter):
        first, sur = map_charname(apicharacter.name)
        
        gender = map_asis(apicharacter.gender)
        born = map_date(apicharacter.born)
        died = map_date(apicharacter.died)

        culture = map_asis(apicharacter.culture)

        fatherfirst, fathersur = map_charname(apicharacter.father)
        motherfirst, mothersur = map_charname(apicharacter.mother)
        spousefirst, spousesur = map_charname(apicharacter.spouse)

        return [self.outmodel(first, sur, gender, born, died, culture, fatherfirst,
            fathersur, motherfirst, mothersur, spousefirst, spousesur)]

class HouseMapper(bsc.Mapper):
    def __call__(self, apihouse):
        name, branch = map_housename(apihouse.name)

        founderfirst, foundersur = map_charname(apihouse.founder)
        heirfirst, heirsur = map_charname(apihouse.heir)
        lordfirst, lordsur = map_charname(apihouse.lord)

        overlord, overlordbranch = map_housename(apihouse.overlord)
        region = map_asis(apihouse.region)

        founded = map_date(apihouse.founded)
        diedout = map_date(apihouse.diedout)

        words = map_asis(apihouse.words)
        coatofarms = map_asis(apihouse.coatofarms)

        return [self.outmodel(name, branch, founderfirst, foundersur, heirfirst, heirsur,
            lordfirst, lordsur, overlord, overlordbranch, region, founded, diedout, words, coatofarms)]

class PossessionMapper(bsc.Mapper):
    def for_loop(self, poslist, apihouseorchar):
        outmodels = []
        for seat in poslist:
            description = seat

            name, branch, first, sur = self.identify(apihouseorchar.name)

            outmodels.append(self.outmodel(description, name, branch, first, sur))

        return outmodels

class HousePossessionMapper(PossessionMapper):
    def identify(self, housename):
        name, branch = map_housename(housename)
        return name, branch, None, None

class CharacterPossessionMapper(PossessionMapper):
    def identify(self, charname):
        first, sur = map_charname(charname)
        return None, None, first, sur

class SeatMapper(HousePossessionMapper):
    def __call__(self, apihouse):
        return self.for_loop(apihouse.seats, apihouse)

class TitleMapper(HousePossessionMapper):
    def __call__(self, apihouse):
        return self.for_loop(apihouse.titles, apihouse)

class WeaponMapper(HousePossessionMapper):
    def __call__(self, apihouse):
        return self.for_loop(apihouse.weapons, apihouse)

class AliasMapper(CharacterPossessionMapper):
    def __call__(self, apichar):
        return self.for_loop(apichar.aliases, apichar)

class TitleMapperChar(CharacterPossessionMapper):
    def __call__(self, apichar):
        return self.for_loop(apichar.titles, apichar)

