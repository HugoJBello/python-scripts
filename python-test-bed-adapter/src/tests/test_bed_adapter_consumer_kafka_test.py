import unittest
import sys
sys.path.append("..")
import json
from test_bed_options import TestBedOptions
from test_bed_adapter import TestBedAdapter

import logging
logging.basicConfig(level=logging.INFO)

class MyTestCase(unittest.TestCase):
    def test_consumer_using_adapter(self):
        self.was_any_message_obtained = False

        options_file = open("test_bed_options_for_tests_consumer.json",encoding="utf8")
        options = json.loads(options_file.read())
        options_file.close()

        test_bed_options = TestBedOptions(options)
        test_bed_adapter = TestBedAdapter(test_bed_options)

        # We add the message handler
        test_bed_adapter.on_message += self.handle_message


        test_bed_adapter.initialize()
        topic=list(test_bed_adapter.kafka_managers.keys())[0]
        test_bed_adapter.kafka_managers[topic].listen_messages()

        self.assertEqual(True, True)

    def handle_message(self,message):
        logging.info("-------")
        self.was_any_message_obtained=True
        logging.info(message)


if __name__ == '__main__':
    unittest.main()
