
class CharInChapter:
    def __init__(self, charfirstname, charsurname, chaptername):
        self.charfirstname = charfirstname
        self.charsurname = charsurname
        self.chaptername = chaptername

class Chapter:
    def __init__(self, chaptername, chapternumber, bookname):
        self.name = chaptername
        self.number = chapternumber
        self.bookname = bookname

class Character:
    def __init__(self, first, sur, gender, born, died, culture, fatherfirst,
            fathersur, motherfirst, mothersur, spousefirst, spousesur):
        self.firstname = first
        self.surname = sur

        self.gender = gender
        self.born = born
        self.died = died

        self.culture = culture

        self.fatherfirst = fatherfirst
        self.fathersur = fathersur

        self.motherfirst = motherfirst
        self.mothersur = mothersur

        self.spousefirst = spousefirst
        self.spousesur = spousesur
