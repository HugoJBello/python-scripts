from datetime import datetime
class IdealistaEntryDTO:

    def __init__(self, title,prize,meters,rooms):
        self.rooms = rooms
        self.title = title
        self.prize = prize
        self.meters = meters
        self.date = str(datetime.now())