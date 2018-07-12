import unittest
import sys
from test_bed_options import TestBedOptions
from test_bed_adapter import TestBedAdapter
import threading
import time
import logging
import json
sys.path.append("..")
logging.basicConfig(level=logging.INFO)

class MyTestCase(unittest.TestCase):


    def test_consumer_from_adapter(self):
        self.was_any_message_obtained = False

        options_file = open("test_bed_options_for_tests.json", encoding="utf8")
        options = json.loads(options_file.read())
        options_file.close()

        test_bed_options = TestBedOptions(options)
        test_bed_adapter = TestBedAdapter(test_bed_options)

        #We add the message handler
        test_bed_adapter.on_message += self.handle_message

        e = threading.Event()
        t = threading.Thread(target=self.run_consumer_in_thread, args=(e, test_bed_adapter))
        t.start()

        # wait 30 seconds for the thread to finish its work
        t.join(5)
        if t.is_alive():
            print
            "thread is not done, setting event to kill thread."
            e.set()
        else:
            print
            "thread has already finished."

        self.assertTrue(self.was_any_message_obtained)

    def handle_message(self,message):
        logging.info("-------")
        self.was_any_message_obtained=True
        logging.info(message)

    def run_consumer_in_thread(self, e, test_bed_adapter):
        data = set()
        test_bed_adapter.initialize()
        test_bed_adapter.consumers["standard_cap"].listen_messages()
        # test_bed_adapter.consumers["simulation-entity-item"].listen_messages()

        for i in range(60):
            data.add(i)
            if not e.isSet():
                time.sleep(1)
            else:
                break


if __name__ == '__main__':
    unittest.main()
