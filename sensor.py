#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)

#define the pin that goes to the circuit
pin = 16
samples = 10

def set_pin_low_input(pin):
    #Output on the pin for
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def discharge_capacity(pin):
    set_pin_low_input(pin)

    while (GPIO.input(pin) != GPIO.LOW):
        time.sleep(0.1)
    time.sleep(0.1)

def charge_time_ms (pin):
    count = 0

    discharge_capacity(pin)
    #Change the pin back to input
    GPIO.setup(pin, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(pin) == GPIO.LOW):
        count += 1
        time.sleep(0.001)
    return count


start_time = time.time()
times = []

print("Discharging")

discharge_capacity(pin)
print("Start measurement")
#Catch when script is interrupted, cleanup correctly
try:
    while True:
        while len(times) < samples:
            charge_time = charge_time_ms(pin)
            #print(charge_time)
            times.append(charge_time)

        average_time = sum(times) / float(len(times))
        print( datetime.now().strftime('%Y-%m-%d %HH:%MM:%SS') + ", " +str(average_time))
        times = []

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()


