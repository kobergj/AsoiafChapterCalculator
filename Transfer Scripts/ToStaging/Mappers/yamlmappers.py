import basicmappers as bsc

class ChapterMapper(bsc.Mapper):
    def __call__(self, bookdict):
        model_list = []

        for bookname, chapterlist in bookdict.iteritems():

            for i, chaptername in enumerate(chapterlist):
                model_list.append(self.outmodel(chaptername, i, bookname))

        return model_list


class CharInChapterMapper(bsc.Mapper):
    def __call__(self, chardict):

        model_list = []

        for chap, [charfirst, charsur] in chardict.iteritems():
            charinchap = self.outmodel(charfirst, charsur, chap)
            model_list.append(charinchap)

        return model_list
