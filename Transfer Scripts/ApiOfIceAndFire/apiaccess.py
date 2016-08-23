import anapioficeandfire

api = anapioficeandfire.API()

book = api.get_book(id=2)

print book.__dict__