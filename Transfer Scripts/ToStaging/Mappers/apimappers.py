
def mapCharacter(apicharacter):
    valuedict = {}

    try:
        valuedict['firstname'], valuedict['surname'] = apicharacter.name.split(' ')
    except ValueError:
        return {}

    if apicharacter.gender:
        valuedict['gender'] = apicharacter.gender

    born = ''.join(i for i in apicharacter.born if i.isdigit())

    if born:
        valuedict['born'] = int(born) 

    died = ''.join(i for i in apicharacter.died if i.isdigit())

    if died:
        valuedict['died'] = int(died)

    return valuedict
