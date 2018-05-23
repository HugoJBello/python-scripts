from datetime import datetime
class IdealistaEntryDTO:

    def __init__(self, title,prize,meters,rooms,url_scrapped,url_element):
        self.rooms = rooms
        self.title = title
        self.prize = prize
        self.meters = meters
        self.url_scrapped=url_scrapped
        self.url_element=url_element
        self.date = str(datetime.now())

        self.construct_id()

    def construct_id(self):
        self._id = self.title + "---" + self.meters+"---" + self.rooms