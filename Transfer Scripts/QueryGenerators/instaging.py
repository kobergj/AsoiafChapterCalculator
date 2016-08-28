import sqlbuilder.smartsql as sql

class StagingLoader:
    def __init__(self, tablename):
        self.tablename = tablename

    def __call__(self, **kwargs):
        stagingtable = sql.T(self.tablename)

        query = sql.Q().tables(stagingtable)

        query = query.insert(kwargs,)

        return query

# class Character:
#     def __init__(self, firstname, surname, gender, born, died):
#         self.stloader = StagingLoader("character")

#         self.valdict = {
            
#         }

#     def __call__(self)
