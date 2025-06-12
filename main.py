from time import sleep
from machine import Pin, ADC
from thermistor import adc_to_celsius

# Configure GPIO 0 (labeled GP0 on Pico pinout, physical pin 1) as output for the LED.
# First argument refers to GP0, not the physical pin (1).
led = Pin(0, Pin.OUT)

# Pin.IN tells the MCU this is an input to read from
# PULL_UP turns on an internal resistor that keeps pin high (1) when button is not pressed, and 0 when pressed.
button = Pin(15, Pin.IN, Pin.PULL_UP)

# Thermistor pin setup
thermistor_pin = ADC(26)

# Activate LED blinking loop
# while True:
#     led.value(1)
#     time.sleep(0.2)
#     led.value(0)
#     time.sleep(0.3)

# Activate LED with button press

prev_button_state = 1 # i.e. not pressed down

while True:
    raw_value = thermistor_pin.read_u16() # raw value read as millivolts

    temperature = adc_to_celsius(raw_value) # converted millivolts to Celcius degrees

    current_button_state = button.value()

    if button.value() == 0 and prev_button_state == 1:
        led.on() # same as led.value(1)
        print("The temperature here is: {} degrees Celcius".format(round(temperature, 1)))
    elif current_button_state == 1 and prev_button_state == 0:
        led.off() # same as led.value(0)
        
    prev_button_state = current_button_state
    sleep(0.01) # short pause