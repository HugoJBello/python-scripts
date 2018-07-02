from pykafka import KafkaClient
import io
import fastavro
import json

class KafkaAvroTester :
    def __init__(self,topic_name,kafka_hosts,schema_file):
        self.client = KafkaClient(hosts=kafka_hosts)
        self.topic = self.client.topics[topic_name]
        self.schema_str = '{"namespace": "example.avro","type": "record","name": "User","fields": [{"name": "name", "type": "string"}, {"name": "favorite_number",  "type": ["int", "null"]}, {"name": "favorite_color", "type": ["string", "null"]} ]}'
        self.test:str
    

    def avro_encode_messages(self,json_messages):
        encoded_messages  = io.BytesIO()
        writer = fastavro.writer(encoded_messages, json.loads(self.schema_str),json_messages)
        return encoded_messages.getvalue()

    def produce_kafka(self,bytes_message):
        with self.topic.get_sync_producer() as producer:
            producer.produce(bytes_message)

    def avro_decode_message(self,message):
        if (message):
            message = io.BytesIO(message)
            record = fastavro.schemaless_reader(message, json.loads(self.schema_str))
            return record



    def listener_consumer(self):
        consumer = self.topic.get_simple_consumer()
        for message in consumer:
            if message is not None:
                print("--------------------------------")
                print(message.offset, message.value)
                decoded = self.avro_decode_message(message.value)
                print("---")
                print(decoded)
                
                
if __name__=="__main__":
    topic_name = b'topic-test2'
    schema_file = "user.avsc"
    kafka_hosts = "127.0.0.1:9092,127.0.0.1:9093"
    kafkaAvroTester = KafkaAvroTester(topic_name,kafka_hosts,schema_file)
    kafkaAvroTester.test="a"
    json1 = {"name": "Alyssa2", "favorite_number": 256}
    json2 = {"name": "Ben2", "favorite_number": 7, "favorite_color": "red2"}

    print(kafkaAvroTester.test)

    messages = [json1,json2]
    message_bytes = kafkaAvroTester.avro_encode_messages(messages)
    
    kafkaAvroTester.produce_kafka(message_bytes)

    kafkaAvroTester.listener_consumer()

    

    