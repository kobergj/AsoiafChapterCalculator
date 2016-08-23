import anapioficeandfire

api = anapioficeandfire.API()

house = api.get_house(id=17)

print house.__dict__