# TODO: Move to config
QUERYTEMPLATE = """
        INSERT INTO %(tablename)s (name)
        SELECT '%(name)s'
        WHERE NOT EXISTS (
            SELECT 1 
            FROM %(tablename)s tb 
            WHERE tb.name = '%(name)s'
        );

        SELECT id 
        FROM %(tablename)s
        WHERE name = '%(name)s'
        """

CHAPTERQUERYTEMPLATE = """
        INSERT INTO %(tablename)s (name, bookid, characterid, chapternumber)
        SELECT '%(name)s', '%(bookid)s', '%(characterid)s', '%(chapternumber)s'
        WHERE NOT EXISTS (
            SELECT 1 
            FROM %(tablename)s tb 
            WHERE tb.name = '%(name)s'
              AND tb.bookid = %(bookid)s
              AND tb.chapternumber = %(chapternumber)s
        );

        SELECT 1
        """

class Querygenerator:
    def __call__(self):
        query =  QUERYTEMPLATE % {'tablename': self.tablename, 'name': self.name}

        return query

class Book(Querygenerator):
    def __init__(self, bname):
        self.name = bname

        self.tablename = 'dbo.D_Book'


class Character(Querygenerator):
    def __init__(self, cname):
        self.name = cname

        self.tablename = 'dbo.D_Character'

class Chapter(Querygenerator):
    def __init__(self, cname, bid, cid, cnum):
        self.name = cname
        self.bookid = bid
        self.charid = cid
        self.chapnum = cnum

        self.tablename = 'dbo.F_Chapter'

    def __call__(self):
        query =  CHAPTERQUERYTEMPLATE % {'tablename': self.tablename, 
                                         'name': self.name,
                                         'bookid': self.bookid,
                                         'characterid': self.charid,
                                         'chapternumber': self.chapnum}

        return query

