import Models.storermodels as smod
import Models.gettermodels as gmod

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
        gettermodel = self.getter(**getterargs)

        if not gettermodel:
            return

        storermodelList = self.mapper(gettermodel)

        for storermodel in storermodelList:

            query = self.querygenerator(storermodel)

            self.connection(query)

        return True

def TransferCharactersFromApi(*pages):
    etl = DataTransfer(getter=apiget.ApiCharacterGetter(gmod.Character), 
                        mapper=apimap.CharacterMapper(smod.Character),
                        querygenerator=insquery.InsertCharacter(),
                        connection=postgres.StagingConnection("AsoiafDWH")
                        )

    for i in pages:
        etl(page=i)

def TransferHousesFromApi(*pages):
    etl = DataTransfer(getter=apiget.ApiHouseGetter(gmod.House), 
                        mapper=apimap.HouseMapper(smod.House),
                        querygenerator=insquery.InsertHouse(),
                        connection=postgres.StagingConnection("AsoiafDWH")
                        )

    for i in pages:
        etl(page=i)

def TransferChapterNumbers(filepath):
    etl = DataTransfer(getter=yamlget.YamlGetter(filepath),
                       mapper=yamlmap.ChapterMapper(smod.Chapter),
                       querygenerator=insquery.InsertChapter(),
                       connection=postgres.StagingConnection("AsoiafDWH")
                       )

    etl()

def TransferCharInChapter(filepath):
    etl = DataTransfer(getter=yamlget.YamlGetter(filepath),
                       mapper=yamlmap.CharInChapterMapper(smod.CharInChapter),
                       querygenerator=insquery.InsertCharInChapter(),
                       connection=postgres.StagingConnection("AsoiafDWH")
                       )

    etl()

if __name__=='__main__':
    # Chapter Numbers
    TransferChapterNumbers("/Users/Kokweazel/Documents/AsoiafYamls/chapternames.yaml")

    # Main Chars
    TransferCharInChapter("/Users/Kokweazel/Documents/AsoiafYamls/maincharacters.yaml")

    # Characters
    TransferCharactersFromApi(*range(10, 30))

    # Houses
    TransferHousesFromApi(*range(30, 50))



