import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)

while True:

    # Read from pin 12. We'll get a 0 or a 1.
    result = GPIO.input(12)

    if result:
        # If true (1), then print high
        print("High")
    else:
        # If false (0), then print low
        print("Low")

    # Wait a quarter second before we look again
    time.sleep(0.25)
