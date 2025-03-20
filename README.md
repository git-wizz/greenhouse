# Greenhouse
## Developing A Smart Greenhouse Monitoring System Prototype
You will design, implement, and test a data acquisition and visualisation
system using the VML6070 sensor (UV) and DHT11 sensor (temperature, humidity)
environmental sensor. The microcontroller will monitor the data and function as an
indicator to display the observed values. The system will use NeoPixel LEDs to
indicate the status of these values. The LED matrix will display a red light if the sensor
is not exposed to sufficient UV light. Conversely, if adequate light is detected, it will
show a green light.

## The system will:
1. Continuously collect the data from the sensors at regular intervals (e.g., every
second).
2. Transmit the collected data wirelessly via Wi-Fi using the MQTT protocol to a
designated broker.
3. Create a CSV file on the microcontroller's local storage device to store the received
data, ensuring proper time stamps and labelling for each data point.
4. Develop a visually appealing and interactive dashboard using Python's Streamlet
library that displays the recorded data.

## The dashboard should:
a. Offer multiple visualisation options (e.g., line charts, histograms) to cater to
different types of data and user preferences.
b. Allow dynamic interaction (e.g., zooming, filtering, drill-down) to facilitate in-
depth exploration of the data.
c. Provide clear labelling and titles for axes, legends, and other visual elements to
enhance readability and understanding.
