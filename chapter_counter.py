
class FileReader:
    def __init__(self, ch_sep, bk_sep):
        self.csep = ch_sep
        self.bsep = bk_sep

    def __call__(self, longstring):
        books = longstring.split(self.bsep)

        book_list = []

        for book in books:
            chap_list = []

            chptrs = book.split(self.csep)

            for ch in chptrs:
                if ch:
                    chap_list.append(ch)

            book_list.append(chap_list)

        return book_list

class ItemCounter:
    def __init__(self, bk_nms, calias={}):
        self.bnames = bk_nms

        self.calias = calias

    def __call__(self, booklist):
        if len(self.bnames) != len(booklist):
            print 'Booknames len does not equal book len'
            quit()

        complete_chapter_info = {}

        for i, bname in enumerate(self.bnames):

            for j, cname in enumerate(booklist[i]):

                c_id = bname + str(j)

                if cname in self.calias:
                    cname = self.calias[cname]

                if cname in complete_chapter_info:
                    cinfos = complete_chapter_info[cname]

                    cinfos['OccurenceList'].append(c_id)

                    occurences = cinfos['Occurences']

                    occurences['Overall'] += 1

                    if bname in occurences:
                        occurences[bname] += 1
                    else:
                        occurences.update({bname: 1})


                else:
                    cinfos = {
                        'Occurences': {
                            'Overall': 1,
                            bname: 1,
                            },
                        'OccurenceList': [c_id]
                        }

                    complete_chapter_info.update({cname: cinfos})

        return complete_chapter_info


class ChapterCounter:
    def __init__(self, csep, bsep, bnames, calias):
        self.filereader = FileReader(csep, bsep)

        self.itemcounter = ItemCounter(bnames, calias)

    def __call__(self, filename):
        with open(filename) as file:
            fileasstring = file.read()

        books = self.filereader(fileasstring)

        counted_chapters = self.itemcounter(books)

        return counted_chapters


class ChapterInformationAccess:
    def __init__(self, filename, csep, bsep, bnames, calias):
        cnt = ChapterCounter(csep, bsep, bnames, calias)

        self.info = cnt(filename)

        self.bnames = bnames

    def chaptertostring(self, ch_name, overall=True, books='All', details=False):
        if books == 'All':
            books = self.bnames

        cinfo = self.info[ch_name]

        pr_str = ch_name + ':\n'

        occ_info = cinfo['Occurences']

        pr_str += '    '

        if overall:
            pr_str += 'Overall' + ' ' + str(occ_info['Overall']) + ' -- '

        for occ_id, occ in occ_info.iteritems():

            if occ_id in books:
                pr_str += occ_id + ' ' + str(occ) + ' -- '

        if details:
            pr_str += '\n'

            pr_str += '    '

            det_occs = cinfo['OccurenceList']

            for d in det_occs:
                pr_str += d + ' -- '

        return pr_str

    def printchapters(self, chapters, sortkey=None, desc=True, limit=False, **printdetails):

        if sortkey:
            not_there = []

            def sortfunc(chapname):
                # Should return value to compare i guess
                occurence_info = self.info[chapname]['Occurences']

                if sortkey in occurence_info:
                    return occurence_info[sortkey]

                not_there.append(chapname)
                return None

            chapters = sorted(chapters, key=sortfunc, reverse=desc)

            chapters = [chap for chap in chapters if chap not in not_there]

        if limit:
            chapters = chapters[:limit]

        for cname in chapters:
            print self.chaptertostring(cname, **printdetails)

    def printsome(self, sortkey=None, size=5, head=True, **printdetails):
        allchaps = self.info.keys()

        self.printchapters(allchaps, sortkey=sortkey, limit=size, desc=head, **printdetails)


