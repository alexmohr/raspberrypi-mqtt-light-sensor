# Light Sensor MQTT 
This repsository contains a simple light sensor for the raspberry pi. 
Because the pi does not have any analog inputs the scripts measures how long it takes to charge a capacitor until the pi recognizes the voltage as logical one.

The script will takes 10 measurements, averages them and publishes the result via MQTT.
In my setup the MQTT data will be read by home assistant and is used to control the lights.

## Installation
`pip install raspberrypi-mqtt-light-sensor` ( not available yet  )


