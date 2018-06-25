import requests
import asyncio
from test_bed_options import TestBedOptions
class SchemaRegistry:
    def __init__(self, test_bed_options):

        self.test_bed_options = test_bed_options
        self.schema_topics = []
        self.selected_topics ={consume:self.test_bed_options.consume, produce:self.test_bed_options.produce}

                
    async def is_schema_registry_available(self):
        url = self.test_bed_options.schema_registry
        try:
            response = await requests.get(url).json()
            print("schema available")
        except:
            print("error fetching schema on url " + url)


    async def fetch_all_schema_versions(self,schema_topic):
        fetch_all_versions_url = self.test_bed_options.schema_registry + '/subjects/' + schema_topic + '/versions'
        response=None
        try:
            print("Fetching all schema versions using url:" + fetch_all_topics_url)
            response = await requests.get(fetch_all_topics_url, headers={'Accept':'application/vnd.schemaregistry.v1+json'}).json()
        except:
            print("Error schema versions using url:" + fetch_all_topics_url)  
        return response.data

    async def fetch_lastest_version(self,schema_topic):
        fetch_lastest_versions_url = self.test_bed_options.schema_registry + '/subjects/' + schema_topic + '/versions/lastest'
        response=None
        try:
            print("Fetching lastest schema versions using url:" + fetch_lastest_versions_url)
            response = await requests.get(fetch_lastest_versions_url, headers={'Accept':'application/vnd.schemaregistry.v1+json'}).json()
        except:
            print("Error fetching lastest schema using url:" + fetch_lastest_versions_url) 
        result = {"version": response.data.version,"schema_topic": schema_topic} 
        return response.data


    async def fetch_all_schema_topics(self):
        fetch_all_schema_topics_url = self.test_bed_options.schema_registry + "/subjects"
        response=None
        try:
            print("Fetching all schemas using url:" + fetch_all_schema_topics_url)
            response = await requests.get(fetch_all_schema_topics_url).json()
        except:
            print("Error fetching all schemas using url:" + fetch_all_schema_topics_url)  
        return response.data

    



