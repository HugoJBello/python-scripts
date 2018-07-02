import avro.schema
import avro.io
import io
import sys
import json

import avro.datafile
class AvroSchemaHelper:
    avro_schema: object

    def __init__(self, schema_str, topic):
        self._schema_str = schema_str
        self.topic = topic
        self.avro_schema = avro.schema.SchemaFromJSONData(json.loads(self._schema_str))
        #self.avro_schema = avro.schema.Parse(open("C:/hugo_documentos/otros/github/python-scripts/python-test-bed-adapter/src/models/cap-value.avsc").read())
        #self.avro_schema = avro.schema.Parse(open("C://Users/HJBG/AppData/Local/Microsoft/Windows/INetCache/Content.Outlook/BVQ694OM/simulation_entity_item-value.avsc").read())

    def avro_encode_messages(self, json_messages):
        bytes_writer = io.BytesIO()
        writer = avro.io.DatumWriter(self.avro_schema)
        encoder = avro.io.BinaryEncoder(bytes_writer)
        for message in json_messages:
            writer.write(message, encoder)
        raw_bytes = bytes_writer.getvalue()
        return raw_bytes

    def avro_decode_message(self, message):
        #We remove the first five bytes
        a = bytearray(message)
        a = a[5:]
        message=bytes(a)
        bytes_reader = io.BytesIO(message)
        decoder = avro.io.BinaryDecoder(bytes_reader)
        reader = avro.io.DatumReader(self.avro_schema)
        decoded_messages = []
        while (bytes_reader.tell() < len(message)):
            try:
                decoded_messages.append(reader.read(decoder))
                sys.stdout.flush()
            except Exception as e:
                print(e)
        return decoded_messages