import anapioficeandfire

import basicgetters as bsc

class ApiCharacterGetter(bsc.BasicGetter):
    def _connect(self, charmodel):
        self.api = anapioficeandfire.API()

        self.charmodel = charmodel

    def __call__(self, **apikwargs):
        chars = self.api.get_characters(**apikwargs)

        clist = []
        for char in chars:
            cmod = self.parseCharacter(char)
            clist.append(cmod)

        return clist

    def parseCharacter(self, rawchar):
        name = rawchar.name
        
        gender = rawchar.gender
        
        born = rawchar.born
        died = rawchar.died

        culture = rawchar.culture

        father = self.getCharName(rawchar.father)
        mother = self.getCharName(rawchar.mother)
        spouse = self.getCharName(rawchar.spouse)

        return self.charmodel(name, gender, born, died, culture, father, mother, spouse)

    def getCharName(self, url):
        if not url:
            return ''

        charId = int(''.join(i for i in url if i.isdigit()))

        char = self.api.get_character(id=charId)

        return char.name

