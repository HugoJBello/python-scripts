import requests
from pymongo import MongoClient
from idealista_entry_dto import IdealistaEntryDTO

class MongoConfigGrabber:

    def __init__(self):
        self.client = MongoClient('mongodb://freshkore:1234@ds231460.mlab.com:31460/real-state-db')
        self.db = self.client['real-state-db']
        self.scrapping_urls=[]
    
    def get_scrapping_urls(self):
        scrapping_config_collection=self.db.scrapping_config
        for url in scrapping_config_collection.find({}):
            self.scrapping_urls = self.scrapping_urls + [url["url"]]
        print (self.scrapping_urls)
        
