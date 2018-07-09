
from models.event_hook import EventHook
from models.test_bed_options import TestBedOptions
from models.consumer_kafka import ConsumerKafka
from models.schema_registry import SchemaRegistry
import asyncio

import logging


class TestBedAdapter:
    def __init__(self, test_bed_options:TestBedOptions):
         
        self.is_connected = False
        self.test_bed_options = test_bed_options
        self.schema_registry = SchemaRegistry(test_bed_options)

        self.consumers = {}
        self.producers = {}

        #We set up the handlers for the events
        self.is_ready = EventHook()
        self.on_message = EventHook()
        self.on_error = EventHook()

    def initialize(self):
        logging.info("Initializing test bed")
        self.schema_registry.start_process()
        self.init_consumers()
        self.init_producers()



    async def connect(self):
        logging.info("")
        self.is_connected = True
        self.is_ready.fire()

    def init_consumers(self):
        for topic_name in self.test_bed_options.consume:
            logging.info("Initializing Kafka consumer for topic " + topic_name)
            avro_helper_key = self.schema_registry.keys_schema[topic_name]["avro_helper"]
            avro_helper_value = self.schema_registry.values_schema[topic_name]["avro_helper"]

            #We create a new consumer for this topic. The last input is the callback where we handle the message recieved and decoded from kafka.
            consumer = ConsumerKafka(bytes(topic_name, 'utf-8'), self.test_bed_options.kafka_host, self.test_bed_options.from_off_set,
                                     self.test_bed_options.client_id, avro_helper_key, avro_helper_value, self.handle_message)
            self.consumers[topic_name] = consumer

    def init_producers(self):
        logging.info("")


    def handle_message(self, message):
        #We emit the message
        self.on_message.fire(message)

    def send_message(self):
        logging.info("")