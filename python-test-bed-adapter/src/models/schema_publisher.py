import asyncio
import logging
import requests
import json
import os
from models.schema_access import SchemaAccess
from utils.helpers import Helpers


class SchemaPublisher(SchemaAccess):
    def __init__(self, test_bed_options):
        super().__init__(test_bed_options)
        self.default_schema = "default_schema.json"
        self.schema_folder = test_bed_options.schema_folder
        file_path = os.path.dirname(os.path.abspath(__file__))
        self.default_schema_path = os.path.join(file_path,self.default_schema)

    async def start_process(self, future):
        await self.is_schema_registry_available()

        if self.schema_available:
            files = Helpers.find_files_in_dir(self.schema_folder)
            missing_key_files = Helpers.missing_key_files(files)
            files_upload = files + missing_key_files
            for schema_file in files_upload:
                use_default_schema = schema_file in missing_key_files
                self.post_schema(schema_file, use_default_schema)

    def post_schema(self, schema_filename:str, use_default_schema:bool):
        schema_topic = os.path.basename(schema_filename).replace(".avsc","")
        upload_url = self.schema_url + "/subjects/"+schema_topic+"/versions"
        default_schema = json.loads(open(self.default_schema_path,encoding="utf-8").read())
        schema = default_schema if use_default_schema else json.loads(open(schema_filename,encoding="utf-8").read())

        data = {"schema":schema}
        headers = {"Content-type": "application/vnd.schemaregistry.v1+json"}
        try:
            requests.post(url=upload_url, data=data, headers=headers)
            logging.info("Uploaded schema " + schema_topic + " to " + upload_url)
        except:
            logging.error("Error uploading schema " + schema_topic + " to " + upload_url)


