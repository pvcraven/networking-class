Lab 3: Networking Layer
-----------------------

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
Step 7    A     97
========  ===== ======

Show me each step in person, or e-mail me a document.

Part 1 - Hostname
^^^^^^^^^^^^^^^^^

Set the host name on your Raspberry Pi. Document how this is done.

Explain how to set the hostname on a Windows computer.

Part 2 - ARP
^^^^^^^^^^^^

Every time you start up your Raspberry Pi, it could have a new IP address.
Demonstrate how to use the ``arp`` command from your PC to discover the IP
address of your Raspberry Pi without hooking it up to a monitor.

You may want to borrow my label maker to put the physical address of your
Pi on the outside.

Part 3 - NSLookup
^^^^^^^^^^^^^^^^^

* Figure out how to use ``nslookup``
* Explain how to buy your own domain. Or just show me a domain you've bought.
* Tell me the
  `steps <http://blog.catchpoint.com/2014/07/01/dns-lookup-domain-name-ip-address/>`_
  that the client lookup in the
  `DNS <https://en.wikipedia.org/wiki/Domain_Name_System>`_ system goes through.
* Tell me how to find out who owns a domain

Part 4 - Ping
^^^^^^^^^^^^^

* Figure out how to use the ``ping`` command.
* Pick a server to ping. Not a local one, some server further away.
* Figure out how to `redirect output from a command to a file <https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/redirection.mspx?mfr=true>`_.
* Run ping a really long time and capture the output. At least an hour. Maybe a day.
* Create a graph of the ping times

Note that not all servers will respond to a ping request. Also, if there is
traffic congestion, ping packets will be one of the first to get dropped.

Part 5 - NMap
^^^^^^^^^^^^^

Figure out how to use the network mapping tool `nmap`_. NMap is great at scanning
computers and seeing what ports and services they have open.

You can install nmap on your Raspberry Pis by::

  sudo apt-get update
  sudo apt-get install nmap

Or you can download and install nmap on your laptop. It
`works on the Mac <https://nmap.org/book/inst-macosx.html>`_ too.

Google, or just type ``nmap`` to see all the command line options. Spend time
to understand how they work.
there are some `nice tutorials <http://www.cyberciti.biz/networking/nmap-command-examples-tutorials/>`_ out there.

Optionally, learn the GUI version too.

Use nmap to scan computers that you have permission to use nmap on.

Note that running an NMap scan might
be against the rules of the network you are on. Don't do this at your workplace
because you might get fired.

You *can* scan:

* 127.0.0.1 (Only works on non-windows computers)
* cs.simpson.edu
* programarcadegames.com
* 10.1.21.198
* Any of your Raspberry Pis
* Any of your friend's Raspberry Pis
* The entire network of 192.168.1.* on our wireless router

Or perhaps try some public computers.

To turn this part in, write up what you found using the tool.

Part 6 - Traceroute
^^^^^^^^^^^^^^^^^^^

Use the traceroute on many sources and destinations. At least 10. Then make a graph
showing the nodes and the routes. For interesting graphs:

* Start at different locations (coffee shop vs. lab) and go to the same
  location.
* Find different places that have as many nodes in common as possible.
* Run a traceroute one day, and then run another a different day.

If you can, find sites that have common pathways.

You may need a large piece of paper.


Part 7 - Routing
^^^^^^^^^^^^^^^^

You can do this part solo, or paired up.

Before you begin, reset both the switch and the router. (Note, I don't have
instructions on how to do this yet, so you'll need to wait until I do.)

Then, to complete, go through the :ref:`routing-tutorial`.

Have the instructor see that you:
    * Can log into one of the switches
    * You have logged into the router
    * That you can route between both switches

.. _nmap: https://nmap.org/
