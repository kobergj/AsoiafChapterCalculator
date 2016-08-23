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

CHARACTERQUERYTEMPLATE = """
        /*INSERT INTO dbo.D_Character (firstname, surname, gender, yearofbirth, yearofdeath)
        SELECT '%(firstname)s', '%(surname)s', '%(gender)s', '%(born)s', '%(died)s'
        WHERE NOT EXISTS (
            SELECT 1 
            FROM dbo.D_Character ch
            WHERE ch.firstname = '%(firstname)s'
              AND ch.surname = '%(surname)s'
        );
        */
        UPDATE dbo.D_Character ch
            SET
                gender = '%(gender)s'
                , yearofbirth = %(born)i
                , yearofdeath = %(died)i
            
            WHERE ch.firstname = '%(firstname)s'
              AND ch.surname = '%(surname)s'

            RETURNING ch.id;
        /*
        SELECT id 
        FROM dbo.D_Character
        WHERE firstname = '%(firstname)s'
          AND surname = '%(surname)s'
        */
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
    tablename = 'dbo.D_Book'

    def __init__(self, bname):
        self.name = bname


class Character(Querygenerator):
    def __init__(self, firstname, surname, gender='', born=0, died=0):
        self.firstname = firstname
        self.surname = surname

        self.gender = gender

        self.born = int(born) if born else 0
        self.died = int(died) if died else 0

    def __call__(self):
        query = CHARACTERQUERYTEMPLATE % {'firstname': self.firstname,
                                          'surname': self.surname,
                                          'gender': self.gender,
                                          'born': self.born,
                                          'died': self.died
                                          }

        return query



class Chapter(Querygenerator):
    tablename = 'dbo.F_Chapter'

    def __init__(self, cname, bid, cid, cnum):
        self.name = cname
        self.bookid = bid
        self.charid = cid
        self.chapnum = cnum

    def __call__(self):
        query =  CHAPTERQUERYTEMPLATE % {'tablename': self.tablename, 
                                         'name': self.name,
                                         'bookid': self.bookid,
                                         'characterid': self.charid,
                                         'chapternumber': self.chapnum}

        return query

