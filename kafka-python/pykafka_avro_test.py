# pip3 install pykafka
# pip3 install avro-python3
# https://github.com/Parsely/pykafkaS

#kafka-topics --create --zookeeper 127.0.0.1:2181 --partitions 1 --replication-factor 1 --topic topic-test

from pykafka import KafkaClient
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import avro.io
import io

client = KafkaClient(hosts="127.0.0.1:9092,127.0.0.1:9093")

schema = avro.schema.Parse(open("user.avsc").read())
writer = avro.io.DatumWriter(schema)


bytes_writer = io.BytesIO()
encoder = avro.io.BinaryEncoder(bytes_writer)
writer.write({"name": "Alyssa", "favorite_number": 256}, encoder)
writer.write({"name": "Ben", "favorite_number": 7, "favorite_color": "red"}, encoder)

raw_bytes = bytes_writer.getvalue()

print(client.topics)
topic = client.topics[b'topic-test']

with topic.get_sync_producer() as producer:
    producer.produce(raw_bytes)


consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
        print(message.offset, message.value)
        try:
            bytes_reader = io.BytesIO(message.value)
            decoder = avro.io.BinaryDecoder(bytes_reader)
            reader = avro.io.DatumReader(schema)
            user1 = reader.read(decoder)
            user2 = reader.read(decoder)
            print(user1)
            print(user2)
        except:
            print("error")