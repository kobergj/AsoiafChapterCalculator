import chapter_counter as cc

FILENAME = 'ChapterCalculator/asoiafchapters.txt'

CHAPTERSEPERATOR = '\n'
BOOKSEPERATOR = '--------'

BOOKNAMES = ['GameOfThrones', 'ClashOfKings', 'StormOfSwords', 'FeastForCrows', 'DanceWithDragons']

CHAPTERALIASES = {
    'The Iron Captain': 'Victarion Greyjoy',
    'Alayne': 'Sansa Stark',
    'Reek': 'Theon Greyjoy',
    "The Krakens Daughter": 'Asha Greyjoy',
    'The Drowned Man': 'Aeron Greyjoy',
    'The Prophet': 'Aeron Greyjoy',
    'The Reaver': 'Victarion Greyjoy',
    'The Soiled Knight': 'Arys Oakheart',
    'The Captain Of Guards': 'Areo Hotah',
    'The Queenmaker': 'Arianne Martell',
    'The Princess In The Tower': 'Arianne Martell',
    'Cat Of The Canals': 'Arya Stark',
    'The Windblown': 'Quentyn Martell',
    'The Blind Girl': 'Arya Stark',
    "The Queens Hand": 'Barristan Selmy',
    'The Iron Suitor': 'Victarion Greyjoy',
    'The Wayward Bride': 'Asha Greyjoy',
    'The Prince of Winterfell': 'Theon Greyjoy',
    'The Dragontamer': 'Quentyn Martell',
    "The Kings Prize": 'Asha Greyjoy',
    'A Ghost in Winterfell': 'Theon Greyjoy',
    'The Queensguard': 'Barristan Selmy',
    'The Watcher': 'Areo Hotah',
    "The Merchants Man": 'Quentyn Martell',
    'The Griffin Reborn': 'Jon Connington',
    'The Kingbreaker': 'Barristan Selmy',
    'The Sacrifice': 'Asha Greyjoy',
    'The Ugly Little Girl': 'Arya Stark',
    'The Discarded Knight': 'Barristan Selmy',
    'The Lost Lord': 'Jon Connington',
    'The Turncloak': 'Theon Greyjoy',
    'The Spurned Suitor': 'Quentyn Martell'
    }

PASSWORD = 'WinterIsHere'

def get_access(password):
    if password == PASSWORD:
        return cc.ChapterInformationAccess(
                filename=FILENAME,
                csep=CHAPTERSEPERATOR,
                bsep=BOOKSEPERATOR,
                bnames=BOOKNAMES,
                calias=CHAPTERALIASES
                )

    return 'Wrong Password, Sorry...'
