from time import sleep # import sleep for implementing delay
from machine import Pin, ADC
from thermistor import adc_to_celsius # imports celcius converting method
from mqtt import MQTTClient # For use of MQTT protocol to talk to Adafruit IO
import boot # Contains functions to connect/disconnect from WiFi
import keys # Contains all keys used here


# CONFIGURATION SETTINGS

# Configure GPIO 0 (labeled GP0 on Pico pinout, physical pin 1) as output for the LED.
# First argument refers to GP0, not the physical pin (1).
led = Pin(0, Pin.OUT)

# Thermistor pin setup
thermistor_pin = ADC(26)

def send_temperature():
    raw_value = thermistor_pin.read_u16() # raw value read as millivolts
    temperature = adc_to_celsius(raw_value) # converts millivolts to Celsius degrees
    print(f"Sending temperature to Adafruit feed: {temperature} Celcius degrees")
    client.publish(keys.AIO_TEMPS_FEED, str(temperature)) # send message as string payload to conform to MQTT message policy

    # Flash LED briefly to visually indicate that data has been transferred
    led.on()
    sleep(0.5)
    led.off()


# Try WiFi Connection
try:
    ip = boot.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Use the MQTT protocol to connect to Adafruit IO, not currently subscribed to messages.
client = MQTTClient(keys.AIO_CLIENT_ID, keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)
client.connect()

try:
    while True:
        send_temperature()
        sleep(30)
except Exception as e:
    print("Something went wrong:", e)
finally:
    client.disconnect()
    boot.disconnect()
    print("Disconnected cleanly.")