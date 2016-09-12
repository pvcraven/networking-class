Raspberry Pi Setup
==================

Basic Setup and Installation
----------------------------

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
* Go to 'menu...preferences...mouse and keyboard settings'.
* Change your keyboard to US. (Might need to scroll up to see it.)
* Open up a terminal

  * Type ``sudo apt-get update``
  * Type ``sudo apt-get upgrade``
  * Wait a really long time

* Done!

Getting on to the Network
-------------------------

The easiest way is to get on with a pre-shared key. Ask your
instructor for how to do this. Simpson's student network won't
let you on because you don't have anti-virus software.

Below are instructions for getting on if you have an exception
for that. You can just ignore this probably, but I'm leaving
it here because it took me a long time to figure out.

Open a terminal window.

Now, encode your password:

echo -n 'YOUR_REAL_PASSWORD' | iconv -t utf16le | openssl md4 > hash.txt

Open another terminal window.

Edit the configuration file with nano or vim:

``sudo nano /etc/wpa_supplicant/wpa_supplicant.conf``

network={
    ssid="staff"
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

Replace
