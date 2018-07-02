from models.event_hook import EventHook
from pykafka import KafkaClient
import logging


class ConsumerKafka():
    def __init__(self, topic, test_bed_options, on_message_handler, avro_helper_key, avro_helper_value):
        self.topic = topic
        self.on_message = EventHook()
        self.on_message += on_message_handler
        self.avro_helper_key = avro_helper_key
        self.avro_helper_value = avro_helper_value

        self.kafka_host = test_bed_options.kafka_host
        self.registry = test_bed_options.schema_registry
        client_id = test_bed_options.client_id

        self.client = KafkaClient(hosts=self.kafka_host)
        self.client_topic = self.client.topics[topic]


    def listen_messages(self):
        consumer = self.client_topic.get_simple_consumer()
        for message in consumer:
            if message is not None:
                logging.info(str(message.value))
                #decoded_key = self.avro_helper_key.avro_decode_message(message.partition_key)
                decoded_value = self.avro_helper_value.avro_decode_message(message.value)
                logging.info("-------------------------------")
                logging.info(decoded_value)
                decoded_message = {"decoded_key" : "", "decoded_value" : decoded_value}
                self.on_message.fire(decoded_message)
