
from models.event_hook import EventHook
from models.test_bed_options import TestBedOptions
from pykafka import KafkaClient


class TestBedAdapter:
    def __init__(self):
         
        self.is_connected = False

        self.kafkaClient: KafkaClient = None
        self.config: TestBedOptions = None

        #We set up the listeners
        self.is_ready = EventHook()
        self.message = EventHook()
        self.error = EventHook()

    def connect(self):
        print("")
        self.is_connected = True
        self.is_ready.fire()

    def send_message(self):
        print("")