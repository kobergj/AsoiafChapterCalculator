import anapioficeandfire

import basicgetters as bsc

class ApiGetter(bsc.BasicGetter):
    def _connect(self, outmodel, cache):
        self.api = anapioficeandfire.API()

        self.outmodel = outmodel

        self._charactercache = cache.character
        self._housecache = cache.house

    def __call__(self, **apikwargs):
        inmodels = self.getmany(**apikwargs)

        outlist = []
        for inmodel in inmodels:
            args = self.parse(inmodel)
            outlist.append(self.outmodel(*args))

        return outlist

    def getmany(self, **kwargs):
        # Should Return Specific Page of Api
        return None

    def parse(self, model):
        # Should Return Arguments for StorerModel
        return None

    def extractId(self, url):
        if url:
            return int(''.join(i for i in url if i.isdigit()))

    def get_some(self, cache, getter, url):
        Id = self.extractId(url)

        if Id in cache:
            return cache[Id]

        some = getter(id=Id)

        cache.update({Id: some})

        return some

    def get_char(self, url):
        return self.get_some(self._charactercache, self.api.get_character, url)

    def get_house(self, url):
        return self.get_some(self._housecache, self.api.get_house, url)

class ApiCharacterGetter(ApiGetter):
    def getmany(self, **kwargs):
        return self.api.get_characters(**kwargs)

    def parse(self, rawchar):
        name = rawchar.name
        
        gender = rawchar.gender
        
        born = rawchar.born
        died = rawchar.died

        culture = rawchar.culture

        father = self.get_char(rawchar.father)
        mother = self.get_char(rawchar.mother)
        spouse = self.get_char(rawchar.spouse)

        titles = rawchar.titles
        aliases = rawchar.aliases

        allegiances = []
        for charUrl in rawchar.allegiances:
            allegiances.append(self.get_char(charUrl))

        return name, gender, born, died, culture, father, mother, spouse, \
            titles, aliases, allegiances

class ApiHouseGetter(ApiGetter):
    def getmany(self, **kwargs):
        return self.api.get_houses(**kwargs)

    def parse(self, rawhouse):
        name = rawhouse.name

        founder = self.get_char(rawhouse.founder)
        heir = self.get_char(rawhouse.heir)
        lord = self.get_char(rawhouse.currentLord)

        overlord = self.get_house(rawhouse.overlord)

        region = rawhouse.region
        founded = rawhouse.founded
        diedout = rawhouse.diedOut
        words = rawhouse.words
        coatofarms = rawhouse.coatOfArms

        weapons = rawhouse.ancestralWeapons
        titles = rawhouse.titles
        seats = rawhouse.seats

        members = []
        for charUrl in rawhouse.swornMembers:
            members.append(self.get_char(charUrl))

        cadets = []
        for houseUrl in rawhouse.cadetBranches:
            cadets.append(self.get_house(houseUrl))

        return name, founder, heir, lord, overlord, region, founded, \
            diedout, words, coatofarms, weapons, titles, seats, members, cadets

