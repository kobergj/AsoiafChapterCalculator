
def mapCharacters(charlist):
    values = []
    for char in charlist:
        vallist = mapCharacter(char)
        if vallist:
            values.append(vallist)

    return values

def mapCharacter(apicharacter):
    values = [None, None, None, None, None]

    try:
        values[0], values[1] = apicharacter.name.split(' ')
    except ValueError:
        pass

    if apicharacter.gender:
        values[2] = apicharacter.gender

    born = ''.join(i for i in apicharacter.born if i.isdigit())

    if born:
        values[3] = int(born) 

    died = ''.join(i for i in apicharacter.died if i.isdigit())

    if died:
        values[4] = int(died)

    return values
