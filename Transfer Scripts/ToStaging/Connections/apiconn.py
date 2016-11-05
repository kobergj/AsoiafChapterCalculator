import anapioficeandfire

class CachedApiConnection:
    def __init__(self):
        api = ApiConnection()

        self._chargetter = CachedGetter(ApiObjectCache(), api.get_character, api.get_characters)
        self._housegetter = CachedGetter(ApiObjectCache(), api.get_house, api.get_houses)

    def getcharpage(self, page):
        return self._chargetter(page=page)

    def gethousepage(self, page):
        return self._housegetter(page=page)

    def geturl(self, url):
        if not url:
            return

        splittedurl = url.split('/')

        if splittedurl[-2] == 'characters':
            return self._chargetter(url=url)

        if splittedurl[-2] == 'houses':
            return self._housegetter(url=url)

    def getkeypage(self, page, key):
        if key == 'characters':
            return self.getcharpage(page=page)

        if key == 'houses':
            return self.gethousepage(page=page)

class CachedGetter:
    def __init__(self, cache, getone, getmany):
        self._cache = cache
        self._getone = getone
        self._getmany = getmany

    def __call__(self, url=None, page=None):
        if page:
            apiobjects = self._getmany(page=page)
            self._cache.setmany(apiobjects)
            return apiobjects

        if self._cache.contains(url):
            return self._cache.get(url)

        apiobject = self._getone(url)
        self._cache.set(apiobject)
        return apiobject

class ApiConnection:
    def __init__(self):
        self._conn = anapioficeandfire.API()

    def get_characters(self, page):
        return self._conn.get_characters(page=page)

    def get_character(self, url):
        Id = self.extractId(url)
        return self._conn.get_character(id=Id)

    def get_houses(self, page):
        return self._conn.get_houses(page=page)

    def get_house(self, url):
        Id = self.extractId(url)
        return self._conn.get_house(id=Id)

    # Difficult. Don't like parsing Data at this Point - But needed for querying Api
    def extractId(self, url):
        if url:
            return int(''.join(i for i in url if i.isdigit()))

class ApiObjectCache:
    def __init__(self, startdict={None: None}):
        self._dict = startdict

    def get(self, key):
        if key in self._dict:
            return self._dict[key]

    def set(self, apiobject):
        url = apiobject.url
        if url not in self._dict:
            self._dict.update({url: apiobject})

    def setmany(self, apiobjects):
        for apiobject in apiobjects:
            self.set(apiobject)

    def contains(self, key):
        return key in self._dict

