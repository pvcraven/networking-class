import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)

while True:

    # Wait for pin 12 to go high
    result = GPIO.wait_for_edge(12, GPIO.RISING)
    print("High")

    # Now wait for it to go low
    result = GPIO.wait_for_edge(12, GPIO.FALLING)
    print("Low")
