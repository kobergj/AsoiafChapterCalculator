
import Getters.apigetters as apiget
import Mappers.apimappers as apimap
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

        for document in page:
            values = self.mapper(document)

            query = self.querygenerator(**values)

            self.connection(query)

        return True

def TransferCharactersFromApi(*pages):
    etl = DataTransfer(getter=apiget.ApiCharacterGetter(), 
                        mapper=apimap.mapCharacter,
                        querygenerator=insquery.InsertQuery("character"),
                        connection=postgres.StagingConnection("AsoiafDWH")
                        )

    for i in pages:
        etl(page=i)

if __name__=='__main__':
    TransferCharactersFromApi(1,2,3,4,5,6,7,8)
