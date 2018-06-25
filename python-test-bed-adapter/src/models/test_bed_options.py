class TestBedOptions:
    def __init__(self, **entries):
        #, clientId, kafkaHost, schemaRegistry):
        # Unique ID of this client
        self.clientId = None

        # Uri for the Kafka broker, e.g. broker:3501
        self.kafkaHost = None

        # Uri for the schema registry, e.g. schema_registry:3502
        self.schemaRegistry = None

        self.__dict__.update(entries)
       
    def validate_options(self):
        print("")

    def get_options_from_file(self):
        print("")
        
        
