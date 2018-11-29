.. _datagram_tutorial:

Send and Receive Datagrams
==========================

Sending a datagram is easy. Below is Python code to do it:

Send Datagram
-------------
.. literalinclude:: send_datagram.py
    :linenos:
    :language: python

Receive
-------

Receiving data usually is done one of several ways:

* Blocking: Use a command to receive data. The program pauses and won't continue
  until data is received. Because the program can't do anything while
  we are waiting, we will usually spin off the send/receive functions into different
  threads.
* Non-blocking: Use a command to receive data. If no data is available, the command
  doesn't wait. It returns immediately.
* Time-out: Wait for a certain number of milliseconds for data. If there's no
  data after x milliseconds, then time-out.
* Callback: Register a function that we write which will get called when we receive data.

Receive Datagram - Blocking
---------------------------

.. literalinclude:: receive_datagram.py
    :linenos:
    :language: python

Receive Datagram - Non-Blocking
-------------------------------

.. literalinclude:: receive_datagram_nonblocking.py
    :linenos:
    :language: python

Packet Structure
----------------

I have used these programs to send myself a packet. I captured it with
Wireshark. Let's deconstruct the packet.

.. image:: udp_01.png
    :width: 640px
    :align: center
    :alt: alternate text

Ethernet
^^^^^^^^

The first six bytes are the destination address. The first three of those are
unique to each device, the second three are unique to the manufacturer.
In my case, the destination computer motherboard was built by ASRock.

The IEEE keeps a
`registry <https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries>`_
of what manufacturer gets what 3 digit MAC address. You can do a
`MAC address lookup <http://www.macvendors.com/>`_ to find out the manufacturer.

.. image:: udp_02.png
    :width: 640px
    :align: center
    :alt: alternate text

The next six bytes is the source address. This is **not** the computer that
originally sent the message. In this case, it is the Cisco router that is
between the source computer and the destination computer.

.. image:: udp_03.png
    :width: 640px
    :align: center
    :alt: alternate text

Then we set the type of Ethernet packet to Ethernet II using 0x0800.

.. image:: udp_04.png
    :width: 640px
    :align: center
    :alt: alternate text

IP
^^

Finally, we reach the TCP/IP part of the packet! The next byte 0x45 holds two
pieces of data. Four bits represent the version of TCP/IP we are using (TCPv4)
and the next to say how long the header is (20 bytes). Note that this is length
of the header, not the entire message. Together those eight bits gives us the next
byte.

.. image:: udp_05.png
    :width: 640px
    :align: center
    :alt: alternate text

Next we have some fields for prioritizing traffic. `Differentiated services`_
allows some packets to take priority over others. We aren't using them in
this case, so they are all left at zero.

.. image:: udp_06.png
    :width: 640px
    :align: center
    :alt: alternate text

The total length of this packet is 51 bytes. Which in hexadecimal is 0x33.

.. image:: udp_07.png
    :width: 640px
    :align: center
    :alt: alternate text

Next we have a packet ID field. This is used if a packet is fragmented so we can
reassemble based on the ID. It doesn't have much use otherwise.

While TCP/IP packets can be large, we often try to keep them small so that
fragmentation does not occur. There is a `Path MTU Discovery protocol`_ that
tries to figure out how large you can make a packet before it breaks up.

`This blog post <https://blog.cloudflare.com/path-mtu-discovery-in-practice/>`_
provides a nice example of someone debugging a network problem related to this.

.. image:: udp_08.png
    :width: 640px
    :align: center
    :alt: alternate text

Here we tell the network that we don't want this datagram fragmented into parts.

.. image:: udp_09.png
    :width: 640px
    :align: center
    :alt: alternate text

"Time to live:" (TTL) is an interesting field. By default, we start out at 64. Each
time we make a "hop" on the network we subtract one. When we hit zero the packet
is dropped.

Why do we do this? What if
we had a "circle" of computers. They took a packet and kept passing the packet
around the circle. Yet the destination wasn't in the circle. The packet could
stay there forever. And we could keep getting more packets like that, keeping
legitimate traffic from using the network.

Traceroute uses TTL. It keeps sending packets with one more added to the TTL
and figures out where the packet expires.

.. image:: udp_10.png
    :width: 640px
    :align: center
    :alt: alternate text

The next byte says that this is a UDP packet. What else can you pick?
`See this list <https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers>`_.

.. image:: udp_11.png
    :width: 640px
    :align: center
    :alt: alternate text

This is a checksum to make sure that the header is valid. Not sure what a
checksum is? `Click here to learn <https://en.wikipedia.org/wiki/IPv4_header_checksum>`_.

.. image:: udp_12.png
    :width: 640px
    :align: center
    :alt: alternate text

Next up, source IP address in hex:

.. image:: udp_13.png
    :width: 640px
    :align: center
    :alt: alternate text

Destination IP address in hex:

.. image:: udp_14.png
    :width: 640px
    :align: center
    :alt: alternate text

UDP
^^^

We are done with the IP part of the packet. Now on to the UDP part.

Source port:

.. image:: udp_15.png
    :width: 640px
    :align: center
    :alt: alternate text

Destination port:

.. image:: udp_16.png
    :width: 640px
    :align: center
    :alt: alternate text

Length of the data:

.. image:: udp_17.png
    :width: 640px
    :align: center
    :alt: alternate text

Checksum for the data portion:

.. image:: udp_18.png
    :width: 640px
    :align: center
    :alt: alternate text

Data/Payload
^^^^^^^^^^^^

Finally, the data.

.. image:: udp_19.png
    :width: 640px
    :align: center
    :alt: alternate text

.. _differentiated services: https://en.wikipedia.org/wiki/Differentiated_services
.. _Path MTU Discovery protocol: https://en.wikipedia.org/wiki/Path_MTU_Discovery