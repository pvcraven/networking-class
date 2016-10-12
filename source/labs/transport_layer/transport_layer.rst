Lab 4: Transport Layer
----------------------

========  ===== ======
Step      Grade Points
========  ===== ======
No steps  F     0
Step 1    F     55
Step 2    D     65
Step 3    C     75
Step 4    B     85
Step 5    A     95
Step 6    A     100
========  ===== ======

Packet Sizes
^^^^^^^^^^^^

* Read how `TCP handshaking`_ occurs when building a connection.
* Examine the code at :ref:`tcp_tutorial`.
* Run a Wireshark packet trace to see the data go across the line.
* Show the packet capture and explain the packets and how the connection is built.

Packet Sizes
^^^^^^^^^^^^

* Examine the code at :ref:`tcp_tutorial`.
* Set up your workspace so your sender and receiver are on different computers.
* Run a Wireshark packet trace to see the data go across the line.
* Figure out how many characters can you send before the data will be split
  into multiple packets.
* Show the packet capture and explain your results.

Data Transmission Rates and Packet Sizes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Examine the code at :ref:`tcp_tutorial`.
* Figure out a way to measure data transmission rates. For example, if your
  message was 2 bytes long, and you were able to send/receive 5,000 of these
  in 7 seconds, you have a data transmission rate of:

.. math::

  \frac{packets \cdot size}{time} = \frac{ 5000 \cdot 2}{7} = 1,429\:bytes/sec

* Steadily change how much data you send from one byte, up to 5,000.
* Graph the results
* Test the resulting speed if you keep the connection open, or if you close/open
  each time when sending data.
* For the best results, you may want to "toss" the first 100 packets or so,
  as those packets often have different timings.

Bouncing Balls
^^^^^^^^^^^^^^

The goal of this project is to get bouncing ball on the computer screen to pass
from one computer to another. So if you line up five laptops, the ball will
appear to bounce across all the screens.

* Examine the code at :ref:`tcp_tutorial`.
* Get a "bouncing ball" program to work. Either
  `this Pygame one <http://programarcadegames.com/python_examples/f.php?file=bouncing_rectangle.py>`_
  or `this Arcade one <https://pythonhosted.org/arcade/examples/bouncing_rectangle.html>`_
* Adjust the program so you can have any number of balls bouncing. I suggest creating
  a ball each time you hit the space bar.
* Create variables to hold what computer is to your left and right.

  * Set them for address and port on "left" and "right" side

* If the variables are set to null or None, ignore them and have the program
  operate as normal.
* If the variable is set, then when the ball hits the left or right side, open
  a connection, send the following numbers over the network:

``y,change_x,change_y<carriage return>``

For example:

``50,-3,2\n``

* Close the connection after sending.
* Add TCP listeners for the left and for the right.
* If you receive numbers, add a new ball with the appropriate y value and vector.
* Set up your computers so you get the ball bouncing between screens.
* Feel free to help each other out with the coding. If you are done, PLEASE be
  mindful of other people still coding. Don't make lots of noise and distract
  them from finishing. Stick around and help them integrate with your code.
* The code can be visually more pleasing if you include size and color.

Threaded Bouncing Balls
^^^^^^^^^^^^^^^^^^^^^^^

* Instead of non-blocking calls in your main program loop, figure out how to
  create separate receiving threads to manage the network connections. (No
  need to thread the sending.)

Foreign Bouncing Balls
^^^^^^^^^^^^^^^^^^^^^^

* Create a threaded on non-threaded bouncing ball program in a language other
  than Python. Like Java for example.

.. _TCP handshaking: https://en.wikipedia.org/wiki/Transmission_Control_Protocol

