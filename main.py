import time # imports methods from time library
from machine import Pin, ADC
from thermistor import adc_to_celsius # imports celcius converting method
from mqtt import MQTTClient # For use of MQTT protocol to talk to Adafruit IO
import wifiConnection # Contains functions to connect/disconnect from WiFi
import keys # Contains all keys used here


# CONFIGURATION SETTINGS

# Configure GPIO 0 (labeled GP0 on Pico pinout, physical pin 1) as output for the LED.
# First argument refers to GP0, not the physical pin (1).
led = Pin(0, Pin.OUT)

# Thermistor pin setup
thermistor_pin = ADC(26)



def send_temperature():
    raw_value = thermistor_pin.read_u16() # raw value read as millivolts
    temperature = adc_to_celsius(raw_value) # converted millivolts to Celcius degrees
    print("Sending temperature to Adafruit feed: ", temperature)
    client.publish(keys.AIO_TEMPS_FEED, str(temperature)) # send message as string payload to conform to MQTT message policy

    led.on()
    time.sleep(0.3)
    led.off()


# Try WiFi Connection
try:
    ip = wifiConnection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Use the MQTT protocol to connect to Adafruit IO, not currently subscribed to messages.
client = MQTTClient(keys.AIO_CLIENT_ID, keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)
client.connect()

try:
    while True:
        send_temperature()
        time.sleep(60)
except Exception as e:
    print("Something went wrong:", e)
finally:
    client.disconnect()
    wifiConnection.disconnect()
    print("Disconnected cleanly.")