Networking Layer
================

What is the networking layer?
-----------------------------

The networking layer is the third layer of the OSI model. The networking
layer is responsible for routing. It can forward a packet of data from one
node (a computer or router) across multiple other nodes, to finally
arrive at its destination. It also makes sure that the data gets to the correct
program running on your computer.

The networking layer in action
------------------------------

Before we dive too far into the details, let's run a few commands to get an
overview of what is happening in the networking layer.

Finding your address
^^^^^^^^^^^^^^^^^^^^

Computers on the Internet have both a MAC address and an IP address. You
can see the address by typing ``ipconfig /all`` on the command line for Windows,
or ``ifconfig`` for Mac/UNIX/Linux computers

See the highlighted lines below. I used Windows to show both my physical
address (MAC address) and IP address.

.. code-block:: none
    :emphasize-lines: 16,20

    c:\>ipconfig /all

    Windows IP Configuration

       Host Name . . . . . . . . . . . . : cvr1834b
       Primary Dns Suffix  . . . . . . . : sc.loc
       Node Type . . . . . . . . . . . . : Hybrid
       IP Routing Enabled. . . . . . . . : No
       WINS Proxy Enabled. . . . . . . . : No
       DNS Suffix Search List. . . . . . : sc.loc

    Ethernet adapter Ethernet:

       Connection-specific DNS Suffix  . : sc.loc
       Description . . . . . . . . . . . : Broadcom NetLink (TM) Gigabit Ethernet
       Physical Address. . . . . . . . . : D0-50-99-07-6F-A9
       DHCP Enabled. . . . . . . . . . . : Yes
       Autoconfiguration Enabled . . . . : Yes
       Link-local IPv6 Address . . . . . : fe80::a9e4:9368:508d:c45c%2(Preferred)
       IPv4 Address. . . . . . . . . . . : 10.1.23.175(Preferred)
       Subnet Mask . . . . . . . . . . . : 255.255.0.0
       Lease Obtained. . . . . . . . . . : Monday, September 19, 2016 6:11:36 AM
       Lease Expires . . . . . . . . . . : Friday, September 23, 2016 12:45:54 PM
       Default Gateway . . . . . . . . . : 10.1.1.100
       DHCP Server . . . . . . . . . . . : 172.16.99.2
       DHCPv6 IAID . . . . . . . . . . . : 63983769
       DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-1E-1E-36-40-D0-50-99-07-6F-A9
       DNS Servers . . . . . . . . . . . : 198.206.243.21
                                           198.206.243.28
       NetBIOS over Tcpip. . . . . . . . : Enabled

Not just computers have IP addresses. Your wireless router has an IP address.
Your phone has an IP address. Every **node** that exists on the network has
an address.

Traceroute
^^^^^^^^^^

You can see the path between two nodes by using the ``tracert`` command on
Windows, or the ``traceroute`` command on MAC/Linux computers. Below
I can see the route the computer in my office takes to get to ``www.simpson.edu``.

First, I start at my computer ``10.1.23.175``. Then my first hop goes to ``10.1.1.100``.
The last stop is the computer that hosts ``www.simpson.edu`` at ``198.206.243.15``.

::

    c:\>tracert www.simpson.edu

    Tracing route to web2.simpson.edu [198.206.243.15]
    over a maximum of 30 hops:

      1     1 ms    <1 ms    <1 ms  10.1.1.100
      2    <1 ms    <1 ms    <1 ms  198.206.243.15

    Trace complete.


Wait, how does ``www.simpson.edu`` relate to ``10.1.23.175``? We'll talk about
that when we talk about the Domain Name System (DNS). For now, just think of it
as a human-friendly alias to the IP address.

Below we have a more complex route to Google. I can see it takes me
nine hops to get to Google. With a round-trip time of 19 ms. The computer
tries three times, which is why we have three columns of numbers.

::

    c:\>tracert www.google.com

    Tracing route to www.google.com [172.217.4.100]
    over a maximum of 30 hops:

      1    <1 ms    <1 ms    <1 ms  10.1.1.100
      2     1 ms     1 ms     1 ms  207.32.33.126
      3     2 ms     4 ms     2 ms  199.120.66.233
      4     1 ms     1 ms     9 ms  ins-border10-ds1-60-33.desm.netins.net [167.142.60.33]
      5     2 ms     2 ms     1 ms  ins-dc1-po200.desm.netins.net [167.142.67.193]
      6    18 ms    19 ms    19 ms  206.126.235.14
      7    19 ms    23 ms    18 ms  108.170.244.1
      8    19 ms    18 ms    18 ms  108.170.233.109
      9    19 ms    18 ms    19 ms  ord36s04-in-f100.1e100.net [172.217.4.100]

Netstat
^^^^^^^

Now we want to get an idea of how we figure out what program gets the
data once it arrives at the computer. On my work computer
I have programs like Google Drive, the file browser (that can look at network
drives), Microsoft Outlook, Moba XTerm, SourceTree, and Steam.

If a packet of data arrives, how do we know what program it goes to? We use
**ports**. Every (most) network connection has a port. My web server will listen
on port 80. My web browser will open a connection on port 15000. Therefore
if I send data to 172.217.4.100:80 then it will go to the computer at 172.217.4.100,
and to the program listening on port 80. Responses to my web request will go to
my computer at 10.1.23.175, and then my web browser which listens to port 15000.

On either UNIX or Windows you can use a program called ``netstat`` to see what
network connections you have open. You can see command-line options for netstat by typing
``netstat -?``. I particularly like ``netstat -b`` which shows me what application
is communicating on what port.

Note: To run ``netstat -b`` you need run the command as an administrator. When
opening the command prompt, right-click on the command prompt and select
"Run as Administrator".

Below is a shortened list of what my computer showed:

::

    C:\>netstat -b

    Active Connections

      Proto  Local Address          Foreign Address        State
      TCP    10.1.23.175:15319      ord30s25-in-f10:https  CLOSE_WAIT
     [googledrivesync.exe]
      TCP    10.1.23.175:43450      ord30s25-in-f205:https  CLOSE_WAIT
     [googledrivesync.exe]
      TCP    10.1.23.175:46136      fileserve:microsoft-ds  ESTABLISHED
     Can not obtain ownership information
      TCP    10.1.23.175:46170      162.254.193.47:27021   ESTABLISHED
     [Steam.exe]
      TCP    10.1.23.175:46174      jd-in-f125:5222        ESTABLISHED
     [Explorer.EXE]
      TCP    10.1.23.175:46658      msnbot-65-52-108-208:https  ESTABLISHED
      ShellHWDetection
     [svchost.exe]
      TCP    10.1.23.175:48688      207.32.33.199:59234    ESTABLISHED
     [OUTLOOK.EXE]
      TCP    10.1.23.175:48696      207.32.33.199:59234    ESTABLISHED
     [CompanionApp.exe]
      TCP    10.1.23.175:62396      ord36s04-in-f10:https  CLOSE_WAIT
     [motty.exe]
      TCP    10.1.23.175:65125      cs:ssh                 ESTABLISHED
     [MobaXterm.exe]
      TCP    10.1.23.175:65127      bitbucket:ssh          TIME_WAIT
      TCP    127.0.0.1:4172         cvr1834b:65001         ESTABLISHED
     [NvStreamNetworkService.exe]
      TCP    127.0.0.1:6000         cvr1834b:65121         ESTABLISHED
     [XWin_MobaX.exe]
      TCP    127.0.0.1:6000         cvr1834b:65122         ESTABLISHED


Now that we've seen an overview of Layer 3, let's dive down into some details.

Vocabulary
----------

* **Frame:** A chunk of data at Layer 2. An Ethernet frame can have up to 1500
  bytes of payload.
* **Datagram:** A datagram is a chunk of data on a packet-switched network.
  Unlike a packet, the sender is not notified if the receiver fails to receive
  the packet.
* **Packets:**  A chunk of data at Layer 3. We add extra information on a Frame
  to make it a packet. But it isn't a 1-to-1 mapping. A TCP/IPv4 packet can be
  up to 64k large, so multiple frames may be needed to move one packet.
  If a packet fails to be received, the sender gets a message letting it know.
* **Socket:** A socket is an end-point for a network communication. Think of it
  as a 'virtual plug.' Our programs create sockets for both the sender and
  receiver, then we virtually create string a 'cable', then we send data.
* **Checksums:** To detect if we received the bits correctly, or if there is
  an error, we use checksums. There are multiple ways to calculate checksums.
  For the IP, `click here to learn <https://en.wikipedia.org/wiki/IPv4_header_checksum>`_
  how they are calculated.
* **RFC:** `Request For Comments`_ is a publication used to set technical standards
  for the Internet. You can see a
  `list of standards <https://en.wikipedia.org/wiki/List_of_RFCs>`_. I
  particularly like the avian carrier standard.

* **Bus:** Multiple computers hook up to one long wire and share it. This used
  to be common because it was easy to wire. It wasn't reliable or fast however.
* **Hub:** Multiple computers will hook up to a central spot (hub). When one computer
  wants to say something, the hub will repeat it to all computers.
* **Switch:** Multiple computers will hook up to a central spot (hub). When one
  computer wants to talk to another computer, the switch will pass the message to
  only the computer it was intended to.
* **Router:** Knows how to intelligently pass a message across multiple computers.


TCP/IP
------

TCP/IP stands for `Transmission Control Protocol/Internet Protocol`_. The TCP/IP
abbreviation is a bit sad, because there is actually a third protocol that is part
of TCP/IP that gets left out. This is the User Datagram Protocol.

TCP/IP is a networking protocol used by the Internet. It does some of what is
needed by Layer 3. It also extends a bit into Layers 2 and 4. It doesn't do
everything that Layer 3 needs.

The OSI model is a conceptual model. Not a technical one. Therefore
note that TCP/IP is not the same thing as Layer 3. It does, however, work
out best to cover TCP/IP while we cover Layer 3 of the OSI model.

TCP/IP is sometimes referred to as the "TCP/IP stack" because it covers
several layers.

TCP/IP became a standard for military networks in 1982.
IBM, AT&T, and DEC became the first people to adopt TCP/IP. Note that they
already had their own networking standards, and this was a politically difficult
change.

UNIX and OS/2 systems started being released with TCP/IP stacks. In 1989 AT&T
released their TCP/IP code into the public domain. They gave it away, which
was important for creating a standard. This must have been a difficult
business decision.

You could BUY TCP/IP stacks from vendors for Windows 95. Eventually Microsoft
released their own TCP/IP stack that you didn't have to buy. With native
Windows support, this solidified industry standardization around TCP/IP.

Unfortunately, there aren't enough TCP/IP addresses to support all of the network
devices out there. The four-bytes addresses we are used to seeing come from
TCP/IPv4. There is a TCP/IPv6 that has longer addresses. Network administrators
also use Network Address Translation (NAT) to reduce the need for addresses.

IP
^^

The `Internet Protocol`_ forms the base communications protocol that both
UDP and TCP are built on. It is *almost* the same as UDP.

IP is connectionless:
    * You don't have to log in.
    * If you want to send data longer than the maximum size of the packet, there's
      no mechanism to split up the data.
    * If the data doesn't arrive, there's no mechanism to request the data be sent
      again.
    * IP **does not** have any way to route data between software programs on the
      computer. Because of this, rarely does one use IP.


UDP
^^^

The `User Datagram Protocol`_ sends a packet of data across the network. It is
built on top of IP, and adds support for *ports*.

IP is connectionless:
    * You don't have to log in.
    * If you want to send data longer than the maximum size of the packet, there's
      no mechanism to split up the data.
    * If the data doesn't arrive, there's no mechanism to request the data be sent
      again.
    * IP **does** have a way to route data between software programs on the
      computer. We call these *ports*.

Point three is important. Because I know a joke about it, and I love jokes:
    "I'd tell you a UDP joke, but you might not get it."

Below is an image that shows how a UDP packet is arranged. Note on the left
side is shows what part is the Ethernet frame, what part is the IP, and what
part UDP adds.

.. figure:: udp_packet.gif
    :width: 550px
    :alt: alternate text

    Image from (`Twiddle, 1997 <http://www.doc.ic.ac.uk/~kpt/Slides/Internet/sld052.htm>`_).
    Technically it is a datagram and not a packet.

A UDP datagram can be 65,535 bytes long. With an 8 bit UDP header and a 20 byte
IP header, that leaves 65,507 bytes for data.

Since a UDP datagram can be larger than an Ethernet frame it can be *fragmented*.
See the additional fields that support this. Ideally, we don't want to fragment
our packets.

How do you send and receive datagrams? Easy. See :ref:`datagram_tutorial`. Also,
at the end of that tutorial there are many images that pull apart the datagram
byte by byte. Look at that and see how it maps to the UDP image.

Ports
^^^^^

Ports allow us to route between applications on the same computer. A program on
a server will "listen" for incoming data on certain ports. You can work with any
port from 0 to 65,535. Some computers require root or admin privileges for a program
to listen on ports 0-1023.

By convention, certain ports represent certain services. See
Wikipedia's `list of TCP and UDP port numbers`_.

The client to the server normally connects using a `ephemeral port`_. These
are numbered 49152–65535. Therefore a web browser may connect to google.com
on port 80. The IP address and port may be: 216.58.192.206:80. Google will
connect back to the client computer on an ephemeral port. So return packets would
go to the client address which might look like 192.168.1.101:51010.


TCP
^^^

Most connections on the Internet happen with the
`Transmission Control Protocol`_ (TCP) protocol. TCP is built on top of
IP and offers:

* Notification of delivery failure
* Retransmission
* Breaking a large message into parts
* Reassembly in the proper order
* Network congestion

A lot of these are Layer 4 items on the OSI model. So we will table our discussion
of TCP until a later date.

Special IP Addresses
^^^^^^^^^^^^^^^^^^^^

`Reserved IP Addresses`_

Local loop back link:
  * 127.0.0.1

Private subnets (often used with NAT, explained below):
  * 10.0.0.0 - 10.255.255.255
  * 172.16.0.0 - 172.31.255.255
  * 192.168.0.0 - 192.168.255.255

Local link:
  * 169.254.0.0 - 169.254.255.255

* Items ending in .0 are broadcast. Exactly what the broadcast address is
  depends on the `netmask`_. It might be something other than .0.
* Items ending in .1 would be the gateway. This isn't a requirement but most
  people follow this convention.
* Items ending in .10 would be switches. A few people follow this convention.
* Ending in .100 would be end-user nodes. A few people follow this convention.

Blocks of IP addresses (aside from the private subnets) are owned.
Who owns a block of IP addresses? You can look it up with several tools, such
as this one:

https://mxtoolbox.com/arin.aspx

We have run out of IPv4 addresses. Therefore we must manage IPv4 addresses
carefully, or use IPv6.

IPv4 and IPv6
^^^^^^^^^^^^^

`Internet Protocol version 6`_ uses a much larger address than IPv4.

In 2014 about 99% of the traffic was IPv4.
In July 2016 Google reported that 13% of the traffic hitting its services was IPv6.

Subnets and Netmasks
^^^^^^^^^^^^^^^^^^^^

Networks are divided into `subnets`_. We divide the network into a subnet
of "local" computers. If we want to talk with any of the "local" computers
we don't need to travel multiple hops. We just talk, and using a switch
or a hub they will be able to hear us. If we need to talk outside out local
network, we need to pass it over to a router.

How do figure out what computers are local or not? It depends on the IP address
and a `netmask`_. For example, we might have all 254 computers on the local
subnet numbered::

  192.168.1.1 to 192.168.1.255

Or do we need a bigger subnet? We could have over 65,000 computers on:

  192.168.1.1 to 192.168.255.255

We determine what part of the IP address is "local" and what part is routing
with the `netmask`_ which comes from `RFC 1878`_.

The Subnet mask covers the routing portion of the address with 1's.

From Wikipedia's entry on subnetworks:

=============== ======================================= ====================
What            Binary form                             Dot-decimal notation
=============== ======================================= ====================
IP address      ``11000000.10101000.00000101.10000010``        192.168.5.130
Subnet mask     ``11111111.11111111.11111111.00000000``        255.255.255.0
Network prefix  ``11000000.10101000.00000101.00000000``          192.168.5.0
Host part       ``00000000.00000000.00000000.10000010``            0.0.0.130
=============== ======================================= ====================

We often show a subnet's routing properties using `CIDR form`_. The subnet above
would be shown with 192.168.5.0/24.

See also this handy `netmask reference`_.

Broadcast
^^^^^^^^^

Sending a message to the broadcast address will send the message to every
computer in the subnet. Useful if you want to announce something to every
computer. To find the broadcast address, use your IP address and bit-wise
and it with the netmask. This would be the 'network prefix' sown in the example
table above.

Gateway
^^^^^^^

This is your router. If a message isn't intended for your network, we will
pass it to the router. A router's IP address should normally be one more than
the broadcast IP address. So if your broadcast address is 192.168.1.0 the router
should be 192.168.1.1.

By using a netmask, the router can quickly figure out if the message should be
picked up for routing, or left to the local network.

Protocols
---------

ICMP
^^^^

`Internet Control Message Protocol`_ (ICMP) is defined by `RFC 792`_. Also, there
is a `ICMPv6`_ version of the protocol.



NAT
^^^

DNS
^^^

Tricks, talk about `Google public DNS`_ at 8.8.8.8 and 8.8.4.4.

DHCP
^^^^

WINS
^^^^

FTP
^^^

NTP
^^^

LDAP
^^^^

SMTP
^^^^

IMAP
^^^^

How does Routing Work
---------------------

* DVMRP
* BGP
* RIP

Internet Providers
------------------

* `Tier 1 Network Provider`_

.. _Handshaking: https://en.wikipedia.org/wiki/Handshaking
.. _User Datagram Protocol: https://en.wikipedia.org/wiki/User_Datagram_Protocol
.. _Internet Protocol: https://en.wikipedia.org/wiki/Internet_Protocol
.. _Tier 1 Network Provider: https://en.wikipedia.org/wiki/Tier_1_network
.. _Request For Comments: https://en.wikipedia.org/wiki/Request_for_Comments
.. _Transmission Control Protocol/Internet Protocol: https://en.wikipedia.org/wiki/Internet_protocol_suite
.. _list of TCP and UDP port numbers: https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
.. _Reserved IP Addresses: https://en.wikipedia.org/wiki/Reserved_IP_addresses
.. _ephemeral port: https://en.wikipedia.org/wiki/Ephemeral_port
.. _Transmission Control Protocol: https://en.wikipedia.org/wiki/Transmission_Control_Protocol
.. _subnets: htt``ps://en.wikipedia.org/wiki/Subnetwork
.. _RFC 1878: http://www.ietf.org/rfc/rfc1878.txt
.. _netmask: http://www.computerhope.com/jargon/n/netmask.htm
.. _netmask reference: http://www.unixwiz.net/techtips/netmask-ref.html
.. _CIDR form: https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation
.. _Internet Protocol version 6: https://en.wikipedia.org/wiki/IPv6
.. _Internet Control Message Protocol: https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol
.. _RFC 792: https://tools.ietf.org/html/rfc792
.. _Google public DNS: https://developers.google.com/speed/public-dns/docs/using
.. _ICMPv6: https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol_version_6

