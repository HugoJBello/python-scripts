from datetime import datetime
class IdealistaEntryDTO:

    def __init__(self, title,prize,meters,rooms,url):
        self.rooms = rooms
        self.title = title
        self.prize = prize
        self.meters = meters
        self.date = str(datetime.now())
        self.url_scrapped = url