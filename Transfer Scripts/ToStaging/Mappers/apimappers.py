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

def map_date(rawdate):
    date = ''.join(i for i in rawdate if i.isdigit())

    if not date:
        return None

    if len(date) == 6:
        return (int(date[:3]) + int(date[3:]))/2

    return int(date)

def map_asis(rawstring):
    if not rawstring:
        return None

    return rawstring

class CharacterMapper(bsc.Mapper):
    def __call__(self, charlist):
        values = []
        for char in charlist:
            vallist = self.mapCharacter(char)
            if vallist:
                values.append(vallist)

        return values

    def mapCharacter(self, apicharacter):
        first, sur = map_charname(apicharacter.name)
        
        gender = map_asis(apicharacter.gender)
        born = map_date(apicharacter.born)
        died = map_date(apicharacter.died)

        culture = map_asis(apicharacter.culture)

        fatherfirst, fathersur = map_charname(apicharacter.father)
        motherfirst, mothersur = map_charname(apicharacter.mother)
        spousefirst, spousesur = map_charname(apicharacter.spouse)

        return self.outmodel(first, sur, gender, born, died, culture, fatherfirst,
            fathersur, motherfirst, mothersur, spousefirst, spousesur)
