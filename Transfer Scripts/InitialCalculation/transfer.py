import sys

import Connections.postgresconn as conn
import QueryGenerators.querygenerators as qg

import initdb as source

DBNAME = 'AsoiafDWH'

class CharacterToDatabase:
    def __init__(self, uid, pwd):
        self.connection = conn.Connection(DBNAME, uid, pwd)

    def __call__(self, cinfo):
        con = self.connection

        for chapterinfo in cinfo['OccurenceList']:
            book = qg.Book(chapterinfo['BookName'])

            bookid = con(book)

            try:
                firstname, surname = chapterinfo['Character'].split(' ')
            except ValueError:
                firstname = chapterinfo['Character']
                surname = ''

            char = qg.Character(firstname, surname)

            charid = con(char)

            chap = qg.Chapter(chapterinfo['ChapterName'], bookid, charid, chapterinfo['ChapterId'])

            con(chap)

if __name__ == '__main__':
    uid, pwd = sys.argv[1:3]
    dest = CharacterToDatabase(uid, pwd)

    for _, info in source.db.info.iteritems():
        dest(info)


