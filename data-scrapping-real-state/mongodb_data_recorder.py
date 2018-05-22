import requests
from pymongo import MongoClient
from idealista_entry_dto import IdealistaEntryDTO

class MongoDBDataRecorder:

    def __init__(self, dto_dictionary):
        self.dto_dictionary = dto_dictionary
        self.client = MongoClient('mongodb://freshkore:1234@ds231460.mlab.com:31460/real-state-db')
        self.db = self.client['real-state-db']
    
    def post_data(self):
        print(self.dto_dictionary)
        scrapped_data_collection=self.db.scrapped
        for key, dto in self.dto_dictionary.items():
            dto_mongodb=dto.__dict__
            dto_mongodb["_id"] = self.construct_id(dto)
            scrapped_data_collection.save(dto_mongodb)
        

    def construct_id(self,dto):
        return dto.title + "---" + dto.meters+"---" + dto.rooms