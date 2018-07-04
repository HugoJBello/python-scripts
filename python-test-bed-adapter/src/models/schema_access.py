import asyncio
import logging
import requests

class SchemaAccess:
    def __init__(self, test_bed_options):

        self.schema_url = test_bed_options.schema_registry

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





