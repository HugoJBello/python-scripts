import asyncio
import logging
import requests
from models.avro_schema_helper import AvroSchemaHelper

class SchemaRegistry:
    def __init__(self, test_bed_options):

        self.topics = []
        self.fetched_schemas = []
        self.schema_available = False
        self.selected_topics = {"consume": test_bed_options.consume, "produce": test_bed_options.produce}
        self.fetch_all_versions = test_bed_options.fetch_all_versions
        self.schema_url = test_bed_options.schema_registry

        self.keys_schema = {}
        self.values_schema = {}
        self.schema_meta = {}

    def start_process(self):
        self.loop = asyncio.get_event_loop()
        is_schema_registry_available_task = self.loop.create_task(self.is_schema_registry_available())
        self.loop.run_until_complete(asyncio.wait([is_schema_registry_available_task]))

        if self.schema_available:
            fetch_all_schema_topics_task = self.loop.create_task(self.fetch_all_schema_topics())
            self.loop.run_until_complete(asyncio.wait([fetch_all_schema_topics_task]))

            fetch_schema_tasks =[]
            for topic in self.topics:
                fetch_schema_tasks.append(self.loop.create_task(self.fetch_schema(topic)))

            self.loop.run_until_complete(asyncio.wait(fetch_schema_tasks))


    async def is_schema_registry_available(self):
        url = self.schema_url
        logging.info("schema available")
        self.schema_available = True
        try:
            logging.info("checking schema in url :" + url)
            response = requests.get(url)
            self.schema_available = True
        except:
            logging.error("Error fetching url:" + url)
            self.schema_available = False

    async def fetch_all_schema_topics(self):
        fetch_all_schema_topics_url = self.schema_url + "/subjects"
        try:
            logging.info("Fetching all schemas using url:" + fetch_all_schema_topics_url)
            response = requests.get(fetch_all_schema_topics_url, headers={'Accept': 'application/vnd.schemaregistry.v1+json'})
            self.topics = response.json()
        except:
            logging.error("Error fetching all schemas using url:" + fetch_all_schema_topics_url)



    async def fetch_all_schema_versions(self, topic):
        fetch_all_versions_url = self.schema_url + '/subjects/' + topic + '/versions'
        try:
            logging.info("Fetching all schema versions using url:" + fetch_all_versions_url)
            response = requests.get(fetch_all_versions_url, headers={'Accept': 'application/vnd.schemaregistry.v1+json'})
            return response.json()
        except:
            logging.error("Error schema versions using url:" + fetch_all_versions_url)
            return None


    async def fetch_schema(self, topic):
        schema_topic_latest = await self.fetch_lastest_version(topic)
        topic = schema_topic_latest["topic"]
        version = schema_topic_latest["version"]
        parts = topic.split('-')
        schema_type = parts.pop()
        if not '-'.join(parts) is None:
            topic = '-'.join(parts)
        else:
            topic = schema_type

        fetch_schema_url = self.schema_url + "/subjects/" + schema_topic_latest["topic"] + "/versions/" + str(version)

        try:
            logging.info("Fetching schema using url:" + fetch_schema_url)
            response = requests.get(fetch_schema_url, headers={'Accept': 'application/vnd.schemaregistry.v1+json'})
            new_schema = {"version": version, "response_raw": response.json(), "schema_type": schema_type, "schema_topic_raw": topic, "topic": topic}
            new_schema= self.register_schema(new_schema)
            self.fetched_schemas.append(new_schema)
        except:
            logging.error("Error fetching latest schema using url:" + fetch_schema_url)

    async def fetch_lastest_version(self, topic):
        fetch_latest_versions_url = self.schema_url + '/subjects/' + topic + '/versions/latest'
        try:
            logging.info("Fetching latest schema versions using url:" + fetch_latest_versions_url)
            response = requests.get(fetch_latest_versions_url, headers={'Accept': 'application/vnd.schemaregistry.v1+json'})
            result = {"version": response.json()["version"], "topic": topic}
            return result
        except:
            logging.error("Error fetching latest schema using url:" + fetch_latest_versions_url)

    def register_schema(self, schema_topic):
        topic = schema_topic["topic"]
        logging.info("Registering schema " +  topic)
        avro_helper = AvroSchemaHelper(schema_topic["response_raw"]["schema"], topic)
        schema_topic["avro_helper"] = avro_helper

        item = {"avro_helper": schema_topic["avro_helper"], "sr_id": schema_topic["response_raw"]["id"]}
        if schema_topic["schema_type"].lower() == 'key':
            self.keys_schema[topic] = item
        else:
            self.values_schema[topic] = item
        self.schema_meta[topic] = schema_topic["response_raw"]

        return schema_topic




