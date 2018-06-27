import io

import avro.schema


class AvroSchemaHelper:
    avro_schema: object

    def __init__(self, schema_str, topic):
        self._schema_str = schema_str
        self.topic = topic
        self.avro_schema = avro.schema.Parse(self._schema_str)

    def avro_encode_messages(self, json_messages):
        bytes_writer = io.BytesIO()
        writer = avro.io.DatumWriter(self.avro_schema)
        encoder = avro.io.BinaryEncoder(bytes_writer)
        for message in json_messages:
            writer.write(message, encoder)
        raw_bytes = bytes_writer.getvalue()
        return raw_bytes

    def avro_decode_message(self, message):
        bytes_reader = io.BytesIO(message)
        decoder = avro.io.BinaryDecoder(bytes_reader)
        reader = avro.io.DatumReader(self.avro_schema)
        decoded_messages =[]
        while(bytes_reader.tell() < len(message)):
            try:
                decoded_messages.append(reader.read(decoder))
            except Exception as e: print(e)
        return decoded_messages