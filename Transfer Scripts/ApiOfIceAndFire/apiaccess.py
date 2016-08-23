import anapioficeandfire

api = anapioficeandfire.API()

jon_snow = api.get_character(id=583)

for title in jon_snow.aliases:
    print(title)

print jon_snow.__dict__