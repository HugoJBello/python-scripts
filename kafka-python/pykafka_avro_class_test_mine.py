from pykafka import KafkaClient
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import avro.io
import io
import threading
import traceback

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter, VALID_CODECS, SCHEMA_KEY
from avro.io import DatumReader, DatumWriter
from avro import io as avro_io


class MyDataFileReader(DataFileReader):
    def __init__(self, reader, datum_reader,schema):
        """Initializes a new data file reader.

        Args:
          reader: Open file to read from.
          datum_reader: Avro datum reader.
        """
        self._reader = reader
        self._raw_decoder = avro_io.BinaryDecoder(reader)
        self._datum_decoder = None  # Maybe reset at every block.
        self._datum_reader = datum_reader

        # read the header: magic, meta, sync
        self._read_header()

        # ensure codec is valid
        avro_codec_raw = self.GetMeta('avro.codec')
        if avro_codec_raw is None:
            self.codec = "null"
        else:
            self.codec = avro_codec_raw.decode('utf-8')
        if self.codec not in VALID_CODECS:
            raise Exception('Unknown codec: %s.' % self.codec)

        self._file_length = self._GetInputFileLength()

        # get ready to read



class KafkaAvroTester :
    def __init__(self,topic_name,kafka_hosts,schema_file):
        self.client = KafkaClient(hosts=kafka_hosts)
        self.topic = self.client.topics[topic_name]
        self.schema = avro.schema.Parse(b'{"namespace":"example.avro","type":"record","name":"User","fields":[{"name":"name","type":"string"},{"name":"favorite_number","type":["int","null"]},{"name":"favorite_color","type":["string","null"]}]}')
        #self.schema = avro.schema.Parse(open(schema_file).read())


    def avro_encode_messages(self,json_messages):
        buf = io.BytesIO()
        writer = avro.datafile.DataFileWriter(buf, avro.io.DatumWriter(self.schema),self.schema)
        for message in json_messages:
            writer.append(message)
        writer.flush()
        buf.seek(0)
        data = buf.read()
        return data

    def produce_kafka(self,bytes_message):
        with self.topic.get_sync_producer() as producer:
            producer.produce(bytes_message)

    def avro_decode_message(self, message):
        if(message):
            try:
                message_buf = io.BytesIO(message)
                reader =  MyDataFileReader(message_buf, avro.io.DatumReader(),self.schema)
                decoded_messages = []
                for thing in reader:
                    print(thing)
                    decoded_messages.append(thing)
                reader.close()
                return decoded_messages
            except: traceback.print_exc()


    def listener_consumer(self):
        consumer = self.topic.get_simple_consumer()
        for message in consumer:
            if message is not None:
                print(message.offset, message.value)
                decoded = self.avro_decode_message(message.value)
                print(decoded)
                
                
if __name__=="__main__":
    topic_name = b'topic-test2'
    schema_file = "user.avsc"
    kafka_hosts = "127.0.0.1:9092,127.0.0.1:9093"
    kafkaAvroTester = KafkaAvroTester(topic_name,kafka_hosts,schema_file)
    json1 = {"name": "Alyssa2", "favorite_number": 256}
    json2 = {"name": "Ben2", "favorite_number": 7, "favorite_color": "red2"}

    messages = [json1,json2]
    message_bytes = kafkaAvroTester.avro_encode_messages(messages)
    
    kafkaAvroTester.produce_kafka(message_bytes)

    kafkaAvroTester.listener_consumer()

    

    