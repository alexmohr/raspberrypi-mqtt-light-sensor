"""
Measures the time how long it takes to charge a capacity, averages 10 measurement 
and publishes the result via mqtt. 
"""

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json
import math
import argparse

from datetime import datetime

GPIO.setmode(GPIO.BCM)

# todo export into configuration file
__PIN = 25
__SAMPLES = 5
__MIN_TIME_SECONDS = 10
__MQTT_SERVER = '127.0.0.1'
__MQTT_TOPIC = 'sensors/brightness'


def discharge_capacity(pin):
    """
    Discharge the capicity until we read low on the input pin
    """

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

    while (GPIO.input(pin) != GPIO.LOW):
        time.sleep(0.1)
    time.sleep(0.1)


def charge_time_ms(pin):
    """
    Measure how long it takes until the value on the pin is HIGH
    """

    discharge_capacity(pin)

    # Change the pin back to input
    GPIO.setup(pin, GPIO.IN)

    # wait until pin is high
    start_time = datetime.now()
    while (GPIO.input(pin) == GPIO.LOW):
        time.sleep(0.001)

    delta_t = datetime.now() - start_time
    elapsed = delta_t.total_seconds() * 1000 + (delta_t.microseconds / 1000)
    return math.ceil(elapsed)


def mqtt_publish(mqtt_server, topic, value):
    """
    Publishes the new measured value via mqtt. 
    """
    mqttc = mqtt.Client()
    mqttc.connect(__MQTT_SERVER)

    mqtt_value = json.dumps({'brightness': value})
    mqttc.publish(topic, mqtt_value)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Raspberry pi mqtt LDR.')

    parser.add_argument('-p', '--pin', required=False,
                        help='Defines the GPIO pin used.')

    parser.add_argument('-m', '--mqtt-host', required=False,
                        help='Defines the MQTT server.')

    parser.add_argument('-s', '--seconds', required=False,
                        help='How long the measurement is before mqtt push. Values will be averaged.')

    parser.add_argument('-t', '--topic', required=False,
                        help='Defines the mqtt topic.')

    args = parser.parse_args()
    
    if args.pin is not None:
        __PIN = args.pin

    if args.seconds is not None:
        __MIN_TIME_SECONDS = args.seconds

    if args.mqtt_host is not None:
        __MQTT_SERVER = args.mqtt_host

    if args.topic is not None:
        __MQTT_TOPIC = args.topic


    times = []

    discharge_capacity(__PIN)

    try:
        while True:
            start_time = datetime.now()
            delta_t = datetime.now() - start_time

            # at least 1 sample must be measured
            while len(times) < 1 or delta_t.total_seconds() < __MIN_TIME_SECONDS:
                charge_time = charge_time_ms(__PIN)
                times.append(charge_time)
                delta_t = datetime.now() - start_time
            average_time = math.ceil(sum(times) / float(len(times)))
            mqtt_publish(__MQTT_SERVER, __MQTT_TOPIC, average_time)
            times = []

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
