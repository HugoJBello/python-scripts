import unittest
import unittest
import sys
sys.path.append("..")

from models.test_bed_options import TestBedOptions
from models.consumer_kafka import ConsumerKafka
from models.avro_schema_helper import AvroSchemaHelper
from test_bed_adapter import TestBedAdapter
import asyncio

import logging
logging.basicConfig(level=logging.INFO)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        options ={
          "auto_register_schemas":False,
          #"kafka_host": 'driver-testbed.eu:3501',
          #"schema_registry": 'http://driver-testbed.eu:3502',
          "kafka_host": '127.0.0.1:3501',
          "schema_registry": 'http://localhost:3502',
          "fetch_all_versions": False,
          "client_id": 'GMV-Consumer',
          "consume": ["standard_cap","simulation-entity-item"]}

        test_bed_options = TestBedOptions(options)
        test_bed_adapter = TestBedAdapter(test_bed_options)

        #We add the message handler
        test_bed_adapter.on_message += self.handle_message

        asyncio.run(test_bed_adapter.initialize())

        test_bed_adapter.consumers["standard_cap"].listen_messages()
        #test_bed_adapter.consumers["simulation-entity-item"].listen_messages()



        self.assertEqual(True, False)

    def handle_message(self,message):
        logging.info("-------")
        logging.info(message)


if __name__ == '__main__':
    unittest.main()
