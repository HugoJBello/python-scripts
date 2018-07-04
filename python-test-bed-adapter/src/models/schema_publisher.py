import asyncio
import logging
import requests
from model.schema_access import SchemaAccess

class SchemaRegistry(SchemaAccess):
    def __init__(self, test_bed_options):
        super().__init__(test_bed_options)

    async def start_process(self, future):
        await self.is_schema_registry_available()







