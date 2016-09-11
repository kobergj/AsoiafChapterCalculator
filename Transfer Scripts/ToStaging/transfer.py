
import Getters.apigetters as apiget
import Getters.yamlgetters as yamlget

import Mappers.apimappers as apimap
import Mappers.yamlmappers as yamlmap

import QueryGenerators.insertqueries as insquery
import Connections.postgresconn as postgres

class DataTransfer:
    def __init__(self, getter, mapper, querygenerator, connection):
        self.getter = getter
        self.mapper = mapper
        self.querygenerator = querygenerator
        self.connection = connection

    def __call__(self, **getterargs):
        page = self.getter(**getterargs)

        if not page:
            return

        valueList = self.mapper(page)

        for values in valueList:

            query = self.querygenerator(*values)

            self.connection(query)

        return True

def TransferCharactersFromApi(*pages):
    etl = DataTransfer(getter=apiget.ApiCharacterGetter(), 
                        mapper=apimap.mapCharacters,
                        querygenerator=insquery.InsertCharacter(),
                        connection=postgres.StagingConnection("AsoiafDWH")
                        )

    for i in pages:
        etl(page=i)

def CalculateChapterNumbers(filepath):
    etl = DataTransfer(getter=yamlget.YamlGetter(filepath),
                       mapper=yamlmap.mapChapters,
                       querygenerator=insquery.InsertChapter(),
                       connection=postgres.StagingConnection("AsoiafDWH")
                       )

    etl()

def TransferCharInChapter(filepath):
    etl = DataTransfer(getter=yamlget.YamlGetter(filepath),
                       mapper=yamlmap.mapCharInChapter,
                       querygenerator=insquery.InsertCharInChapter(),
                       connection=postgres.StagingConnection("AsoiafDWH")
                       )

    etl()

def test(*pages):
    for i in pages:
        print i

if __name__=='__main__':
    TransferCharactersFromApi(*range(1, 100))
    #CalculateChapterNumbers("/Users/Kokweazel/Documents/AsoiafYamls/chapternames.yaml")
    #TransferCharInChapter("/Users/Kokweazel/Documents/AsoiafYamls/maincharacters.yaml")

