import avro.schema
import avro.io
import io
import sys
import json
import logging

import avro.datafile
class AvroSchemaHelper:
    avro_schema: object

    def __init__(self, schema_str, topic):
        self._schema_str = schema_str
        self.topic = topic
        json_schema = json.loads(self._schema_str)
        self.avro_schema = avro.schema.SchemaFromJSONData(json_schema)

    def avro_encode_messages(self, json_messages):
        bytes_writer = io.BytesIO()
        writer = avro.io.DatumWriter(self.avro_schema)
        encoder = avro.io.BinaryEncoder(bytes_writer)
        writer.write(json_messages, encoder)
        raw_bytes = bytes_writer.getvalue()
        return raw_bytes

    def avro_decode_message(self, message):
        if (message):
            bytes_from_message = bytearray(message)
            # if the message starts with this sequence of bytes '\\x00\\x00\\x00\\x00',
            # the avro decoder for python does not decode the message so we remove the first five bytes
            if ('\\x00\\x00\\x00\\x00' in str(bytes_from_message[0:5])):
                bytes_from_message = bytes_from_message[5:]
                message = bytes(bytes_from_message)
            bytes_reader = io.BytesIO(message)
            decoder = avro.io.BinaryDecoder(bytes_reader)
            reader = avro.io.DatumReader(self.avro_schema)
            decoded_messages = []

            #We iterate in case there are more than one messages
            while (bytes_reader.tell() < len(message)):
                try:
                    #Here is where the messages are read
                    decoded_messages.append(reader.read(decoder))
                    sys.stdout.flush()
                except Exception as e:
                    logging.error(e)
            return decoded_messages