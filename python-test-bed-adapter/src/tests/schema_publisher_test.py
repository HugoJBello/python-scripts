import unittest
import asyncio
from models.test_bed_options import TestBedOptions
from models.schema_publisher import SchemaPublisher
import logging
logging.basicConfig(level=logging.INFO)

class SchemaPublisherTest(unittest.TestCase):

    def test_schema_registry(self):
        options ={
          "auto_register_schemas":False,
          #"kafka_host": 'http://driver-testbed.eu:3501',
          #"schema_registry": 'http://driver-testbed.eu:3502',
          "kafka_host": 'http://localhost:3501',
          "schema_registry": 'http://localhost:3502',
          "fetch_all_versions": False,
          "client_id": 'ConsumerErik',
          "consume": None}

        test_bed_configuration = TestBedOptions(options)
        schema_publisher = SchemaPublisher(test_bed_configuration)

        error_obtained = False
        try:
            schema_publisher.start_process()
        except:
            error_obtained=True

        self.assertIs(error_obtained, False)



if __name__ == '__main__':
    unittest.main()