import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

while True:

    # Set wire high
    print("Sending High")
    GPIO.output(12, GPIO.HIGH)

    # Wait one second
    time.sleep(1)

    # Set wire low
    print("Sending Low")
    GPIO.output(12, GPIO.LOW)

    # Wait one second
    time.sleep(1)
