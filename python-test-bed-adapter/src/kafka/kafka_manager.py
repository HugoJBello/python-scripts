from event_hook import EventHook
from pykafka import KafkaClient
import datetime, time
import logging
import uuid

class KafkaManager():
    def __init__(self, kafka_topic, kafka_host, from_off_set, client_id, avro_helper_key, avro_helper_value, on_message_handler):
        self.topic = kafka_topic
        self.on_message = EventHook()
        self.avro_helper_key = avro_helper_key
        self.avro_helper_value = avro_helper_value
        self.from_off_set = from_off_set
        self.kafka_host = kafka_host
        self.client_id = client_id

        if(on_message_handler):
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

    def send_messages(self,json_message):
        if ("messages" in list(json_message.keys())):
            messages = json_message["messages"]

            date = datetime.datetime.utcnow()
            date_ms = int(time.mktime(date.timetuple())) * 1000

            if ("key" in list(json_message.keys())):
                key = json_message["key"]
            else:
                key = {"distributionID": str(uuid.uuid4()), "senderID": self.client_id, "dateTimeSent": date_ms, "dateTimeExpires": 0, "distributionStatus": "Test", "distributionKind": "Unknown"}
                #key = {"identifier": str(uuid.uuid4()), "sender": self.client_id, "sent": date}

            encoded_message = self.avro_helper_value.avro_encode_messages(messages)
            encoded_key = self.avro_helper_key.avro_encode_messages(key)

            with self.client_topic.get_sync_producer() as producer:
                producer.produce(encoded_key)
                producer.produce(encoded_message)

