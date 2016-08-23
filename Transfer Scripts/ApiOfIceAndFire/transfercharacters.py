import sys
import os
import anapioficeandfire

os.chdir('/Users/Kokweazel/AsoiafDWH')

import Connections.postgresconn as pc
import QueryGenerators.querygenerators as qg

class CharacterParser:
    def __init__(self, db, uid, pwd):
        self.connection = pc.Connection(db, uid, pwd)

        self.api = anapioficeandfire.API()

    def __call__(self, charactername):
        characters = self.api.get_characters(page=charactername)

        if not characters:
            return

        for char in characters:

            try:
                firstname, surname = char.name.split(' ')
            except ValueError:
                continue

            gender = char.gender

            born = ''.join(i for i in char.born if i.isdigit())

            died = ''.join(i for i in char.died if i.isdigit())

            querygenerator = qg.Character(firstname, surname, gender, born, died)

            self.connection(querygenerator)

        return True

if __name__ == '__main__':
    uid, pwd = sys.argv[1:3]
    char_parser = CharacterParser('AsoiafDWH', uid, pwd)

    for i in range(1, 300):
        success = char_parser(i)

        if not success:
            break
