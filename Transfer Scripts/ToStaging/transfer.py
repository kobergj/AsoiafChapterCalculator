import Models.storermodels as smod
import Models.gettermodels as gmod

import Getters.apigetters as apiget
import Getters.yamlgetters as yamlget

import Mappers.apimappers as apimap
import Mappers.yamlmappers as yamlmap

import QueryGenerators.insertqueries as insquery

import Connections.postgresconn as postgres

class DataTransfer:
    def __init__(self):
        self._gml = []
        self._sml = []
        self._qu = []

    def getmodels(self, getter, **getterargs):
        self._gml.extend(getter(**getterargs))

    def storemodels(self, mapper, querygenerator):
        self.mapmodels(mapper)

        self.genqueries(querygenerator)

    def mapmodels(self, mapper):
        for gettermodel in self._gml:
            self._sml.extend(mapper(gettermodel))

    def genqueries(self, querygenerator):
        while self._sml:
            storermodel = self._sml.pop()
            self._qu.append(querygenerator(storermodel))

    def commit(self, connection):
        while self._qu:
            query = self._qu.pop()
            connection(query)

def ApiCharToStaging(*pages):
    data = DataTransfer()

    for i in pages:
        data.getmodels(apiget.ApiCharacterGetter(gmod.Character), page=i)

    data.storemodels(apimap.CharacterMapper(smod.Character), insquery.InsertCharacter())

    data.storemodels(apimap.TitleMapperChar(smod.Possession), insquery.InsertPossession("Title"))

    data.storemodels(apimap.AliasMapper(smod.Possession), insquery.InsertPossession("Alias"))

    data.commit(postgres.StagingConnection("AsoiafDWH"))

def ApiHouseToStaging(*pages):
    data = DataTransfer()

    for i in pages:
        data.getmodels(apiget.ApiHouseGetter(gmod.House), page=i)

    data.storemodels(apimap.HouseMapper(smod.House), insquery.InsertHouse())

    data.storemodels(apimap.SeatMapper(smod.Possession), insquery.InsertPossession("Seat"))

    data.storemodels(apimap.TitleMapper(smod.Possession), insquery.InsertPossession("Title"))

    data.storemodels(apimap.WeaponMapper(smod.Possession), insquery.InsertPossession("Weapon"))

    data.commit(postgres.StagingConnection("AsoiafDWH"))

def ChapterNumbersToStaging(filepath):
    data = DataTransfer()

    data.getmodels(yamlget.YamlGetter(filepath))

    data.storemodels(yamlmap.ChapterMapper(smod.Chapter), insquery.InsertChapter())

    data.commit(postgres.StagingConnection("AsoiafDWH"))

def CharNChapterToStaging(filepath):
    data = DataTransfer()

    data.getmodels(yamlget.YamlGetter(filepath))

    data.storemodels(yamlmap.CharInChapterMapper(smod.CharInChapter), insquery.InsertCharInChapter())

    data.commit(postgres.StagingConnection("AsoiafDWH"))


if __name__=='__main__':
    # Chapter Numbers
    ChapterNumbersToStaging("/Users/Kokweazel/Documents/AsoiafYamls/chapternames.yaml")

    # Main Chars
    CharNChapterToStaging("/Users/Kokweazel/Documents/AsoiafYamls/maincharacters.yaml")

    # Characters
    ApiCharToStaging(*range(1, 50))

    # Houses
    ApiHouseToStaging(*range(1, 50))



