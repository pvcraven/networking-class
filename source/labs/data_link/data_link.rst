Lab 2: Data Link Layer
----------------------

Pass as many of the steps below as you can.

========  ===== ======
Step      Grade Points
========  ===== ======
No steps  F     0
Step 1    C-    60
Step 2    C+    70
Step 3    B-    80
Step 4    B     85
Step 5    B+    88
Step 6    A-    92
Step 7    A     98
========  ===== ======

Make your own patch cable
^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the patch cable tutorial to make your own patch cable. For credit, all
wires must pass the cable connection tester.

Vocabulary
^^^^^^^^^^

Explain each of the items below. Do this orally or via written report.

Media Access Control
	* CSMA, plus `CSMA/CD`_ and `CSMA/CA`_
	* `Token Ring`_
Concepts:
    * Tunneling_

Protocols
	* ARP_
	* PPP_
	* L2TP_
	* NDP_

Wireless Encryption Types
    * Open
    * WEP
    * WPA-PSK (AES)
    * WPA2-PSK (TKIP)
    * WPA2-PSK (AES)
    * WPA2-Enterprise

Pseudo-security
	* SSID hiding
	* MAC ID filtering


Run Wireshark
^^^^^^^^^^^^^

Read the chapter on the :ref:`datalink-layer`. Next, go through
the :ref:`wireshark-tutorial`.

Find a packet that you captured. Sit and explain what you are seeing at Layer 2,
similar to how the chapter on the :ref:`datalink-layer` did. Also, talk about what
is in an Ethernet frame that *doesn't* show up on Wireshark.

Send raw Ethernet frames
^^^^^^^^^^^^^^^^^^^^^^^^

Go through the :ref:`raw-ethernet-tutorial`. Successfully send/receive packets
between two Raspberry Pi computers with this tutorial.

Fast data sending part 1
^^^^^^^^^^^^^^^^^^^^^^^^

Change your raw Ethernet program and see how fast you can send data over
the *wire* using raw Ethernet packets.

For the sender:
	* Send as much data as you can in a packet. Just send 0's or other random
	  garbage.
	* Wait x milliseconds.
	* Send more data.
	* Repeat for about five seconds worth transmission. Adjust the number of repeats
	  as needed.

On the receiving end:
	* Count the packets you received. See if you lost any. Change the time delay
	  and see how fast you can make it before losing packets.


Fast data sending part 2
^^^^^^^^^^^^^^^^^^^^^^^^

Repeat the prior experiment.

Find out:
	* How fast can you send data over wired with multiple people? Does it change?
	* How fast can you send data over wireless vs. wired?
	* How fast can you send data over wireless with multiple people at the same time?

Write down the numbers and the conditions that you tested in. Repeat the tests
a few times and see how consistent they are. Call me over, or write up the results
and send them in.

Data loss
^^^^^^^^^

See if you can spot a pattern in data loss:
	* Right before the data that you send, also send an sequential number marking the
	  current Ethernet frame you are on. Start at 1 and keep going.
	* On the receiver, decode the frame number that you get.
	* Print the frame numbers that you don't get.
	* Get to a spot where you have frame loss. How do the frames drop? Just random
	  ones? Are they in a clump?

.. _CSMA/CD: https://en.wikipedia.org/wiki/Carrier_sense_multiple_access_with_collision_detection
.. _CSMA/CA: https://en.wikipedia.org/wiki/Carrier_sense_multiple_access_with_collision_avoidance
.. _Token Ring: https://en.wikipedia.org/wiki/Token_ring
.. _ARP: https://en.wikipedia.org/wiki/Address_Resolution_Protocol
.. _PPP: https://en.wikipedia.org/wiki/Point-to-Point_Protocol
.. _Tunneling: https://en.wikipedia.org/wiki/Tunneling_protocol
.. _L2TP: https://en.wikipedia.org/wiki/Layer_2_Tunneling_Protocol
.. _NDP: https://en.wikipedia.org/wiki/Neighbor_Discovery_Protocol
