import requests
import sys
from pymongo import MongoClient

class MongoDBDataRecorder:

    def __init__(self):
        self.client = MongoClient('mongodb://freshkore:freshkore1234@ds161620.mlab.com:61620/pod3c-backup')
        self.db = self.client['pod3c-backup']
    
    def post_data(self,dto):
        collection=self.db.entriespod3c
        print("saving " + dto["title"])
        collection.save(dto)
