import time
import RPi.GPIO as GPIO

# This is a callback function that will be called whenever we have a high/low
# or low/high change in the signal.
def my_callback(channel):
	if GPIO.input(channel):
		print("Channel {} is high".format(channel))
	else:
		print("Channel {} is low".format(channel))

# Set pin 12 up for input
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)

# Now we have to 'register' the callback function so that the GPIO library
# will call the function when the change occurs on pin 12. The BOTH means
# it is called on both rising and falling changes.
GPIO.add_event_detect(12, GPIO.BOTH, callback=my_callback)

# Now just wait forever.
print("Running")
while True:
    time.sleep(10)
    print("Still running")
