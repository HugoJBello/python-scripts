from pykafka import KafkaClient
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import avro.io
import io
import threading

class KafkaAvroTester :
    def __init__(self,topic_name,kafka_hosts,schema_file):
        self.client = KafkaClient(hosts=kafka_hosts)
        self.topic = self.client.topics[topic_name]
        self.schema = avro.schema.Parse(open(schema_file).read())
        self.test:str
    

    def avro_encode_messages(self,json_messages):
        bytes_writer = io.BytesIO()
        writer = avro.io.DatumWriter(self.schema)
        encoder = avro.io.BinaryEncoder(bytes_writer)
        for message in json_messages:
            writer.write(message, encoder)
        raw_bytes = bytes_writer.getvalue()
        return raw_bytes

    def produce_kafka(self,bytes_message):
        with self.topic.get_sync_producer() as producer:
            producer.produce(bytes_message)

    def avro_decode_message(self,message):
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
        consumer = self.topic.get_simple_consumer()
        for message in consumer:
            if message is not None:
                print(message.offset, message.value)
                decoded = self.avro_decode_message(message.value)
                print(decoded)
                
                
if __name__=="__main__":
    topic_name = b'topic-test'
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

    

    