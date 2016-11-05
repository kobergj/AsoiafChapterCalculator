
class CacheDB:
    def __init__(self):
        self.character = {None: None}
        self.house = {None: None}

class CacheConnection:
    def __init__(self, chargetter, housegetter):
        self._chars = SelfFillingDict(chargetter)
        self._houses = SelfFillingDict(housegetter)

    def get_character(self, Id):
        return self._chars.getset(Id)

    def get_house(self, Id):
        return self._houses.getset(Id)


class SelfFillingDict:
    def __init__(self, getter=None, startDict={None: None}):
        self._subdict = startDict

        if not getter:
            getter = (lambda x: None)

        self._getter = getter

    def getset(self, itemname):
        if itemname in self._subdict:
            return self._subdict[itemname]

        item = self._getter(itemname)

        self._subdict.update({itemname: item})
