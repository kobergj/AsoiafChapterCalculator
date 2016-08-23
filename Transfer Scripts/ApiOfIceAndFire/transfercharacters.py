import sys
import anapioficeandfire

import Connections.postgresconn as pc
import QueryGenerators.querygenerators as qg

class CharacterParser:
    def __init__(self, db, uid, pwd):
        self.connection = pc.Connection(db, uid, pwd)

        self.api = anapioficeandfire.API()

    def __call__(self, page):
        characters = self.api.get_characters(page=page)

        for char in characters:
            querygenerator = qg.Character(char.name)

        self.conn(querygenerator)

if __name__ == '__main__':
    uid, pwd = sys.argv[1:3]
    char_parser = CharacterParser('AsoiafDWH', uid, pwd)

    char_parser(0)
