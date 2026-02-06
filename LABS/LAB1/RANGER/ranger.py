#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import sys
from HCSR04_lib import HCSR04


#GPIO Mode (BOARD / BCM)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

TRIG = 4
ECHO = 17

GPIO.setup(TRIG, GPIO.OUT)

instance = HCSR04(TRIG_pin=TRIG, ECHO_pin=ECHO)  # BCM17

CLEAR_SCREEN = "\033[2J\033[H"
# keep a short pause between measurements to reduce sensor noise
REFRESH_DELAY = 0.1

instance.init_HCSR04()

try:
    while True:
        distance = instance.measure_distance()
        sys.stdout.write(CLEAR_SCREEN + "distance is: {:.1f} cm\n".format(distance))
        sys.stdout.flush()
        time.sleep(REFRESH_DELAY)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()