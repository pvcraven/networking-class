Lab 1: Manage your own physical layer
-------------------------------------

This lab is designed to promote a deeper understanding of the physical layer
by applying what you've learned to create your own implementation if the
physical layer.

We will be using two `Raspberry Pi`_'s to communicate. Rather than use the built-in
Ethernet or wireless, we'll control the voltage with our own programs we write.
We will also do the wiring ourselves.

Please work with another student so you have two Raspberry Pi's to communicate,
or work with a couple of the computers that I have.

Your grade for this lab depends on how many steps you complete. Each step gets
you closer to the protocol that was originally used for things like Ethernet,
and even your remote control.

========  =====
Step      Grade
========  =====
No steps  F
Step 1    C-
Step 2    C+
Step 3    B-
Step 4    B
Step 5    B+
Step 6    A-
Step 7    A
========  =====

If you are new to the Linux command line, which many of you are, ask questions!
You can also find a lot on line. I recommend this `linux command line tutorial`_
and this `command line cheat sheet`_. If you find something you like better, make
sure to tell me.

Step 1
^^^^^^

Start with the tutorial to blink an LED. Make sure you have that working.

Remember: Use 'python3' to run your program. The 'python' command will use
python version 2, which won't work with our code.

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
* It may take some work to keep from adding an extra bit or dropping an bit
  when your program runs.

Your final result should look something like the video below. One terminal
shows the sending computer, the other terminal shows the receiving computer.

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/n61MLYCA_p0" frameborder="0" allowfullscreen></iframe>

Step 5
^^^^^^

* Change your program so it decodes the individual bits, and into an
  array of bytes. Print the message sent from the sending computer.


Step 6
^^^^^^

Update your code so you can send using `Manchester Encoding`_


Step 7
^^^^^^

Update your code so you can receive using `Manchester Encoding`_

.. _Manchester Encoding: https://en.wikipedia.org/wiki/Manchester_code
.. _Raspberry Pi: https://www.raspberrypi.org/products/raspberry-pi-3-model-b/
.. _command line cheat sheet: http://cheatsheetworld.com/programming/unix-linux-cheat-sheet/
.. _linux command line tutorial: http://linuxcommand.org/index.php
