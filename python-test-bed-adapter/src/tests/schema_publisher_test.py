import unittest
import json
from test_bed_options import TestBedOptions
from registry.schema_publisher import SchemaPublisher
import logging
logging.basicConfig(level=logging.INFO)

class SchemaPublisherTest(unittest.TestCase):

    def test_schema_registry(self):
        options_file = open("test_bed_options_for_tests_consumer.json", encoding="utf8")
        options = json.loads(options_file.read())
        options_file.close()

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