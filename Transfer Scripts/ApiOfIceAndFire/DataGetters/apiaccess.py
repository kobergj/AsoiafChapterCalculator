import anapioficeandfire

api = anapioficeandfire.API()

chars = api.get_characters(pages=range(5))

print chars[0].url