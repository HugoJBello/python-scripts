import requests
import asyncio

class SchemaRegistry:
    def __init__(self, test_bed_options):

        self.topics = []
        self.fetched_schemas = []
        self.schema_available = False
        self.selected_topics = {"consume": test_bed_options.consume, "produce": test_bed_options.produce}
        self.fetch_all_versions = test_bed_options.fetch_all_versions
        self.schema_url = test_bed_options.schema_registry

    def start_process(self):
        self.loop = asyncio.get_event_loop()
        is_schema_registry_available_task = self.loop.create_task(self.is_schema_registry_available())
        self.loop.run_until_complete(asyncio.wait([is_schema_registry_available_task]))

        if self.schema_available:
            fetch_all_schema_topics_task = self.loop.create_task(self.fetch_all_schema_topics())
            self.loop.run_until_complete(asyncio.wait([fetch_all_schema_topics_task]))

            fetch_topic_tasks =[]
            for topic in self.topics:
                fetch_topic_tasks.append(self.loop.create_task(self.fetch_schema(topic)))

            self.loop.run_until_complete(asyncio.wait(fetch_topic_tasks))


    async def is_schema_registry_available(self):
        url = self.schema_url
        print("schema available")
        self.schema_available = True
        try:
            print("checking schema in url :" + url)
            response = requests.get(url)
            self.schema_available = True
        except:
            print("Error fetching url:" + url)
            self.schema_available = False

    async def fetch_all_schema_topics(self):
        fetch_all_schema_topics_url = self.schema_url + "/subjects"
        try:
            print("Fetching all schemas using url:" + fetch_all_schema_topics_url)
            response = requests.get(fetch_all_schema_topics_url)
            self.topics = response.json()
        except:
            print("Error fetching all schemas using url:" + fetch_all_schema_topics_url)  



    async def fetch_all_schema_versions(self, topic):
        fetch_all_versions_url = self.schema_url + '/subjects/' + topic + '/versions'
        try:
            print("Fetching all schema versions using url:" + fetch_all_versions_url)
            response = requests.get(fetch_all_versions_url, header={'Accept': 'application/vnd.schemaregistry.v1+json'})
            return response.json()
        except:
            print("Error schema versions using url:" + fetch_all_versions_url)
            return None


    async def fetch_schema(self, topic):
        schema_topic = await self.fetch_lastest_version(topic)
        topic = schema_topic["topic"]
        version = schema_topic["version"]
        parts = topic.split('-')
        schema_type = parts.pop() 
        if not '-'.join(parts) is None:
            topic = '-'.join(parts)
        else:
            topic = schema_type

        fetch_schema_url = self.schema_url + "/subjects/" + topic + "/versions/" + str(version)

        try:
            print("Fetching schema using url:" + fetch_schema_url)
            response = requests.get(fetch_schema_url, headers={'Accept': 'application/vnd.schemaregistry.v1+json'})
            self.fetched_schemas.append({"version": version, "response_raw": response.json(), "schema_type": schema_type, "schema_topic_raw": schema_topic, "topic": topic})
        except:
            print("Error fetching latest schema using url:" + fetch_schema_url)

    async def fetch_lastest_version(self, topic):
        fetch_latest_versions_url = self.schema_url + '/subjects/' + topic + '/versions/latest'
        try:
            print("Fetching latest schema versions using url:" + fetch_latest_versions_url)
            response = requests.get(fetch_latest_versions_url, headers={'Accept': 'application/vnd.schemaregistry.v1+json'})
            result = {"version": response.json()["version"], "topic": topic}
            return result
        except:
            print("Error fetching latest schema using url:" + fetch_latest_versions_url)



    
    



