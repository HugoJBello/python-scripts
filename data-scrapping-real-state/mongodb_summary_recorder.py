import requests
from pymongo import MongoClient
from idealista_entry_dto import IdealistaEntryDTO

class MongoDBSummaryRecorder:

    def __init__(self, summary):
        self.summary = summary
        self.client = MongoClient('mongodb://freshkore:1234@ds231460.mlab.com:31460/real-state-db')
        self.db = self.client['real-state-db']
    
    def post_data(self):
        summary_collection=self.db.summary
        dto_mongodb=self.summary.__dict__
        summary_collection.save(dto_mongodb)
