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

Part 1 - Hostname and Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do the following:

* Set the host name (computer name) on a Linux computer like your
  Raspberry Pi. Don't use ``raspi-config``, because that is specific to the
  Pi, we want a method that will work for all Linux computers.
  Document how this is done.
* Explain how to set the hostname on a Windows computer.
* Explain how the ``/etc/resolv.conf`` and ``/etc/hosts`` files on Linux work.
* Explain the
  `Host Name Resolution Order <https://support.microsoft.com/en-us/kb/172218>`_
  in Windows.
* Explain how to manually set a computer's IP address on either Mac, Linux, or Windows.
* Explain how to manually set a computer's DNS servers.

Part 2 - ARP
^^^^^^^^^^^^

Every time you start up your Raspberry Pi, it could have a new IP address.
Demonstrate how to use the ``arp`` command from your PC to discover the IP
address of your Raspberry Pi without hooking it up to a monitor.

If you don't get many addresses when you run ``arp``, skip down and learn to
run ``nmap`` on an entire subnet. Then run ``arp`` afterwards. Your address
resolution table will be filled out once you force the computer to connect to
other local computers.

You may want to borrow my label maker to put the physical address of your
Pi on the outside.

You may wonder why I didn't teach you this earlier.

Part 3 - NSLookup
^^^^^^^^^^^^^^^^^

* Figure out how to use the ``nslookup`` command:

  * Get an IP address from a domain.
  * Get a domain from an IP address (reverse lookup)
  * Explain what a non-authoritative answer means

* Explain how to buy your own domain. Or just show me a domain you've bought.
* Tell me the
  `steps <https://www.verisign.com/en_US/website-presence/online/how-dns-works/index.xhtml>`_
  that the client lookup in the
  `DNS <https://en.wikipedia.org/wiki/Domain_Name_System>`_ system goes through.
* Demonstrate how to find out who owns a domain. Use ICANN, not some other
  service, as ICANN provides the most information.

Part 4 - Ping
^^^^^^^^^^^^^

* Figure out how to use the ``ping`` command.
* Pick a server to ping. Not a local one, but a server further away.
* Figure out how to `redirect output from a command to a file <https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/redirection.mspx?mfr=true>`_.
* Run ping a really long time and capture the output. At least an hour. Maybe a day.
* Create a graph of the ping times. If you use the ``grep`` tool and regular expressions
  you can filter out the "extra" and just leave the timings. However it is probably
  easier just to use search and replace in Excel. I **don't** want a histogram.
  Just graph the ping times for each ping.

Note that not all servers will respond to a ping request. Also, if there is
traffic congestion, ping packets will be one of the first to get dropped.

**Totally random suggestion to get side-tracked with:**

If you are on Linux or Mac, you can use ``grep`` to filter your ping
commands so that only the timing is left over. `Grep`_ is a tool used to quickly
filter text based on regular expressions.

I don't want to show you *exactly* how to do that, so I'll give
you a different example. The ``ifconfig`` outputs a lot of text::

  craven@cs ~ $ ifconfig
  eth0      Link encap:Ethernet  HWaddr 52:54:00:ae:c5:0e
            inet addr:206.72.8.162  Bcast:206.72.8.255  Mask:255.255.255.0
            inet6 addr: fe80::5054:ff:feae:c50e/64 Scope:Link
            UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
            RX packets:1197657294 errors:0 dropped:361116 overruns:0 frame:0
            TX packets:19216543 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1000
            RX bytes:138105341533 (138.1 GB)  TX bytes:5148797084 (5.1 GB)

  lo        Link encap:Local Loopback
            inet addr:127.0.0.1  Mask:255.0.0.0
            inet6 addr: ::1/128 Scope:Host
            UP LOOPBACK RUNNING  MTU:65536  Metric:1
            RX packets:685399 errors:0 dropped:0 overruns:0 frame:0
            TX packets:685399 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:0
            RX bytes:160200407 (160.2 MB)  TX bytes:160200407 (160.2 MB)

I could use a pipe character ``|`` and "pipe" the output of ``ifconfig`` into the
grep command::

  craven@cs ~ $ ifconfig | grep 'inet addr'
            inet addr:206.72.8.162  Bcast:206.72.8.255  Mask:255.255.255.0
            inet addr:127.0.0.1  Mask:255.0.0.0

I could even fancy that up using the ``-o`` option that only displays matching
text. Along with my advanced knowledge of `regular expressions`_::

  craven@cs ~ $ ifconfig | grep -o 'inet addr:[0-9\.]*'
  inet addr:206.72.8.162
  inet addr:127.0.0.1

And I could "chain" grep filters::

  craven@cs ~ $ ifconfig | grep -o 'inet addr:[0-9\.]*' | grep -o '[0-9\.]*'
  206.72.8.162
  127.0.0.1

Or you could just use search/replace to remove the extra text in Excel. That works too.

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
* The entire network of 192.168.1.* on our wireless router. (Look up how to
  scan a subnet. You'll use a command like ``nmap -v -sP 192.168.1.0/24``. The
  output of that command is kind of messy, so some on-line tutorials might have
  you pipe the output through ``grep`` which can filter based on regular expressions.)

Or perhaps try some public computers.

A common, and interesting trick, is for a network administrator to run nmap
on a local subnet. Then redirect all the output to a file. Each day, run nmap again.
Do a ``diff`` on the new and old files. If there is a difference, it means
a network service on your subnet has changed. You can e-mail that difference
to you automatically.
That way you can know if someone started a web server or some other server on
your network. The code to do this takes less space than the English to explain it.

To turn this part in, write up what you found using the tool. Include:

* Output of two nmap scans on individual machines. Do a quick one or
  two sentence explanation of what each scan shows.
* One more scan of a machine that uses some different command line options.
  Look at what is available for command line options, and try a few out. I just
  want to see that you are able to do something past the default scan.
  Quickly explain the result.
* Scan our entire class wireless subnet (not Simpson's, but the one we set
  up for class).

Part 6 - Traceroute
^^^^^^^^^^^^^^^^^^^

Use the `traceroute <https://en.wikipedia.org/wiki/Traceroute>`_
on many sources and destinations. At least 10. Then make a graph
showing the nodes and the routes.

Remember that ``traceroute`` on Windows is ``tracert``.

For interesting graphs:
    * Start at different locations (coffee shop vs. lab) and go to the same
      location.
    * Find different places that have as many nodes in common as possible.
    * Run a traceroute one day, and then run another a different day.

If you can, find sites that have common pathways.

You may need a large piece of paper. Or get happy with Visio. Or learn
`GraphViz <http://www.graphviz.org/>`_ and
`dot <https://en.wikipedia.org/wiki/DOT_(graph_description_language)>`_ if you
really want to get crazy.

Someone has done a lot of this, you can see their `Internet Map`_ results.

Part 7 - Routing
^^^^^^^^^^^^^^^^

You can do this part solo, or paired up.

Make sure you 'reset' the router as part of the :ref:`routing-tutorial`.

Have the instructor see that you:
    * Can log into one of the switches
    * You have logged into the router
    * That you can route between both switches

You can get
`lots of certifications <http://www.cisco.com/c/en/us/training-events/training-certifications/certifications.html>`_
in how to configure Cisco routers. They can be a ticket to a nice job.


.. _nmap: https://nmap.org/
.. _Internet Map: http://internet-map.net/
.. _regular expressions: https://regexone.com/
.. _grep: https://en.wikipedia.org/wiki/Grep
