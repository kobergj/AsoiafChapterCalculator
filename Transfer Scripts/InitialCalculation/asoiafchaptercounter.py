import chapter_counter as cc

FILENAME = 'asoiafchapters.txt'

CHAPTERSEPERATOR = '\n'
BOOKSEPERATOR = '--------'

BOOKNAMES = ['GameOfThrones', 'ClashOfKings', 'StormOfSwords', 'FeastForCrows', 'DanceWithDragons']

CHAPTERALIASES = {
    'The Iron Captain': 'Victarion',
    'Alayne': 'Sansa',
    'Reek': 'Theon',
    "The Kraken's Daughter": 'Asha',
    'The Drowned Man': 'Aeron',
    'The Prophet': 'Aeron',
    'The Reaver': 'Victarion',
    'The Soiled Knight': 'Arys',
    'The Captain Of Guards': 'Areo',
    'The Queenmaker': 'Arianne',
    'The Princess In The Tower': 'Arianne',
    'Cat Of The Canals': 'Arya',
    'The Windblown': 'Quentyn',
    'The Blind Girl': 'Arya',
    "The Queen's Hand": 'Barristan',
    'The Iron Suitor': 'Victarion',
    'The Wayward Bride': 'Asha',
    'The Prince of Winterfell': 'Theon',
    'The Dragontamer': 'Quentyn',
    "The King's Prize": 'Asha',
    'A Ghost in Winterfell': 'Theon',
    'The Queensguard': 'Barristan',
    'The Watcher': 'Areo',
    "The Merchant's Man": 'Quentyn',
    'The Griffin Reborn': 'Jon Connington',
    'The Kingbreaker': 'Barristan',
    'The Sacrifice': 'Asha',
    'The Ugly Little Girl': 'Arya',
    'The Discarded Knight': 'Barristan',
    'The Lost Lord': 'Jon Connington',
    'The Turncloak': 'Theon',
    'The Spurned Suitor': 'Quentyn'
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
