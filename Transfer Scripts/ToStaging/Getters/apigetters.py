import anapioficeandfire

import basicgetters as bsc

class ApiGetter(bsc.BasicGetter):
    def _connect(self, outmodel):
        self.api = anapioficeandfire.API()

        self.outmodel = outmodel

    def __call__(self, **apikwargs):
        inmodels = self.getmany(**apikwargs)

        outlist = []
        for inmodel in inmodels:
            mod = self.parse(inmodel)
            outlist.append(mod)

        return outlist

    def getmany(self):
        return

    def parse(self, *args):
        return

    def getCharName(self, url):
        if not url:
            return ''

        charId = int(''.join(i for i in url if i.isdigit()))

        char = self.api.get_character(id=charId)

        return char.name

    def getHouseName(self, url):
        if not url:
            return ''

        houseId = int(''.join(i for i in url if i.isdigit()))

        house = self.api.get_house(id=houseId)

        return house.name


class ApiCharacterGetter(ApiGetter):
    def getmany(self, **kwargs):
        return self.api.get_characters(**kwargs)

    def parse(self, rawchar):
        name = rawchar.name
        
        gender = rawchar.gender
        
        born = rawchar.born
        died = rawchar.died

        culture = rawchar.culture

        father = self.getCharName(rawchar.father)
        mother = self.getCharName(rawchar.mother)
        spouse = self.getCharName(rawchar.spouse)

        return self.outmodel(name, gender, born, died, culture, father, mother, spouse)

class ApiHouseGetter(ApiGetter):
    def getmany(self, **kwargs):
        return self.api.get_houses(**kwargs)

    def parse(self, rawhouse):
        name = rawhouse.name

        founder = self.getCharName(rawhouse.founder)
        heir = self.getCharName(rawhouse.heir)
        lord = self.getCharName(rawhouse.currentLord)

        overlord = self.getHouseName(rawhouse.overlord)

        region = rawhouse.region
        founded = rawhouse.founded
        diedout = rawhouse.diedOut
        words = rawhouse.words
        coatofarms = rawhouse.coatOfArms

        return self.outmodel(name, founder, heir, lord, overlord, region, founded,
                diedout, words, coatofarms)

