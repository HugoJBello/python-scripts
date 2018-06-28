class TestBedOptions:
    def __init__(self, dictionary):
        # clientId, kafkaHost, schemaRegistry)
        # Unique ID of this client
        self.clientId = None

        # Uri for the Kafka broker, e.g. broker:3501
        self.kafka_host = None

        # Uri for the schema registry, e.g. schema_registry:3502
        self.schema_registry = None

        #
        self.auto_register_schemas = False

        # If autoRegisterSchemas is true, contains the folder with *.avsc schema's to register
        self.schema_folder = "data/schemas"

        # If true fetch all schema versions (and not only the latest)
        self.fetch_all_versions = False

        # If true fetch all schema's (and not only the consume and produce topics)
        self.fetch_all_schemas = False

        # If true fetch all schema's (and not only the consume and produce topics)
        self.fetch_all_topics = False

        # Topics you want to consume
        self.consume = None

        # Topics you want to produce
        self.produce = None

        for key in dictionary:
            setattr(self, key, dictionary[key])

    def validate_options(self):
        print("")

    def get_options_from_file(self):
        print("")
        
        
