from datetime import datetime
class RealStateEntryDTO:

    def __init__(self, title,prize,meters,rooms,url_scrapped,url_element,url_first_page):
        self.rooms = rooms
        self.title = title
        self.prize = prize
        self.meters = meters
        self.url_scrapped=url_scrapped
        self.url_element=url_element
        self.url_first_page=url_first_page
        self.date = str(datetime.now())

        self.construct_id()

    def construct_id(self):
        self._id = self.title + "---" + self.meters+"---" + self.rooms+"---"+self.prize