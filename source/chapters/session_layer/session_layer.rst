Session Layer
=============

The `session layer`_ is responsible for opening, closing, and managing a session
between two nodes.

It provides:

* Authentication - Are you who you say you are?
* Authorization - Do you have permission to do/access this?

It is also responsible for recreating the connection if it gets dropped. And in
some cases (like the web) you might have multiple connections open as part
of a session.

Protocols You Should Know
-------------------------

Some of these protocols extend across multiple layers. One could even argue
some aren't part of layer 5 at all. But for our purposes this is where we will
talk about them.

File Transfer Protocol (FTP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `File Transfer Protocol`_ predates HTTP. For a while it was one of the main
methods of traversing the Internet, before HTTP/HTML became popular.

The `TL;DR`_ of FTP is: It isn't secure, don't use it any more.

There are some older servers out there that use FTP to serve up files.
You can download from FTP anonymously, or with a user name and password. The
user name and password are sent in clear text, so anyone packet-sniffing can
grab them.

You can access an FTP server with a web browser using the following format::

	ftp://[user[:password]@]host[:port]/url-path

For example::

	ftp://paul_craven:mypassword@cs.simpson.edu/mydir/myotherdir/myfile.zip

There are dedicated FTP clients. My favorite is FileZilla_.
These are great if you have a large number of files to move from one spot to another.
HOWEVER, it now appears that FileZilla has adware. Even though it allows you
to opt-out of it, I'm not so wild about that.

FTP runs by default on port 21.

**Alternatives:**

There are other alternatives to FTP:

* FTPS: Encrypts the session. Outdated.
* SFTP: File Transfer Protocol: Sends files over an SSH connection. FileZilla
  can transfer files this way. MobaXTerm does this on the side. This is the
  better way to do things.
* Use HTTP


If you want to grab a file off the web via the command-line, use the
``wget`` command::

	wget http://cs.simpson.edu/myfile.zip

If you want to keep two directories synchronized, use rsync_. I've wasted a lot
of time with rsync, so I don't personally like it. But a lot of other people do
like it.

Network Time Protocol (NTP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you "automatically set the time" on your computer you are likely using the
`Network Time Protocol`_. It does a great job of synchronizing clocks and
accounting for the round-trip delay that happens on a network. It also limits
the number of queries to "Stratum 0" atomic-precision clocks.

The algorithm and history behind NTP is rather interesting, but probably not
necessary to learn for most people. If you are interested in finding out more,
read the Wiki link.

You can see NTP in action by turning on and off the "set time automatically"
on your PC:

.. image:: time_settings.png
    :width: 450px
    :align: center

Then run Wireshark to see the packets:

.. image:: ntp_packets.png
    :width: 600px
    :align: center

Large organizations might set up their own NTP server to reduce outside traffic.

Alternatively, devices often grab an accurate clock off phone towers or GPS
devices.

Simple Mail Transfer Protocol (SMTP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Simple Mail Transfer Protocol`_ (SMTP) is the protocol used to deliver e-mail over
the Internet. It runs on port 25.

Interestingly, SMTP is NOT the protocol you use to get mail from your server.
SMTP takes the mail from when you send it, to your mail server. A client will use
a different protocol to fetch the mail from the mail server. (POP3, IMAP,
Web Client, etc.)

SMTP is a very simple protocol. For this reason, spam email proliferated for
many years. In the early days of the Internet, a SMTP servers would take messages
from anyone and deliver them anywhere.

So you could sit in a coffee shop in Indianola and run a program that hooked up
to a SMTP server in China and send thousands of messages to an e-mail list you
have. Furthermore, you could make it look like it came from president@whitehouse.gov
just as easily as your actual e-mail.

There are more controls in place now, but it is still easy to send mail using
SMTP. Even just using Telnet.

Note: In the example below I was unable to use MobaXTerm because of the different
line endings between Windows and UNIX. I instead shelled to a Linux machine and
then to mail.simpson.edu.

.. code-block:: none
    :emphasize-lines: 1,6,8,10,12,14-20,22

    craven@cs ~ $ telnet mail.simpson.edu 25
    Trying 207.32.33.199...
    Connected to mail.simpson.edu.
    Escape character is '^]'.
    220 cas3.sc.loc Microsoft ESMTP MAIL Service ready at Fri, 4 Nov 2016 12:27:18 -0500
    HELO simpson.edu
    250 cas3.sc.loc Hello [207.32.33.199]
    MAIL from: <paul.craven@simpson.edu>
    250 2.1.0 Sender OK
    RCPT to: <paul.craven@simpson.edu>
    250 2.1.5 Recipient OK
    DATA
    354 Start mail input; end with <CRLF>.<CRLF>
    From: dude@dude.com
    To: paul.craven@simpson.edu
    Subject: Hi

    This is a test

    .
    250 2.6.0 <fcf8afb4-10f5-489d-8bca-6dc03b3d7105@CAS3.sc.loc> [InternalId=6924808] Queued mail for delivery
    QUIT
    221 2.0.0 Service closing transmission channel
    Connection closed by foreign host.


You don't have to manually write the code to send e-mail however.
There are many libraries out there for sending e-mail from a program. See
`here <https://docs.python.org/3.5/library/email-examples.html>`_ for how
to do it in Python.

JavaMail is used for Java, you can see a tutorial
`here <http://crunchify.com/java-mailapi-example-send-an-email-via-gmail-smtp/>`_.

Multipurpose Internet Mail Extensions (MIME)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MIME_-encoded messages are the way complex mail messages are sent over the
internet. It can support e-mails that have both plain-text, RTF, and HTML
formatted variants. You can attach files to an e-mail message via MIME.

MIME is recursive. So it is possible to put a MIME message inside a MIME message
and so forth.

Internet Message Access Protocol (IMAP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ok, most people now access their e-mail via a web client. But if you wanted to
use a program to manage e-mail, (like Thunderbird_) then it would typically
interface with the server via IMAP_.

IMAP replaced POP3 and added folders, push notifications and a lot of other
functionality.

.. _IMAP: https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol
.. _Thunderbird: https://www.mozilla.org/en-US/thunderbird/

Hyper Text Transfer Protocol (HTTP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can try fetching web pages manually by telneting to port 80 on the
server. Here I've done a telnet to simpson.edu and typed ``GET /``.

.. code-block:: none
	:emphasize-lines: 4

	Trying 198.206.243.15...
	Connected to simpson.edu.
	Escape character is '^]'.
	GET /
	<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
	<html><head>
	<title>301 Moved Permanently</title>
	</head><body>
	<h1>Moved Permanently</h1>
	<p>The document has moved <a href="http://simpson.edu/culver-center/">here</a>.</p>
	<hr>
	<address>Apache/2.2.15 (CentOS) Server at culvercenter.org Port 80</address>
	</body></html>
	Connection closed by foreign host.

Note that I didn't get the Simpson web page. What gives? Web servers can serve
multiple sites. Since we didn't select which site, it gave us the default. Also
we used the original HTTP version, not the updated 1.1 that everyone uses now.

So here I've specified the URL and the modern version of HTTP:

.. code-block:: none
	:emphasize-lines: 4-6

	Trying 198.206.243.15...
	Connected to simpson.edu.
	Escape character is '^]'.
	GET / HTTP/1.1
	Host: simpson.edu

	HTTP/1.1 200 OK
	Date: Fri, 04 Nov 2016 16:48:02 GMT
	Server: Apache/2.2.15 (CentOS)
	Last-Modified: Fri, 04 Nov 2016 16:15:11 GMT
	ETag: "4849d-e2ab-5407bfa884c96"
	Accept-Ranges: bytes
	Content-Length: 58027
	Vary: Accept-Encoding,Cookie
	X-Powered-By: W3 Total Cache/0.9.3-subdir-fix
	Connection: close
	Content-Type: text/html; charset=UTF-8

	<!doctype html>
	And so forth...

If you get into making high-performance web sites, you'll need to understand
the HTTP protocol in more detail.

Try `WebPageTest.org <https://www.webpagetest.org/>`_ on a website like
`Hy-Vee's <http://hyvee.com>`_. Also look at the `HTTP status codes`_ and see how
those codes work on the 2nd request.


Lightweight Directory Access Protocol / Active Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Larger organizations typically use a version of
`Lightweight Directory Access Protocol`_ (LDAP) for managing user accounts.

Microsoft has `Active Directory`_ (AD) which includes an LDAP implementation.

You can use LDAP in your programs to log people in. For example, this PHP code
snipped uses LDAP to check ``$username`` and ``$password`` for a valid login
on a LDAP server.

.. code-block:: php

    $hostname = "ldap://my-ldap-server.mydomain.com/";

    $con =  ldap_connect($hostname);
    if (!is_resource($con))
        die("Unable to connect to $hostname");
    ldap_set_option($con, LDAP_OPT_PROTOCOL_VERSION, 3);
    ldap_set_option($con, LDAP_OPT_REFERRALS, 0);

    if (!ldap_bind($con, $username . "@mydomain.com" , $password))
    {
        $messages['LDAP']="<p class='errormsg'>Error - Login Failed</p>";
        $error=True;
    }
    ldap_close($con);

.. code-block:: none
    :emphasize-lines: 4


Encryption Keys
---------------

Symmetric
^^^^^^^^^

Asymmetric
^^^^^^^^^^

Using Keys with SSH
^^^^^^^^^^^^^^^^^^^

Using Keys with HTTPS
^^^^^^^^^^^^^^^^^^^^^

Cookies
-------

Streaming
---------

https://sidbala.com/h-264-is-magic/

.. _File Transfer Protocol: https://en.wikipedia.org/wiki/File_Transfer_Protocol
.. _TL;DR: https://en.wikipedia.org/wiki/Wikipedia:Too_long;_didn%27t_read
.. _FileZilla: https://filezilla-project.org/
.. _Simple Mail Transfer Protocol: https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol
.. _Internet Message Access Protocol: https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol
.. _Network Time Protocol: https://en.wikipedia.org/wiki/Network_Time_Protocol
.. _Lightweight Directory Access Protocol: https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol
.. _Active Directory: https://en.wikipedia.org/wiki/Active_Directory
.. _MIME: https://en.wikipedia.org/wiki/MIME
.. _HTTP status codes: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
.. _session layer: https://en.wikipedia.org/wiki/Session_layer
.. _rsync: https://en.wikipedia.org/wiki/Rsync

