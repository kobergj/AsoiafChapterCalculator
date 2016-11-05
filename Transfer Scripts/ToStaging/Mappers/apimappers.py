import basicmappers as bsc

def extract_charname(char):
    if not char:
        return None, None

    nameparts = char.name.split(' ')

    if len(nameparts) == 1:
        return None, None

    if len(nameparts) == 2:
        return nameparts[0], nameparts[1]

    if len(nameparts) == 3:
        return nameparts[0] + ' ' + nameparts[1], nameparts[2]

    return ' '.join(nameparts), ''

def extract_housename(house):
    if not house:
        return None, None

    nameparts = house.name.split(' ')

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
        first, sur = extract_charname(apicharacter)
        
        gender = map_asis(apicharacter.gender)
        born = map_date(apicharacter.born)
        died = map_date(apicharacter.died)

        culture = map_asis(apicharacter.culture)

        fatherfirst, fathersur = extract_charname(apicharacter.father)
        motherfirst, mothersur = extract_charname(apicharacter.mother)
        spousefirst, spousesur = extract_charname(apicharacter.spouse)

        return [self.outmodel(first, sur, gender, born, died, culture, fatherfirst,
            fathersur, motherfirst, mothersur, spousefirst, spousesur)]

class HouseMapper(bsc.Mapper):
    def __call__(self, apihouse):
        name, branch = extract_housename(apihouse)

        founderfirst, foundersur = extract_charname(apihouse.founder)
        heirfirst, heirsur = extract_charname(apihouse.heir)
        lordfirst, lordsur = extract_charname(apihouse.lord)

        overlord, overlordbranch = extract_housename(apihouse.overlord)
        region = map_asis(apihouse.region)

        founded = map_date(apihouse.founded)
        diedout = map_date(apihouse.diedout)

        words = map_asis(apihouse.words)
        coatofarms = map_asis(apihouse.coatofarms)

        return [self.outmodel(name, branch, founderfirst, foundersur, heirfirst, heirsur,
            lordfirst, lordsur, overlord, overlordbranch, region, founded, diedout, words, coatofarms)]

class HousePossessionMapper(bsc.ListMapper):
    def extract_args(self, descr, housemodel):
        name, branch = extract_housename(housemodel)
        return descr, name, branch, None, None

class CharacterPossessionMapper(bsc.ListMapper):
    def extract_args(self, descr, char):
        first, sur = extract_charname(char)
        return descr, None, None, first, sur

class CharHouseRelationMapper(bsc.ListMapper):
    def extract_args(self, char, house):
        first, sur = extract_charname(char)
        house, branch = extract_housename(house)
        return first, sur, house, branch

class CadetBranchMapper(bsc.ListMapper):
    def __call__(self, apihouse):
        return bsc.ListMapper.__call__(self, apihouse.cadets, apihouse)

    def extract_args(self, cadet, master):
        master, masterbranch = extract_housename(master)
        cadet, cadetbranch = extract_housename(cadet)
        return master, masterbranch, cadet, cadetbranch

class AllegianceMapper(CharHouseRelationMapper):
    def __call__(self, apichar):
        return CharHouseRelationMapper.__call__(self, apichar.allegiances, apichar)

class MemberMapper(CharHouseRelationMapper):
    def __call__(self, apihouse):
        return CharHouseRelationMapper.__call__(self, apihouse.members, apihouse)

class SeatMapper(HousePossessionMapper):
    def __call__(self, apihouse):
        return HousePossessionMapper.__call__(self, apihouse.seats, apihouse)

class TitleMapper(HousePossessionMapper):
    def __call__(self, apihouse):
        return HousePossessionMapper.__call__(self, apihouse.titles, apihouse)

class WeaponMapper(HousePossessionMapper):
    def __call__(self, apihouse):
        return HousePossessionMapper.__call__(self, apihouse.weapons, apihouse)

class AliasMapper(CharacterPossessionMapper):
    def __call__(self, apichar):
        return CharacterPossessionMapper.__call__(self, apichar.aliases, apichar)

class TitleMapperChar(CharacterPossessionMapper):
    def __call__(self, apichar):
        return CharacterPossessionMapper.__call__(self, apichar.titles, apichar)

