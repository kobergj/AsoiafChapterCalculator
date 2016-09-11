import datetime

import sqlbuilder.smartsql as sql

class InsertQuery:
    def __init__(self, tablename):
        self.tablename = tablename

    def __call__(self, *args):
        stagingtable = sql.T(self.tablename)

        query = sql.Q().tables(stagingtable)

        kwargs = self.generate_kwargs(*args)

        query = query.insert(kwargs,)

        return query

    def generate_kwargs(self, *args):
        return


class InsertCharInChapter(InsertQuery):
    def __init__(self):
        InsertQuery.__init__(self, "charinchapter")

    def generate_kwargs(self, chapname, charfirst, charsur):
        return {
            "charfirstname": charfirst,
            "charsurname": charsur,
            "chapname": chapname,
            'insertiontime': datetime.datetime.now()
        }

class InsertChapter(InsertQuery):
    def __init__(self):
        InsertQuery.__init__(self, "chapter")

    def generate_kwargs(self, chapname, chapnum, bname):
        return {
            "chaptername": chapname,
            "chapternumber": chapnum,
            "bookname": bname,
            'insertiontime': datetime.datetime.now()
        }

class InsertCharacter(InsertQuery):
    def __init__(self):
        InsertQuery.__init__(self, "character")

    def generate_kwargs(self, charfirst, charsur, gender, born, died):
        keydict = {
            "firstname": charfirst,
            "surname": charsur,
            'insertiontime': datetime.datetime.now()
            }

        if gender:
            keydict.update({"gender": gender})
        
        if born:
            keydict.update({"born": born})

        if died:
            keydict.update({"died": died})

        return keydict