import basicmappers as bsc

class CharacterMapper(bsc.Mapper):
    def __call__(self, charlist):
        values = []
        for char in charlist:
            vallist = self.mapCharacter(char)
            if vallist:
                values.append(vallist)

        return values

    def mapCharacter(self, apicharacter):
        try:
            first, sur = apicharacter.name.split(' ')
        except ValueError:
            first, sur = None, None

        gender = None
        if apicharacter.gender:
            gender = apicharacter.gender


        bornAt = None
        born = ''.join(i for i in apicharacter.born if i.isdigit())
        if born:
            bornAt = int(born) 

        diedAt = None
        died = ''.join(i for i in apicharacter.died if i.isdigit())
        if died:
            diedAt = int(died)

        return self.outmodel(first, sur, gender, bornAt, diedAt)
