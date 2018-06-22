class TestBedOptions:
    def __init__(self, clientId, kafkaHost, schemaRegistry):

        # Unique ID of this client
        clientId = clientId

        # Uri for the Kafka broker, e.g. broker:3501
        kafkaHost = kafkaHost

        # Uri for the schema registry, e.g. schema_registry:3502
        schemaRegistry = schemaRegistry
    
    def get_options_from_file(self):
        print("")
        
        
