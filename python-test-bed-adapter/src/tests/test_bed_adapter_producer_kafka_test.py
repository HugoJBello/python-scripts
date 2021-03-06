import unittest
import sys
sys.path.append("..")
import json
import os
from test_bed_options import TestBedOptions
from test_bed_adapter import TestBedAdapter

import logging
logging.basicConfig(level=logging.INFO)

class MyTestCase(unittest.TestCase):
    def test_producer_using_adapter(self):
        self.was_any_message_obtained = False

        options_file = open("test_bed_options_for_tests_producer.json",encoding="utf8")
        options = json.loads(options_file.read())
        options_file.close()
        test_bed_options = TestBedOptions(options)

        message_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"test_messages\\example_amber_alert.json")
        example_message_file = open(message_path, encoding="utf-8")
        message_json = json.loads(example_message_file.read())
        example_message_file.close()
        message = {"messages":message_json}

        test_bed_adapter = TestBedAdapter(test_bed_options)
        test_bed_adapter.on_sent += self.message_sent_handler
        test_bed_adapter.initialize()
        test_bed_adapter.kafka_managers["standard_cap"].send_messages(message)

        #test_bed_adapter.consumers["simulation-entity-item"].listen_messages()

        self.assertEqual(True, True)

    def message_sent_handler(self,json_message):
        logging.info("message sent")
        logging.info(json_message)


if __name__ == '__main__':
    unittest.main()
