
from event_hook import EventHook
from test_bed_options import TestBedOptions
from kafka_manager import KafkaManager
from registry.schema_registry import SchemaRegistry
from schema_publisher import SchemaPublisher
import logging


class TestBedAdapter:
    def __init__(self, test_bed_options: TestBedOptions):
         
        self.is_connected = False
        self.test_bed_options = test_bed_options
        self.schema_registry = SchemaRegistry(test_bed_options)
        self.schema_publisher = SchemaPublisher(test_bed_options)

        self.kafka_managers = {}

        #We set up the handlers for the events
        self.on_ready = EventHook()
        self.on_message = EventHook()
        self.on_sent = EventHook()
        self.on_error = EventHook()

    def initialize(self):
        logging.info("Initializing test bed")
        self.schema_registry.start_process()
        self.schema_publisher.start_process()
        self.init_consumers()
        self.init_producers()

        #We emit here by firing the on ready observable.
        self.on_ready.fire()

    async def connect(self):
        logging.info("")
        self.is_connected = True
        self.is_ready.fire()

    def init_consumers(self):
        if self.test_bed_options.consume:
            self.init_kafka_managers(self.test_bed_options.consume, self.handle_message)

    def init_producers(self):
        if self.test_bed_options.produce:
            self.init_kafka_managers(self.test_bed_options.produce, self.succesfully_sent_message)

    #The last input is the function handler that will be called once a message is recieved or sent
    def init_kafka_managers(self, topics, handler):
        for topic_name in topics:
            logging.info("Initializing Kafka manager for topic " + topic_name)
            avro_helper_key = self.schema_registry.keys_schema[topic_name]["avro_helper"]
            avro_helper_value = self.schema_registry.values_schema[topic_name]["avro_helper"]

            # We create a new manager for this topic. The last input is the callback where we handle the message recieved and decoded from kafka.
            manager = KafkaManager(bytes(topic_name, 'utf-8'), self.test_bed_options.kafka_host,
                                    self.test_bed_options.from_off_set,
                                    self.test_bed_options.client_id, avro_helper_key, avro_helper_value,
                                    handler)
            self.kafka_managers[topic_name] = manager

    def handle_message(self, message):
        #We emit the message
        self.on_message.fire(message)

    def succesfully_sent_message(self, message):
        self.on_sent.fire(message)
