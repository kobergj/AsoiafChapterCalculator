
class Character:
    def __init__(self, name, gender, born, died, culture, father, mother, spouse, titles, aliases): 
        self.name = name 
        self.gender = gender 
        self.born = born 
        self.died = died 
        self.father = father 
        self.culture = culture 
        self.mother = mother
        self.spouse = spouse

        self.titles = titles
        self.aliases = aliases

class House:
    def __init__(self, name, founder, heir, lord, overlord, region, founded, diedout,
            words, coatofarms, weapons, titles, seats):
        self.name = name
        self.founder = founder
        self.heir = heir
        self.lord = lord
        self.overlord = overlord
        self.region = region
        self.founded = founded
        self.diedout = diedout
        self.words = words
        self.coatofarms = coatofarms

        self.weapons = weapons
        self.titles = titles
        self.seats = seats
