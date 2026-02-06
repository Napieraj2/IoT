#!/usr/bin/env python3

import RPi.GPIO as GPIO
from TEMP.DHT11_lib import DHT11
import time
import datetime
import sys

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# read data using BCM pin 17 (physical pin 11)
instance = DHT11(pin=17)

# DHT11 hardware needs a 1 second sampling interval
MIN_SAMPLE_INTERVAL = 1.0
CLEAR_SCREEN = "\033[2J\033[H"
last_valid_status = "Last valid: waiting for sensor"
last_attempt_status = "Last attempt: not started"

try:
    while True:
        loop_started = time.monotonic()
        result = instance.read()
        now = datetime.datetime.now()

        if result.is_valid():
            temp_c = result.temperature
            temp_f = temp_c * 9 / 5 + 32
            last_valid_status = "Last valid: {:%Y-%m-%d %H:%M:%S} | {:>3} C | {:>3} F | {:>2} %".format(
                now,
                temp_c,
                temp_f,
                result.humidity,
            )
            last_attempt_status = "Last attempt: success"
        else:
            last_attempt_status = "Last attempt: error {:d} at {:%H:%M:%S}".format(
                result.error_code,
                now,
            )

        status = "{}\n{}".format(last_valid_status, last_attempt_status)
        sys.stdout.write(CLEAR_SCREEN + status)
        sys.stdout.flush()

        sleep_for = max(0.0, MIN_SAMPLE_INTERVAL - (time.monotonic() - loop_started))
        time.sleep(sleep_for)
except KeyboardInterrupt:
    print()
finally:
    GPIO.cleanup()