#!/usr/bin/python3
from bottle import route, run, response
import OPi.GPIO as GPIO
import time

@route('/')
def get_humidity():
        # Correct GPIO name for physical pin 11
        SENSOR_PIN = "PH2"
        # Use SUNXI pin naming mode
        GPIO.setmode(GPIO.SUNXI)
        GPIO.setup(SENSOR_PIN, GPIO.IN)
        # Give the sensor a brief moment to settle
        time.sleep(0.5)
        # Read the sensor
        state = GPIO.input(SENSOR_PIN)
        GPIO.cleanup()
        # Output result
        return "dry" if state else "wet"

run(host="0.0.0.0", port=19234)
