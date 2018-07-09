import asyncio
import logging
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class SchemaAccess:
    def __init__(self, test_bed_options):
        self.retries = test_bed_options.reconnection_retries
        self.backoff = 0.3
        self.staturs_forcelist = (500, 502, 504)
        self.schema_url = test_bed_options.schema_registry

    def requests_retry_session(self):
        session = requests.Session()
        retry = Retry(
            total=self.retries,
            read=self.retries,
            connect=self.retries,
            backoff_factor=self.backoff,
            status_forcelist=self.staturs_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def is_schema_registry_available(self):
        url = self.schema_url
        logging.info("schema available")
        self.schema_available = True
        try:
            logging.info("checking schema in url :" + url)
            response = self.requests_retry_session().get(url)
            self.schema_available = True
        except:
            logging.error("Error fetching url:" + url)
            self.schema_available = False





