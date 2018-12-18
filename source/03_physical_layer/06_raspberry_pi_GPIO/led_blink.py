# Import the time library so we can pause the program for a specific time.
import time

# Use the Raspberry Pi library to control the general purpose input output
# (GPIO) pins.
import RPi.GPIO as GPIO

# State how we will specify our pin numbers.
# For a more detailed explanation, see here:
# http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
GPIO.setmode(GPIO.BCM)

# Say we will be outputting on pin 17:
GPIO.setup(17, GPIO.OUT)

# Loop forever
while True:

    # Set pin 17 high. (Turn it on.)
    GPIO.output(17, GPIO.HIGH)

    # Wait for a second
    time.sleep(1)

    # Set it low. (Turn it off.)
    GPIO.output(17, GPIO.LOW)

    # Wait for a second
    time.sleep(1)
