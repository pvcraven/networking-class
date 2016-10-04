.. _routing-tutorial:

Routing Tutorial
================

Goal
----

The goal of this lab is to get you to "peek" inside the world of configurable
network switches and routers. We won't actually *do* much aside from
opening the door and peeking inside. But my hope is that if
you realize what you *can* do, you will:

* Learn more about it yourself.
* Have a better idea of what network engineers do, when you work with them.

I don't want network setup to be some puffy cloud that you think only wizards try.

If you want to get into networking as a career, it isn't hard.
You can buy old switches and routers off EBay for cheap.
The switches we will use here I bought for $20 or so.
There are a lot of documentation, manuals, and certification study guides
available on-line and in bookstores.

Cisco_ is a company is responsible for most of the routers on the Internet.
Hewlett-Packard also has many devices available.

Two-year schools are good places to learn the specific technical skills around
working with these devices if you are interested.
If
you search up "DMACC" and "Cisco" you can find some of the courses DMACC offers
to become certified working with Cisco Routers.

Switch Setup
^^^^^^^^^^^^

The simplest switches are plug-and-play. You can buy them
at Wal-Mart. Sometimes switches are combined with routers
as an all-in-one device.

More complex switches can be configured. You can take a
24 port switch and configure it into four six-port switches
for example.

We are going to use a more complex switch than a Wal-Mart
one. This tutorial covers a very basic setup of this switch.


Install Telnet
--------------

We have already used Secure Shell (`SSH`_) to connect to another computer.
SSH is encrypted and a great way to communicate with computers remotely.

Before there was SSH, there was Telnet_. Telnet is like SSH, except it
isn't encrypted. If you log in with your user name and password, someone
with Wireshark that was on the network could see each of the letters
typed. Grabbing the password is easy.

You should never use Telnet.

That said, our switches don't support SSH, so we'll need to use Telnet.

Our Raspberry Pi does not include a Telnet program as part of its
default software. Because no one in their right mind would use it.
Since we aren't in our right mind, let's install telnet.

::

  # Get the update lists of software
  sudo apt-get update
  # Find telnet and install it
  sudo apt-get install telnet

Connect with a Serial Connection
--------------------------------

Great! We can connect with a telnet, right? No. Our switch doesn't
even have an IP address to telnet to.

We need to connect via a serial cable. Before there was telnet,
there was a serial connector. Most computers came with a type
of connector called `RS-232`_. We'd use this connector to connect our
modems.

A lot of networking equipment uses RS-232 as a way to first get
connected. Unfortunately computers don't come with RS-232 connectors
anymore. You can get an adapter that plugs into your USB connector that
will drive an RS-232 port. We'll need that. We will also likely need to
download a driver for it.

Download driver:

* USA-19HS: https://www.tripplite.com/support/model/mid/USA-19HS
* Other connector: TODO

MobaXTerm can connect to a serial line. Serial ports will be named
something like COM0, COM1, COM2, etc.

Find the Manual
---------------

We are using a Hewlett Packard HPJ9085a switch. We will probably need
a manual to learn how to use it. You might think that you can get the manual
on line by searching for "hpj9085a manual."

Or not. Unfortunately it is very difficult to find because of spam and bad
links. Go to HP and find the manual via a serial number lookup.

I searched on "hp manual lookup" and found `this page<http://h20180.www2.hp.com/apps/Lookup?h_pagetype=s-003&h_lang=en&h_client=z-a-r1002-3&h_page=index&h_cc=us&jumpid=hpr_R1002_USEN>`_.
Then I typed in "hpj9085a". That didn't work. Then I entered the serial number
and that *did* work.

I found in the manual on page 4-12 shows you how to reset switch so we can start fresh.
Give that a try.

Plug in the serial line. On startup, you will see::

	ROM information:
	   Build directory: /sw/rom/build/nemorom(ndx)
	   Build date:      Nov 28 2007
	   Build time:      16:36:54
	   Build version:   R.10.06
	   Build number:    14201

	OS identifier found at @ 0xbc020000
	Verifying Image validity ...
	CRC on OS image header Passed
	CRC on complete OS image file Passed
	Valid OS image @ 0xbc020000

	Decompressing...done.
	CRC of image is 0x2e3a30b1
	CRC @ 0x80001000 Len 10873888 is 0x2e3a30b1

	ROM information:
	   Build directory: /sw/rom/build/nemorom(ndx)
	   Build date:      Nov 28 2007
	   Build time:      16:36:54
	   Build version:   R.10.06
	   Build number:    14201

	OS identifier found at @ 0xbc020000
	Verifying Image validity ...
	CRC on OS image header Passed
	CRC on complete OS image file Passed
	Valid OS image @ 0xbc020000

	HP ProCurve Switch 2610-24 (J9085A)
	ROM Build Directory: /sw/rom/build/nemorom(ndx)
	        ROM Version: R.10.06
	     ROM Build Date: 16:36:54 Nov 28 2007
	   ROM Build Number: 14201

	Copyright (c) 1995-2001 Hewlett-Packard Company. All rights reserved.

	                         RESTRICTED RIGHTS LEGEND

	Use, duplication, or disclosure by the Government is subject to restrictions
	as set forth in subdivision (b) (3) (ii) of the Rights in Technical Data and
	Computer Software clause at 52.227-7013.

	    Hewlett-Packard Company, 3000 Hanover Street, Palo Alto, CA 94303

	Enter h or ? for help.

	=>
	ROM information:
	   Build directory: /sw/rom/build/nemorom(ndx)
	   Build date:      Nov 28 2007
	   Build time:      16:36:54
	   Build version:   R.10.06
	   Build number:    14201

	OS identifier found at @ 0xbc020000
	Verifying Image validity ...
	CRC on OS image header Passed
	CRC on complete OS image file Passed
	Valid OS image @ 0xbc020000

	Decompressing...done.
	CRC of image is 0x2e3a30b1
	CRC @ 0x80001000 Len 10873888 is 0x2e3a30b1



	initializing..initialization done.



	Waiting for Speed Sense.  Press <Enter> twice to continue.


Hit enter a few times. After a few more data screens, you get a
prompt that looks like:

.. code::

  ProCurve Switch 2610-24#

Type ``help`` to see a list of commands.

We want to use the ``setup`` command to set it up.
  * It will ask for a name. Call it 'CMSC 340 Switch 1' or similar.
  * Leave contact info, password blank.
  * We won't use a gateway yet. (TODO: Explain what we'd do for a gateway)
  * Spanning Tree - No if we know things will be hooked up right. Yes
    if we might have loops. (TODO: Possible exercise: Turn if off, hook
    up a loop to see what happens. Turn it on and see what happens.)
  * Skip time server setup. (TODO: Talk about time servers.)
  * IP. We will manually set. Hit spacebar twice Use 192.168.1.10
    (0 is broadcast, 1 is router. (TODO: Explain broadcast, and number
    conventions)
  * Netmask: 255.255.255.0 (TODO: Explain netmask and /24 type notation)

Connect to Switch with Telnet
-----------------------------

At this point, can use telnet.
	* Plug in Raspberry Pi to switch
	* Do ifconfig, won't have IP address. No magic yet.
	* Set ip: ``sudo ifconfig eth0 192.168.1.100 netmask 255.255.255.0``
	* Set gateway: ``sudo route add default gw 192.168.1.1`` (TODO: What is a
	  gateway)
	* Type ``telnet 192.168.1.10``
	* Yay! We are there

There is also a browser interface.
  * Open browser and go to 192.168.1.10
  * Oooh, requires a java plugin. Whatever. We'll use the command line


Router
------

Resetting the router
^^^^^^^^^^^^^^^^^^^^

From `NetworkWorld <http://www.networkworld.com/article/2343961/cisco-subnet/cisco-subnet-how-to-reset-a-cisco-router-to-factory-default-removing-the-startup-configuration-file.html>`_:

Type `` erase nvram`` followed by ``reload``.

Router Tutorial
^^^^^^^^^^^^^^^

* Connect
* Power up
* Hit enter
* Go into 'initial configuration dialog'

::

	Would you like to enter the initial configuration dialog? [yes/no]: yes

	At any point you may enter a question mark '?' for help.
	Use ctrl-c to abort configuration dialog at any prompt.
	Default settings are in square brackets '[]'.

	Basic management setup configures only enough connectivity
	for management of the system, extended setup will ask you
	to configure each interface on the system

	Would you like to enter basic management setup? [yes/no]: yes
	Configuring global parameters:

	  Enter host name [Router]: cmsc340router

	  The enable secret is a password used to protect access to
	  privileged EXEC and configuration modes. This password, after
	  entered, becomes encrypted in the configuration.
	  Enter enable secret: cmsc340secret

	  The enable password is used when you do not specify an
	  enable secret password, with some older software versions, and
	  some boot images.
	  Enter enable password: cmsc340password

	  The virtual terminal password is used to protect
	  access to the router over a network interface.
	  Enter virtual terminal password: cmsc340vt
	  Configure SNMP Network Management? [yes]: no

	Current interface summary


	Any interface listed with OK? value "NO" does not have a valid configuration

	Interface                  IP-Address      OK? Method Status                Protocol
	FastEthernet0/0            unassigned      NO  unset  up                    down
	FastEthernet0/1            unassigned      NO  unset  up                    down
	Serial0/0/0                unassigned      NO  unset  down                  down

	management network from the above interface summary: FastEthernet0/0

	Configuring interface FastEthernet0/0:
	  Use the 100 Base-TX (RJ-45) connector? [yes]:
	  Operate in full-duplex mode? [no]: yes
	  Configure IP on this interface? [yes]:
	    IP address for this interface: 192.168.1.1
	    Subnet mask for this interface [255.255.255.0] :
	    Class C network is 192.168.1.0, 24 subnet bits; mask is /24

	The following configuration command script was created:

	hostname cmsc340router
	enable secret 5 $1$7wzp$GmYsBze2WVxkuoaOvbAuP0
	enable password cmsc340password
	line vty 0 4
	password cmsc340vt
	no snmp-server
	!
	no ip routing

	!
	interface FastEthernet0/0
	no shutdown
	media-type 100BaseX
	full-duplex
	ip address 192.168.1.1 255.255.255.0
	no mop enabled
	!
	interface FastEthernet0/1
	shutdown
	no ip address
	!
	interface Serial0/0/0
	shutdown
	no ip address
	!
	end


	[0] Go to the IOS command prompt without saving this config.
	[1] Return back to the setup without saving this config.
	[2] Save this configuration to nvram and exit.

	Enter your selection [2]:

	Building configuration...
	Use the enabled mode 'configure' command to modify this configuration.


	Press RETURN to get started!


	*Sep 17 19:11:28.055: SERVICE_MODULE(Serial0/0/0): self test finished: Passed
	*Sep 17 19:11:45.007: %VPN_HW-6-INFO_LOC: Crypto engine: aim 0  State changed to: Initialized
	*Sep 17 19:11:45.011: %VPN_HW-6-INFO_LOC: Crypto engine: aim 0  State changed to: Enabled sslinit fn

	*Sep 17 19:11:48.371: %VPN_HW-6-INFO_LOC: Crypto engine: onboard 0  State changed to: Initialized
	*Sep 17 19:11:48.371: %VPN_HW-6-INFO_LOC: Crypto engine: onboard 0  State changed to: Disabled
	*Sep 17 19:11:49.071: %LINEPROTO-5-UPDOWN: Line protocol on Interface VoIP-Null0, changed state to up
	*Sep 17 19:11:49.071: %LINK-3-UPDOWN: Interface Serial0/0/0, changed state to down
	*Sep 17 19:11:50.071: %LINEPROTO-5-UPDOWN: Line protocol on Interface Serial0/0/0, changed state to down
	*Sep 17 19:11:50.607: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to down
	*Sep 17 19:11:50.607: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to down
	*Sep 17 19:20:38.795: %LINK-5-CHANGED: Interface Serial0/0/0, changed state to administratively down
	*Sep 17 19:20:39.007: %LINK-5-CHANGED: Interface FastEthernet0/1, changed state to administratively down
	*Sep 17 19:20:43.643: %SYS-5-RESTART: System restarted --
	Cisco IOS Software, 1841 Software (C1841-ADVIPSERVICESK9-M), Version 12.4(3d), RELEASE SOFTWARE (fc3)
	Technical Support: http://www.cisco.com/techsupport
	Copyright (c) 1986-2006 by Cisco Systems, Inc.
	Compiled Tue 18-Apr-06 19:10 by alnguyen
	*Sep 17 19:20:43.647: %SNMP-5-COLDSTART: SNMP agent on host cmsc340router is undergoing a cold start
	cmsc340router>






Enter a secret 'cmsc340secret' - Enables configuration
Enter a password 'cmsc340password' - Enables monitoring
Enter virtual terminal password - 'cmsc340vt' for hooking up via network

Now type:
``help``

Then type:

``?``

then type:

``show ?``

To be able to do make configuration changes,
let's get into a higher mode. Type::

  enable

Then use our password ``cmsc340enable``.

You should have a # for a prompt to show privilege elevation.

Now type ``show ?`` and see all the cool new commands that we have.

Type ``show version`` See ROM, uptime, etc.

Type ``show interface`` See interface details.

Wait! I see that the ``line protocol is down``. Let's fix that.

Plug into 0/0 plug into switch. You should see messages on the
See if it gives you messages.

Type ``show interface`` to see ``line protocol is up``

We want to set up the other interface.
Type ``configure`` and get::

	cmsc340router#configure
	Configuring from terminal, memory, or network [terminal]? t
	Enter configuration commands, one per line.  End with CNTL/Z.

Now we want to select our second card::

	cmsc340router(config)#interface FastEthernet0/1

See the commands available::

	cmsc340router(config-if)#?
	Interface configuration commands:
	[etc]

I did a Google search and found the syntax for the command
to set the IP address here:

http://www.cisco.com/c/en/us/td/docs/ios/12_2/ip/configuration/guide/fipr_c/1cfipadr.html#wp1000918

Most computers give you a "Syntax error" when you type something wrong.
Cisco routers assume you typed in a machine name, and tries to telnet
to it. Along with a really long pause while it tries.

Now to set the IP of that second card::

	cmsc340router(config-if)#ip address 192.168.2.1 255.255.255.0

Turn on routing. This is supposed to be on by default, but that didn't happen for me::

	cmsc340router(config-if)#ip routing

Make the card 'active'::

    cmsc340router(config-if)#no shut

Exit::

	cmsc340router(config-if)#exit
	cmsc340router(config)#exit
	cmsc340router#

Now type ``show interface`` and see our second card is configured.



Save Changes
------------
After you are done, you need to save your changes::

	cmsc340router#copy running config
	Destination filename [config]? cmsc340
	%Warning:There is a file already existing with this name
	Do you want to over write? [confirm]

	872 bytes copied in 1.204 secs (724 bytes/sec)
	cmsc340router#


(TODO: http://www.informit.com/library/content.aspx?b=CCNP_Studies_Switching&seqNum=47)

Port Based VLAN
---------------

Telnet to router.

Type ``show vlan``. No VLAN yet.

Get into configuration mode with ``configuration``.

Create a new vlan with ``vlan 13``. Or whatever number. Prompt changes to let
you know what VLAN you are configuring.

Assign ports 1-5 to VLAN 13. ``untagged 1-5``. We won't really tag the
outgoing packets. We will just do it internally. This says 'no tags.'

Type ``exit`` to get out of VLAN 13 config. Type ``exit`` to get out VLAN
config. Type ``show vlan`` and see our new vlan. Type ``show running`` (``sh
ru`` for short) to see the details. Including what ports are part of the VLAN.



.. _SSH: https://en.wikipedia.org/wiki/Secure_Shell
.. _Telnet: https://en.wikipedia.org/wiki/Telnet
.. _Cisco: http://www.cisco.com/c/en/us/index.html
.. _RS-232: https://en.wikipedia.org/wiki/RS-232
