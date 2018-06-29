from pykafka import KafkaClient

from kafka import KafkaConsumer,SimpleProducer


import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from kafka import KafkaProducer
import avro.io
import io
import threading

class KafkaAvroTester :
    def __init__(self,topic_name,kafka_hosts,schema_file):
        kafka = KafkaClient(kafka_hosts)
        self.topic_name =topic_name
        self.producer = KafkaProducer(bootstrap_servers=kafka_hosts)
        self.consumer = KafkaConsumer(topic_name, bootstrap_servers=kafka_hosts)

        self.schema = avro.schema.Parse(b'{"namespace":"example.avro","type":"record","name":"User","fields":[{"name":"name","type":"string"},{"name":"favorite_number","type":["int","null"]},{"name":"favorite_color","type":["string","null"]}]}')
        #self.schema = avro.schema.Parse(open(schema_file).read())


    def avro_encode_messages(self,json_messages):
        bytes_writer = io.BytesIO()
        writer = avro.io.DatumWriter(self.schema)
        encoder = avro.io.BinaryEncoder(bytes_writer)
        for message in json_messages:
            writer.write(message, encoder)
        raw_bytes = bytes_writer.getvalue()
        return raw_bytes

    def produce_kafka(self, bytes_message):
        future = self.producer.send(self.topic_name, bytes_message)
        result = future.get(timeout=5)

    def avro_decode_message(self,message):
        if(message):
            bytes_reader = io.BytesIO(message)
            decoder = avro.io.BinaryDecoder(bytes_reader)
            reader = avro.io.DatumReader(self.schema)
            decoded_messages =[]
            while(bytes_reader.tell() < len(message)):
                try:
                    decoded_messages.append(reader.read(decoder))
                except Exception as e: print(e)
            return decoded_messages


    def listener_consumer(self):
        for message in self.consumer:
            if message is not None:
                print(message.value)
                decoded = self.avro_decode_message(message.value)
                print(decoded)
                
                
if __name__=="__main__":
    topic_name = 'topic-test2'
    schema_file = "user.avsc"
    kafka_hosts = "localhost:9092,localhost:9093"
    kafkaAvroTester = KafkaAvroTester(topic_name,kafka_hosts,schema_file)
    json1 = {"name": "Alyssa2", "favorite_number": 256}
    json2 = {"name": "Ben2", "favorite_number": 7, "favorite_color": "red2"}

    messages = [json1,json2]
    message_bytes = kafkaAvroTester.avro_encode_messages(messages)
    
    kafkaAvroTester.produce_kafka(message_bytes)

    kafkaAvroTester.listener_consumer()

    

    