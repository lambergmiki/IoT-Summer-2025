import time
from machine import Pin, ADC
from math import log

# Configure GPIO 0 (labeled GP0 on Pico pinout, physical pin 1) as output for the LED.
# First argument refers to GP0, not the physical pin (1).
led = Pin(0, Pin.OUT)

# Pin.IN tells the MCU this is an input to read from
# PULL_UP turns on an internal resistor that keeps pin high (1) when button is not pressed, and 0 when pressed.
button = Pin(15, Pin.IN, Pin.PULL_UP)

# Activate LED blinking loop
# while True:
#     led.value(1)
#     time.sleep(0.2)
#     led.value(0)
#     time.sleep(0.3)

# Activate LED with button press
while True:
    if button.value() == 0:
        led.on() # same as led.value(1)
    else:
        led.off() # same as led.value(0)
        time.sleep(0.01) # short pause