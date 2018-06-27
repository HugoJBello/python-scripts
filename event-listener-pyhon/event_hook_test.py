#https://stackoverflow.com/questions/1092531/event-system-in-python/1094423#1094423
from event_hook import EventHook

def ready(input):
    print("ready " + input)
    return "re"

def start():
    print("start")
    return "a"

class MyBroadcaster:
    def __init__(self):
        self.onReady = EventHook()
        self.onStart = EventHook()

theBroadcaster = MyBroadcaster()

# add a listener to the event
theBroadcaster.onReady += ready

theBroadcaster.onStart += start

# remove listener from the event
#theBroadcaster.onChange -= function

# fire event
theBroadcaster.onReady.fire("aaa")
theBroadcaster.onReady.fire("aaasss 2222")

theBroadcaster.onStart.fire()

