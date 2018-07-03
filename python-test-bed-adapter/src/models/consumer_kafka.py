from models.event_hook import EventHook
from pykafka import KafkaClient
import logging


class ConsumerKafka():
    def __init__(self, kafka_topic, kafka_host, from_off_set, client_id, avro_helper_key, avro_helper_value, on_message_handler):
        self.topic = kafka_topic
        self.on_message = EventHook()
        self.avro_helper_key = avro_helper_key
        self.avro_helper_value = avro_helper_value
        self.from_off_set = from_off_set
        self.kafka_host = kafka_host
        self.client_id = client_id

        self.on_message += on_message_handler

        self.client = KafkaClient(hosts=self.kafka_host,exclude_internal_topics=self.from_off_set)
        self.client_topic = self.client.topics[kafka_topic]


    def listen_messages(self):
        consumer = self.client_topic.get_simple_consumer()
        for message in consumer:
            if message is not None:
                logging.info(str(message.value))
                decoded_value, decoded_key = "" , ""

                if (self.avro_helper_key):
                    decoded_key = self.avro_helper_key.avro_decode_message(message.partition_key)

                if (self.avro_helper_value):
                    decoded_value = self.avro_helper_value.avro_decode_message(message.value)
                decoded_message = {"decoded_key" : decoded_key, "decoded_value" : decoded_value}
                self.on_message.fire(decoded_message)
