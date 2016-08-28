import sys
import datetime
import anapioficeandfire

# os.chdir('/Users/Kokweazel/AsoiafDWH')

import Connections.postgresconn as pc
# import QueryGenerators.querygenerators as qg
import QueryGenerators.instaging as sta

def parseCharacter(apicharacter):
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


class ApiDocumentToDatabase:
    def __init__(self, getter, mapper, querygenerator, storer):
        self.getter = getter
        self.mapper = mapper
        self.querygenerator = querygenerator
        self.storer = storer

    def __call__(self, index):
        page = self.getter(page=index)

        if not page:
            return

        for document in page:
            values = self.mapper(document)

            query = self.querygenerator(insertiontime=datetime.datetime.now(), **values)

            self.storer(query)

        return True


def TransferCharacterPages(*pagenumbers):
    uid, pwd = sys.argv[1:3]

    etl = ApiDocumentToDatabase(
            getter=anapioficeandfire.API().get_characters, 
            mapper=parseCharacter,
            querygenerator=sta.StagingLoader("character"),
            storer=pc.StagingConnection("AsoiafDWH", uid, pwd)
        )

    for i in range(*pagenumbers):
        success = etl(i)

        if not success:
            return

if __name__ == '__main__':
    TransferCharacterPages(17, 40)