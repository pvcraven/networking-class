Lab 1: Manage your own physical layer
-------------------------------------

Start with the tutorial to blink an LED. Make sure you have that working.

Remember: Use 'python3' to run your program. The 'python' command will use
python version 2, which won't work with our code.

Step 1
^^^^^^

Get two LEDs to blink at the same time. Use pins 12 and 17. Blink
both a green and red LED at the same time.

This is an example, with a 1 second blink time.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/QzA1KSAlpSw" frameborder="0" allowfullscreen></iframe>

Step 2
^^^^^^

Look at the bit shifting tutorial. Encode a message.
Have one LED blink when there is a one, and not blink when there is a zero.
The other LED should blink for each change in the bit that you have.

Go ahead and still print the binary numbers as well, so we can confirm the
message was received in Step 3.

You should set the LEDs off to begin with, and wait a second before starting
your message. Keep track of the clock with a Boolean that you flip between
true and false.

Here is an example. The green LED is the 'clock' and the red led blinks red
for a one, and off for a zero. The delay between each bit is 0.25 seconds.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/mXCQbWq5w3Q" frameborder="0" allowfullscreen></iframe>

Step 3
^^^^^^

* Get another Raspberry Pi.
* You can keep the LEDs attached.
* Run a wire to tie the grounds together. Do it on the 3.3v side.
* Run a wire from pin 12 on one Pi to a 220 ohm resistor.
* Run the 220 ohm resistor to pin 12 on the other Pi.
* Run a wire from pin 17 on one Pi to a 220 ohm resistor.
* Run a jumper from that resistor to pin 17 on the other Pi.
* Run the program from Step 2, and the read_wire_wait.py program from the tutorial.
  The read program should be able to detect state changes. If it doesn't, stop
  here and debug.

Step 4
^^^^^^

* Adjust your step 3 program to print out 1's and 0's. Every 8 bits, print
  a new line.
* You may need to learn to use the 'global' keyword so your callback can modify
  a variable to track what bit you are on. Ask your instructor.
* You may need a small program to reset the state of the pins before you run
  your program. Otherwise you'll get an extra starting bit.