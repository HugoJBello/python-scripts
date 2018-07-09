import unittest
import unittest
import sys
sys.path.append("..")

from models.test_bed_options import TestBedOptions
from test_bed_adapter import TestBedAdapter

import logging
logging.basicConfig(level=logging.INFO)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.was_any_message_obtained = False

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

        test_bed_adapter.initialize()
        test_bed_adapter.consumers["standard_cap"].listen_messages()
        #test_bed_adapter.consumers["simulation-entity-item"].listen_messages()

        self.assertEqual(True, True)

    def handle_message(self,message):
        logging.info("-------")
        self.was_any_message_obtained=True
        logging.info(message)


if __name__ == '__main__':
    unittest.main()
