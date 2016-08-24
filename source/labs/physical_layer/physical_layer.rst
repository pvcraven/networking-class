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
you closer to the Manchester encoding protocol that was originally used for
things like Ethernet, and is even used for IR based TV remotes.

After each step you complete, call me over. Let me see that it is working, ask
questions to make sure you understand, and then I'll give you the grade.
Don't skip steps.

========  ===== ======
Step      Grade Points
========  ===== ======
No steps  F     0
Step 1    C-    70
Step 2    C+    77
Step 3    B-    80
Step 4    B     85
Step 5    B+    88
Step 6    A-    92
Step 7    A     98
========  ===== ======

If you are new to the Linux command line, which many of you are, ask questions!
You can also find a lot on line. I recommend this `linux command line tutorial`_
and this `command line cheat sheet`_. If you find something you like better, make
sure to tell me.

Remember: Use 'python3' to run your program. The 'python' command will use
python version 2, which won't work with our code.

Step 1: Dual Blinking LEDs
^^^^^^^^^^^^^^^^^^^^^^^^^^

Start with the tutorial to blink an LED. Make sure you have that working.

Get two LEDs to blink at the same time. Use pins 12 and 17. Blink
both a green and red LED at the same time.

This is an example, with a 1 second blink time.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/mXCQbWq5w3Q" frameborder="0" allowfullscreen></iframe>


Step 2: Encode a message
^^^^^^^^^^^^^^^^^^^^^^^^

Look at the bit shifting tutorial. Encode a message.
Have one LED blink when there is a one, and not blink when there is a zero.
The clock LED should blink on/off for each change bit that you have.

.. image:: ../../chapters/physical_layer/clock_signal.svg
    :width: 500px
    :align: center


You should set the LEDs off to begin with. You may need a separate program
to make sure the LEDs start in that state.
Keep track of the clock with a Boolean that you flip between
true and false.

Go ahead and still print the binary numbers as well, so we can confirm the
message was received in Step 3.

Here is an example. The green LED is the 'clock' and the red led blinks red
for a one, and off for a zero. The delay between each clock is 0.1 seconds. Each
bit takes 0.2 seconds to transmit.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/7Ef11hFo5lo" frameborder="0" allowfullscreen></iframe>

Step 3: Receive a signal
^^^^^^^^^^^^^^^^^^^^^^^^

* Get another Raspberry Pi.
* You can keep the LEDs attached.
* Run a wire to tie the grounds together. Do it on the 3.3v side.
* Run a wire from pin 12 on one Pi to a 220 ohm
  (`red red brown gold <http://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-resistor-color-code-4-band>`_) resistor.
* Run the 220 ohm resistor to pin 12 on the other Pi.
* Run a wire from pin 17 on one Pi to a 220 ohm resistor.
* Run a jumper from that resistor to pin 17 on the other Pi.
* Run the program from Step 2. Go to the tutorial
  :ref:`gpio_tutorial`.
  Run the example code :ref:`read_wire_callback`.
  The read program should be able to detect state changes. If it doesn't, stop
  here and debug.

Step 4: Decode a signal
^^^^^^^^^^^^^^^^^^^^^^^

* Adjust your step 3 program to print out 1's and 0's. Every 8 bits, print
  a new line.
* In order to do something every 8 bits, you are going to need a counter variable.
  It will need to exist in the function and increase each time the function is
  called. But wait! Variables in a function are reset each call. We need a way
  around this.

  There are two ways to do this. The evil way, and the proper way.

  * Evil way: Use global variables. Create a variable outside the function and
    set it to a value. Then at the start of the function, declare the variable
    as global.
  * Proper way: Use static function variables. This are variables that don't
    change between function calls. See below for examples of both ways.

.. code-block:: python

   # Evil way: Global variables
   x = 1

   def my_function():
       global x

       # This will increase x
       x += 1

.. code-block:: python

   # Proper way
   def my_function():
       # This will increase x
       my_function.x += 1

   my_function.x = 0


* You may need a small program to reset the state of the pins before you run
  your program. Otherwise you'll get an extra starting bit.
* It may take some work to keep from adding an extra bit or dropping an bit
  when your program runs.

Your final result should look something like the video below. One terminal
shows the sending computer, the other terminal shows the receiving computer.

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/n61MLYCA_p0" frameborder="0" allowfullscreen></iframe>

You can try adjusting the clock delay to see how fast you can receive data. I was
able to take the clock to 0.0001 and still reliably transmit data.

Step 5: Convert decoded bits to bytes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Change your program so it decodes the individual bits, and into an
  array of bytes. Print the message sent from the sending computer.


Step 6: Manchester encoding
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update your code so you can send using `Manchester Encoding`_.

* You should always transition high to low when you have a zero.
* You should always transition low to high when you have a one.
* You may need to transition mid-way to prep for the next bit.
* You can modify the sending code in step 2 to do this.
  The code for step 6 should be similar in length to step 2. Mine was just five
  lines longer.


Step 7: Manchester decoding
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Write code so you can receive using `Manchester Encoding`_.

* Start with your code from Step 4.
* To make things easier, create a variable here with the same clock speed as
  the clock speed used in Step 6.
* Create a program that does a callback when it detects a rising or falling edge.
* Read the channel. If it is high, then print low->high, else print high->low
* Calculate the time between transitions. You can get the current time with
  cur_time = time.time() in Python. Print the time between transitions along with
  the transition from the prior step.
* Don't print the clock anymore. But if the interval is larger than
  clock_speed + clock_speed / 2, you know you have a data bit. So print out the
  proper data bit. (You'll be skipping some bits. We'll get to that in a bit.
  Pardon the pun.)
* Create a static Boolean variable in your callback. I'll call it "data_bit".
  If time_interval > clock_speed + clock_speed / 2 set data_bit to False. This is
  because the next transition will NOT be a data bit.
* Update you 'if time_interval > clock_speed + clock_speed / 2' to also trigger
  if the data_bit is true or we have a long time interval.
* Update 'if time_interval > clock_speed + clock_speed / 2' so that if it
  DOESN'T trigger, set data_bit to be True, because the next bit will be a data
  bit.
* Come up with a way to keep from losing bits when the communication starts.


.. _Manchester Encoding: https://en.wikipedia.org/wiki/Manchester_code
.. _Raspberry Pi: https://www.raspberrypi.org/products/raspberry-pi-3-model-b/
.. _command line cheat sheet: http://cheatsheetworld.com/programming/unix-linux-cheat-sheet/
.. _linux command line tutorial: http://linuxcommand.org/index.php
