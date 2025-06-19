# How to build a simple ambient temperature monitor
**Author:** Miki Lamberg, ml227cr

When I started this project, the initial idea was to monitor the household temperature, since the ambient temperature in my household can significantly vary during summer and massively impact the proofing of my pizza doughs. I began with a basic starter kit that included a thermistor, an _analog sensor_, rather than something like a _digital_ DHT11 (which measures temperature and humidity), deeming it redundant for my end purposes. I simply wanted a temperature monitor which would ping me if the temperature went below or above X or Y degrees, allowing me to take appropriate measures for the pizza dough (e.g. placing it in the fridge if too warm, or opposite if too cold).

With either a thermistor (analog) or DS18B20* (digital), building this monitor using this tutorial should take approximately 10–15 hours.

* I will elaborate on this in # Objective below.


# Objective

As mentioned in the project overview, the initial objective was to create a sensor that monitors the ambient temperature where my pizza dough usually rests (the kitchen), and ping me on Discord if the temperature reaches a certain threshold so I could take the appropriate action. This would allow me to be do other things and not constantly worry about the fluctuating temperature - I would instead receive pings via the Discord application on my mobile phone.

However, as the project progressed, I realized I would want more than just ambient temperature readings at some point — I would want to monitor the actual temperature of the dough itself. Reading the temperatures of the dough would make for more accurate readings because it's affected by kneading and our body temperature which means it often has a different temperature than the ambient temperature.

After discussions with TA's I was given the recommendation to try a DS18B20*, a *digital* temperature sensor which is food safe and can be inserted into the actual dough**, this was an excellent idea which I, unfortunately, did not attempt to build due to other commitments.
<br>

<small>* DS18B20</small>
<br>
<img src="./images/ds18b20.png" width="150"><br>
<small>** I am not quite sure if the dough, in the proofing process, would "consume" the probe, which is why I want to leave a disclaimer.</small>


# Material
I chose the Basic Starter Kit by Freenove as recommended by the course management. Seeing as it was my first encounter with this kind of tech, I found it reasonable.
The following items were used in this project. I've included the starter kit as a whole, but also the individual components that I actually used from that base kit. How they were used will follow in chapters below.

| Component                                                                                                                         | Image                                                 | Description                                                      | Cost                |
|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|------------------------------------------------------------------|---------------------|
| 1x [Freenove Basic Starter Kit](https://www.amazon.se/Freenove-Raspberry-Dual-core-Cortex-M0-Microcontroller/dp/B0BJ1QC6X8/?th=1) | <img src="./images/starter_kit.png" width="450">      | Starter kit including the Microcontroller and various components | ~360 SEK            |
| 1x Raspberry Pi Pico W                                                                                                            | <img src="./images/pico_w.png" width="150">           | Microcontroller (MCU) with Wi-Fi enabled                         | *incl. in starter kit* |
| 1x USB-A to Micro-USB Cable                                                                                                       | <img src="./images/usb_cable.png" width="150">        | USB cable between MCU and PC                                     | *incl. in starter kit* |
| 1x 220Ω Resistor                                                                                                                  | <img src="./images/220ohmresistor.png" width="150">   | Current-limiting resistor for optional LED                       | *incl. in starter kit* |
| 1x 10kΩ Resistor                                                                                                                  | <img src="./images/10kohmresistor.png" width="150">   | Used in voltage divider with thermistor                          | *incl. in starter kit* |
| x Jumper Wires                                                                                                                    | <img src="./images/jumper_wires.png" width="150">     | Used to connect components on the breadboard                     | *incl. in starter kit* |
| 1x Thermistor                                                                                                                     | <img src="./images/thermistor.png" width="150">       | Analog temperature sensor                                        | *incl. in starter kit* |
| 1x LED (*optional*)                                                                                                               | <img src="./images/led.png" width="150">              | Red LED for visual debugging (e.g., temperature alert)           | *incl. in starter kit* |


# Computer setup

### Setting up the Pico

Before anything, the Pico needs to be flashed with MicroPython firmware. You can download the latest firmware (v.1.25.0 as of 18/6-2025) [here](https://micropython.org/download/RPI_PICO_W/). Follow these steps to flash the firmware:

1. Hold the BOOTSEL button on your Raspberry Pi Pico.

2. While holding the button, plug the Pico into your computer via USB.

3. The Pico should appear as a removable USB drive named RPI-RP2 which is the Pico storage.

4. Drag and drop the downloaded .uf2 firmware file onto this USB drive.

5. After a few seconds, the Pico will automatically reboot — the drive will disappear, indicating that the firmware was successfully installed.

6. To confirm the board is ready, unplug and plug the Pico back in - it should no longer show up as a USB drive. Done!

---

### Setting up for a Linux environment (Ubuntu 20.04/22.04/24.04) with Visual Studio Code

This guide works for Ubuntu and most Debian-based Linux distributions.

### Step 1: Install Node.js, npm and Python

Open your terminal and run:
```
sudo apt update && sudo apt upgrade -y
sudo apt install -y nodejs npm
```

Check if Node.js and npm were correctly installed:
```
node --version
npm --version
```

You should see numbers like `v22.xx.x` and `10.x.x`.

You'll also need Python and the package manager `pip`.
```
sudo apt install python3-pip
sudo pip3 install --upgrade pip
```
This ensures you have the latest version of `pip` to install any required Python tools.


### Step 2: Install Visual Studio Code

If VS Code is not yet installed on your machine, download it via the official .deb installer [here](https://code.visualstudio.com/Download).

Run the installer (double-click the .deb file) or use the terminal with the following command, assuming the file is in the Downloads folder:
```
sudo dpkg -i ~/Downloads/code_*.deb
```

Once installed, open Visual Studio Code. If it was already open, restart it so it can detect Node.js and other installed tools and packages.

### Step 3: Install the MicroPico extension in VS Code

The MicroPico extension provides auto-completion, REPL access, and workspace integration for Raspberry Pi Pico boards running MicroPython.

1. Open Visual Studio Code

2. Go to the Extensions view (or press Ctrl+Shift+X)

3. Search for: "MicroPico" and install the extension by "paulober" (as of 18/6-2025)


Once installed, make sure the Pico is plugged in and then:

1. Press `CTRL + SHIFT + P` to open the Command Palette

2. Type "MicroPico: Connect" and press `Enter`

2. A MicroPico REPL shell will open — your Pico is now connected!

To test the connection, type the following in the shell:

```print("Hello from Pico!")```

Done!

# Putting everything together

_(Coming soon)_


# Platform

For this project, I chose **Adafruit** because of its simplicity and beginner-friendly UI. I didn’t have much time to create an elaborate setup, so I aimed for a stable, easy-to-replicate solution. No complex configuration was necessary.

The free tier of Adafruit offers more than enough features for this project's purpose. Here are a few key features that convinced me that Adafruit was an excellent choice of platform for my needs:

* Up to 10 feeds
* Built-in alert system and webhook integrations (more on this below)
* Cloud-hosted data feed (no local server needed)
* MQTT support for the Raspberry Pi Pico W and MicroPython
* Visual dashboard with charts, sliders, buttons etc.

The course guide also provided a great example of how to send events from Adafruit to Discord using a webhook. I adopted this method to create an alert system that notifies me via Discord when the ambient temperature reaches a certain threshold. This allows me to take action even when I’m not in the kitchen where the dough is proofing.

All of this made Adafruit a solid choice — quick to set up, beginner-friendly, and powerful enough to make this small beginner-project possible.

# The code

While I had some experience with Python since before, the whole IoT-aspect including electronics made me want to be cautious because im a super rookie when it comes to hardware and electricity.

With that in mind, I don't want to exaggerate something that in it's essence is **very** simple, so here goes.


This is main function. The function is responsible for reading the ambient temperature, converting it to celcius degrees and finally sending converted value to Adafruit where it is registered and stored.
```python
def send_temperature():
    raw_value = thermistor_pin.read_u16() # raw value read as millivolts
    temperature = adc_to_celsius(raw_value) # converts millivolts to Celsius degrees
    print(f"Sending temperature to Adafruit feed: {temperature} Celcius degrees")
    client.publish(keys.AIO_TEMPS_FEED, str(temperature)) # send message as string payload to conform to MQTT message policy

    # Flash LED briefly to visually indicate that data has been transferred
    led.on()
    time.sleep(0.5)
    led.off()
```

The conversion is handled by the helper function adc_to_celsius(), which takes the raw thermistor reading as input. This function uses the Beta parameter equation, a simplified form of the Steinhart-Hart equation, to convert the ADC (Analog-To-Digital Converter) value into temperature in Celsius by calculating the thermistor's resistance and then estimating the temperature.

```python
# Constants
BETA = 3950
KELVIN_CONSTANT = 273.15

# ADC conversion function to give Celsius
def adc_to_celsius(x):
    return (1 / (log(1 / (65535 / x - 1)) / BETA + 1 / 298.15) - KELVIN_CONSTANT)
```

# Transmitting the data / connectivity

_(Coming soon)_


# Presenting the data

Below you can see a standard line chart and feed data with typical attributes such as 'data', 'created at' and the possibility to add, download and filter data.
<img src="./images/adafruit_temps_feed.png" alt="adafruit_temp_line_chart">
<img src="./images/adafruit_temps_feed2.png" alt="adafruit_temp_feed_data">


# Finalizing the design

_(Coming soon)_

