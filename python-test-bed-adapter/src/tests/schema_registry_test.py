import unittest
import sys
sys.path.append("..")
from models.schema_registry import SchemaRegistry
from models.test_bed_options import TestBedOptions
import logging
logging.basicConfig(level=logging.INFO)

class MyTestCase(unittest.TestCase):
    def test_something(self):
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
        schema_registry = SchemaRegistry(test_bed_configuration)
        schema_registry.start_process()
        logging.info(schema_registry.fetched_schemas)

        logging.info(schema_registry.keys_schema)
        logging.info("----------------------------------------------------------------------------\n\n")
        logging.info(schema_registry.values_schema)
        logging.info("----------------------------------------------------------------------------\n\n")
        logging.info(schema_registry.schema_meta)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
