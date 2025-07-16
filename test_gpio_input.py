#!/usr/bin/python3
import OPi.GPIO as GPIO
import time

SENSOR_PIN = "PH2"  # Physical Pin 11 = GPIO PH2 on Orange Pi Zero 2W

GPIO.setmode(GPIO.SUNXI)  # Use SUNXI mode for Orange Pi
GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
    while True:
        state = GPIO.input(SENSOR_PIN)
        if state:
            print(" DRY soil (no moisture)")
        else:
            print(" WET soil (moisture detected)")
        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting. Cleaning up GPIO...")
    GPIO.cleanup()
