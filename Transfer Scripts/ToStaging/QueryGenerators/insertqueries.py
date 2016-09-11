import datetime

import sqlbuilder.smartsql as sql

class InsertQuery:
    def __init__(self, tablename):
        self.tablename = tablename

    def __call__(self, **kwargs):
        stagingtable = sql.T(self.tablename)

        query = sql.Q().tables(stagingtable)

        kwargs.update({'insertiontime': datetime.datetime.now()})

        query = query.insert(kwargs,)

        return query

    def generate_kwargs(self, *args):
        return


class InsertChapter(InsertQuery):
    def __init__(self):
        InsertQuery.__init__(self, "charinchapter")

    def generate_kwargs(charfirst, charsur, chapname, chapnum, bname):
        return {
            "charfirstname": charfirst,
            "charsurname": charsur,
            "chaptername": chapname,
            "chapternumber": chapnum,
            "bookname": bname
        }