Raspberry Pi Setup
==================

Basic Setup and Installation
----------------------------

**Notice:** The Raspberry Pi detects the monitor's resolution on start-up. If
you plug in the power, then the monitor, you'll be stuck at a really low default
resolution. So plug in the monitor before you power the board.

* Pull out the motherboard
* Put it in the case
* Install the memory card. (Pink package, upside down)
* Install the heatsinks
* Plug in the GPIO board. The NEGATIVE power gets plugged into the BLUE lines
  on the breadboard.
* Install the cable from the GPIO board to the computer
* Plug in the:

  * Power supply
  * Network cable (Wifi is built in, but putting the box on Simpson's network is a pain. If you don't have a wired connection available, see the section below on how to get onto Simpson's network.)
  * Keyboard
  * Mouse
  * Monitor

* Boot
* Select an install of Raspbian OS. (It's the only option)
* Wait a really long time.
* Reboot
* Open up a terminal

  * Type ``sudo apt-get update``
  * Type ``sudo apt-get upgrade``
  * Wait a really long time

* Done!

Getting on to Simpson's Network
-------------------------------

Open a terminal window.

Now, encode your password:

``echo -n 'YOUR_REAL_PASSWORD' | iconv -t utf16le | openssl md4``

Open another terminal window.

Edit the configuration file with nano or vim:

``sudo nano /etc/wpa_supplicant/wpa_supplicant.conf``

Then, add the section below. If there already is a section for student, remove
it and replace it with this. If you have a section scguest, remove that.
Replace ``USERNAME`` with your username.

Next, replace the password with the hash we created above.
You can copy and paste between windows using ctrl-insert and shift-insert.
ctrl-x and ctrl-c do something totally different than copy-paste.

Note that you need ``hash:`` in front of your hash::

    network={
        ssid="student"
    	priority=1
    	proto=RSN
    	key_mgmt=WPA-EAP
    	pairwise=CCMP
    	auth_alg=OPEN
    	eap=PEAP
    	identity="USERNAME"
    	password=hash:9a6e.....2782
    	phase1="peaplabel=0"
    	phase2="auth=MSCHAPV2"
    }

Save the file. Then reboot the raspberry pi. You can do it with the GUI
or by typing ``sudo shutdown -r now``.

Don't try to select the student network from the wireless menu. That will change
the configuration file you just edited. Specifically, in my case it changed the
``key_mgmt`` to something that didn't work.

Shutdown and Reboot
-------------------

Like any computer, the Raspberry Pi should be shut down properly. Don't just
unplug it. The easiest way is to use the GUI. If you want to use the terminal,
this command shuts down (halts) the computer:

``sudo shutdown -h now``

This one reboots:

``sudo shutdown -r now``
