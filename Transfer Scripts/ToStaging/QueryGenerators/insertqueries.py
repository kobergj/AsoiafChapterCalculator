import datetime

import sqlbuilder.smartsql as sql

class InsertQuery:
    def __init__(self, tablename):
        self.tablename = tablename

    def __call__(self, *args):
        insert_table = sql.T(self.tablename)

        query = sql.Q().tables(insert_table)

        colnames = self.add_column_names(*args)

        insertquery = query.insert(colnames,)

        return insertquery

    def add_column_names(self, *args):
        return


class InsertCharInChapter(InsertQuery):
    def __init__(self):
        InsertQuery.__init__(self, "charinchapter")

    def add_column_names(self, charinchapmodel):
        return {
            "charfirstname": charinchapmodel.charfirstname,
            "charsurname": charinchapmodel.charsurname,
            "chapname": charinchapmodel.chaptername,

            'insertiontime': datetime.datetime.now()
        }

class InsertChapter(InsertQuery):
    def __init__(self):
        InsertQuery.__init__(self, "chapter")

    def add_column_names(self, chaptermodel):
        return {
            "chaptername": chaptermodel.name,
            "chapternumber": chaptermodel.number,
            "bookname": chaptermodel.bookname,

            'insertiontime': datetime.datetime.now()
        }

class InsertCharacter(InsertQuery):
    def __init__(self):
        InsertQuery.__init__(self, "character")

    def add_column_names(self, charactermodel):
        return {
            "firstname": charactermodel.firstname,
            "surname": charactermodel.surname,
            "culture": charactermodel.culture,
            "fatherfirst": charactermodel.fatherfirst,
            "fathersur": charactermodel.fathersur,
            "motherfirst": charactermodel.motherfirst,
            "mothersur": charactermodel.mothersur,
            "spousefirst": charactermodel.spousefirst,
            "spousesur": charactermodel.spousesur,
            "gender": charactermodel.gender,
            "born": charactermodel.born,
            "died": charactermodel.died,

            'insertiontime': datetime.datetime.now()
            }

class InsertHouse(InsertQuery):
    def __init__(self):
        InsertQuery.__init__(self, "house")

    def add_column_names(self, housemodel):
        return {
            "name": housemodel.name,
            "branch": housemodel.seat,
            "founderfirst": housemodel.founderfirst,
            "foundersur": housemodel.foundersur,
            "heirfirst": housemodel.heirfirst,
            "heirsur": housemodel.heirsur,
            "lordfirst": housemodel.lordfirst,
            "lordsur": housemodel.lordsur,
            "overlord": housemodel.overlord,
            "overlordbranch": housemodel.overlordseat,
            "region": housemodel.region,
            "founded": housemodel.founded,
            "diedout": housemodel.diedout,
            "words": housemodel.words,
            "coatofarms": housemodel.coatofarms,

            'insertiontime': datetime.datetime.now()
            }

class InsertPossession(InsertQuery):
    def __init__(self, postype):
        InsertQuery.__init__(self, "possession")

        self.postype = postype

    def add_column_names(self, possessionmodel):
        return {
            "description": possessionmodel.description,

            "possessiontype": self.postype,

            "house": possessionmodel.house,
            "branch": possessionmodel.branch,

            "charfirst": possessionmodel.charfirst,
            "charsur": possessionmodel.charsur,

            'insertiontime': datetime.datetime.now()
        }

class InsertCharHouseRelation(InsertQuery):
    def __init__(self, reltype):
        InsertQuery.__init__(self, "charhouserelation")

        self.reltype = reltype

    def add_column_names(self, charhousemodel):
        return {
            "first": charhousemodel.first,
            "sur": charhousemodel.sur,

            "relationtype": self.reltype,

            "house": charhousemodel.house,
            "branch": charhousemodel.branch,

            'insertiontime': datetime.datetime.now()
        }

class InsertCadetBranches(InsertQuery):
    def __init__(self):
        InsertQuery.__init__(self, "cadetbranches")

    def add_column_names(self, cadetbranchmodel):
            return {
                "master": cadetbranchmodel.master,
                "masterbranch": cadetbranchmodel.masterbranch,

                "cadet": cadetbranchmodel.cadet,
                "cadetbranch": cadetbranchmodel.cadetbranch,

                'insertiontime': datetime.datetime.now()
            }

