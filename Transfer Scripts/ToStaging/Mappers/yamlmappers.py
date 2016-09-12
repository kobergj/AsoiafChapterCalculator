
def mapChapters(bookdict):
    values = []

    for bookname, chapterlist in bookdict.iteritems():

        for i, chaptername in enumerate(chapterlist):
            values.append([chaptername, i, bookname])

    return values

def mapCharInChapter(chardict):
    values = []

    for chap, [charfirst, charsur] in chardict.iteritems():
        values.append([chap, charfirst, charsur])

    return values
