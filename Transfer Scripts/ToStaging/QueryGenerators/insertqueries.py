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
        keydict = {
            "firstname": charactermodel.firstname,
            "surname": charactermodel.surname,
            "culture": charactermodel.culture,
            "fatherfirst": charactermodel.fatherfirst,
            "fathersur": charactermodel.fathersur,
            "motherfirst": charactermodel.motherfirst,
            "mothersur": charactermodel.mothersur,
            "spousefirst": charactermodel.spousefirst,
            "spousesur": charactermodel.spousesur,
            'insertiontime': datetime.datetime.now()
            }

        if charactermodel.gender:
            keydict.update({"gender": charactermodel.gender})
        
        if charactermodel.born:
            keydict.update({"born": charactermodel.born})

        if charactermodel.died:
            keydict.update({"died": charactermodel.died})

        return keydict