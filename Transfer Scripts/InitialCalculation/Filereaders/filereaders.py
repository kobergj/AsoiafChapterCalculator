# import yaml

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename)

    def readtxt(self, bsep, csep):
        txtstring = self.file.read()
        books = txtstring.split(bsep)

        book_list = []

        for book in books:
            chap_list = []

            chptrs = book.split(csep)

            for ch in chptrs:
                if ch:
                    chap_list.append(ch)

            book_list.append(chap_list)

        return book_list

    def __exit__(self, type, value, tb):
        self.file.close()
