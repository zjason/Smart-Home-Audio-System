#!/usr/bin/python

from vcnl4000 import VCNL4000
import time
import threading

__author__ = 'icer'


class Detector(object):
    """
    sensor detector base class, update led
    status according to the sensor reading
    @:param
    """
    # Constructor
    # initiating sensor and reading thread
    def __init__(self):
        self.LED = False
        self.LEDAction = False
        self.vcnl = VCNL4000(0x13)
        t = threading.Thread(target=self.check_present)
        t.daemon = True
        t.start()

    # check proximity
    def check_present(self):
        while True:
            if self.vcnl.read_proximity() > 10000:
                if self.LEDAction == False:
                    print "Present !!!!"
                    self.LED = True
                time.sleep(0.1)
            else:
                if self.LEDAction == False:
                    print "No one"
                    self.LED = False
                time.sleep(0.1)

    def control_LED(self, status):
        self.LEDAction = True
        if status == 'ON':
            self.LED = True
        else:
            self.LED = False

    def check_led(self):
        return self.LED


