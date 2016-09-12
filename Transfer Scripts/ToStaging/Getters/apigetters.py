import anapioficeandfire

import basicgetters as bsc

class ApiCharacterGetter(bsc.BasicGetter):
    def _connect(self):
        return anapioficeandfire.API().get_characters
