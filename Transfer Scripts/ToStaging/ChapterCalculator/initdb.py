import asoiafchaptercounter as ac

GOT = 'GameOfThrones'
COK = 'ClashOfKings'
SOS = 'StormOfSwords'
FFC = 'FeastForCrows'
DWD = 'DanceWithDragons'

OVERALL = 'Overall'


db = ac.get_access('WinterIsHere')


if __name__ == '__main__':
    book = DWD
    db.printsome(OVERALL, size=5)
