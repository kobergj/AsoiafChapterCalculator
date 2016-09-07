import datetime

import Connections.postgresconn as conn
import QueryGenerators.instaging as qg

import initdb as source

DBNAME = 'AsoiafDWH'

def parseChapter(chapterinfo):
    valuedict = {}
    try:
        valuedict["charfirstname"], valuedict["charsurname"] = chapterinfo['Character'].split(' ')
    except ValueError:
        valuedict["charfirstname"] = chapterinfo['Character']
        valuedict["charsurname"] = ''

    valuedict["bookname"] = chapterinfo['BookName']

    valuedict["chaptername"] = chapterinfo['ChapterName']
    valuedict["chapternumber"] = chapterinfo['ChapterId']

    return valuedict



class ChapterToStaging:
    def __init__(self, uid=None, pwd=None):
        self.connection = conn.StagingConnection(DBNAME, uid, pwd)
        self.querygenerator = qg.StagingLoader("charinchapter")

    def __call__(self, cinfo):
        for chapterinfo in cinfo['OccurenceList']:
            values = parseChapter(chapterinfo)
            query = self.querygenerator(insertiontime=datetime.datetime.now(), **values)

            self.connection(query)

            # try:
            #     firstname, surname = chapterinfo['Character'].split(' ')
            # except ValueError:
            #     firstname = chapterinfo['Character']
            #     surname = ''

            # char = qg.Character(firstname, surname)

            # charid = con(char)

            # chap = qg.Chapter(chapterinfo['ChapterName'], bookid, charid, chapterinfo['ChapterId'])

            # con(chap)

if __name__ == '__main__':
    # uid, pwd = sys.argv[1:3]
    dest = ChapterToStaging() #uid, pwd)

    for _, info in source.db.info.iteritems():
        dest(info)


