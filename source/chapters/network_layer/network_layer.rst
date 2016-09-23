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

Now we want to get an idea of how we route between applications. On my work computer
I have programs like Google Drive, a file browser that can look at network
drives, Microsoft Outlook, Moba XTerm, SourceTree, and Steam.

If a packet of data arrives, how do we know what program it goes to? We use
**ports**. Every (most) network connection has a port. My web server will listen
on port 80. My web browser will open a connection on port 15000. Therefore
if I send data to 172.217.4.100:80 then it will go to the computer at 172.217.4.100,
and to the program listening on port 80. Responses to my web request will go to
my computer at 10.1.23.175, and then my web browser which listens to port 15000.

On either UNIX or Windows you can use a program called ``netstat`` to see what
network connections you have open. You can see more options for netstat by typing
``netstat /?``. I particularly like ``netstat -b`` which shows me what application
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

* Packets
* Frames
* Sockets
* Datagram
* Handshaking
* Checksums
* RFC

TCP/IP
------

TCP/IP stands for Transmission Control Protocol/Internet Protocol. The TCP/IP
abbreviation is a bit sad, because there is actually a third protocol that is part
of TCP/IP that gets left out. This is the User Datagram Protocol.

TCP/IP is a networking protocol used by the Internet. It does some of what is
needed by Layer 3. It also extends a bit into Layers 2 and 4. It doesn't do
everything that Layer 3 needs.

The OSI model is a conceptual model. Not a technical one. Therefore
note that TCP/IP is not the same thing as Layer 3. It does, however, work
out best to cover TCP/IP while we cover Layer 3 of the OSI model.

(Talk about history and TCP/IP stack
)
UDP
^^^

The `User Datagram Protocol`_ sends a packet of data across the network.

It is connectionless:
    * You don't have to log in.
    * If you want to send data longer than the maximum size of the packet, there's
      no mechanism to split up the data.
    * If the data doesn't arrive, there's no mechanism to request the data be sent
      again.

Point three is important. There's a joke related to it:
    "I'd tell you a UDP joke, but you might not get it."

* What does a UDP packet look like?

A UDP packet can be 65,535 bytes long. With an 8 bit UDP header and a 20 byte
IP header, that leaves 65,507 bytes for data.

How do you send and receive datagrams? Easy. See :ref:`datagram_tutorial`.

* How much data can a UDP packet send?
* What is a checksum?



TCP
^^^

IP
^^

Ports
^^^^^

Gateway
^^^^^^^

Broadcast
^^^^^^^^^

Netmask
^^^^^^^

IPv4 and IPv6
^^^^^^^^^^^^^

Routing
-------

* DVMRP
* BGP
* RIP

Protocols
---------

NAT
^^^

DNS
^^^

Tricks, talk about 8.8.8.8

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



.. _User Datagram Protocol: https://en.wikipedia.org/wiki/User_Datagram_Protocol
