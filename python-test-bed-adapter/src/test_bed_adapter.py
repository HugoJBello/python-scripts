
from models.event_hook import EventHook
from models.test_bed_options import TestBedOptions
from models.consumer_kafka import ConsumerKafka
import logging


class TestBedAdapter:
    def __init__(self):
         
        self.is_connected = False

        self.config: TestBedOptions = None

        #We set up the listeners
        self.is_ready = EventHook()
        self.message = EventHook()
        self.error = EventHook()

    def connect(self):
        logging.info("")
        self.is_connected = True
        self.is_ready.fire()

    def init_consumer(self):
        logging.info("")

    def handle_message(self):
        logging.info("")

    def send_message(self):
        logging.info("")