Lab 5: Session Layer
--------------------

========  ===== ======
Step      Grade Points
========  ===== ======
No steps  F     0
Step 1    F     45
Step 2    F     55
Step 3    D     65
Step 4    C     75
Step 5    B     85
Step 6    A     95
Step 7    A     100
========  ===== ======

Understanding UNIX Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(Easy)

* Create groups and accounts on Raspberry Pi
* Explain why we have groups
* `Here's a tutorial <https://www.tutorialspoint.com/unix/unix-user-administration.htm>`_.
* `Here's another <https://www.linode.com/docs/tools-reference/linux-users-and-groups>`_.
* Understand the ``chmod``, ``chown``, ``useradd``, ``passwd``, ``groups``, ``userdel``, ``newgrp``, ``chgrp`` commands.
* Learn the Chmod Octal Format
* How to create a group, add a person to a group, remove a person from a group
* Explain, in person, how this works.

SSH Using Public/Private Keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(Easy)

* Figure out how to shell to another computer using SSH and a public/private key. Do this
  with two Linux/Mac computers using the ``.ssh`` directory.
* `Tutorial <https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2>`_ (Steps 1-3)
* Make sure you know what directory and files all the key info is stored in. Ask if you
  have trouble figuring it out, because the directory is hidden.
* Demonstrate, in person, the ability to shell between computers this way.

Understanding Cookies
^^^^^^^^^^^^^^^^^^^^^

(Easy)

* Show and explain, in person, how this whole web-cookie thing works.
  If you can't figure it out on your
  own you can ask, but then you must wait 24 hours before you are allowed to
  explain it to me.
* Demonstrate and show what happens with a cookie to manage a session via Wireshark
* You can use this website:
    * `Source code of website <http://webdev.training/index.php?chapter=login_management>`_
    * `Website itself <http://webdev.training/chapters/login_management/v2/main.php>`_
    * The password is "mysecretpassword"
* How is a cookie set? What does across the wire?
* What is the difference between a persistent and a session cookie?
* What is a third party cookie?
* How do you set an expire time on a cookie? (See `cookie options <https://www.nczonline.net/blog/2009/05/05/http-cookies-explained/>`_)
* What is a cookie path?
* Why would you not set a cookie to equal a user name?
* How does a cookie track a user name or other information? How does it hold
  "session data" when none of that is stored in the cookie?
* Session data for most languages is stored in memory.
    * What is the best data structure for doing this?
    * What are disadvantages of doing this?
    * When programming, what do you need to keep in mind because of this?
    * What are advantages/disadvantages of storing data in the database?
* What are the security risks around cookies?
  How `does this work <http://motherboard.vice.com/read/this-5-device-can-hack-your-locked-computer-in-one-minute?utm_source=mbtwitter>`_ and
  how do you stop it?

Encryption Coding
^^^^^^^^^^^^^^^^^

(Hard)

* Use libraries in Java, Python, or whatever to perform:
    * Secret Key Encryption (Like AES)
      (`Example <http://www.quickprogrammingtips.com/java/how-to-encrypt-and-decrypt-data-in-java-using-aes-algorithm.html>`_)
    * Asymmetric Key Encrypting
        * `Example Java RSA <http://www.mysamplecode.com/2011/08/rsa-encryption-decryption-using-bouncy.html>`_
        that uses `Bouncy Castle <https://www.bouncycastle.org/java.html>`_.
    * Hash function (`Hash example <http://stackoverflow.com/questions/3103652/hash-string-via-sha-256-in-java>`_)
* Show me working examples.

E-Mail
^^^^^^

(Easy)

* Write code to send e-mail. You can use libraries.
* Demonstrate that the code works, and e-mail me the code.
* Please don't mail-bomb people.

Web Scrape
^^^^^^^^^^

(Medium)

* Use a library to automatically grab a web page
* Write code that parses that web page (or use a library to do it), and grab
  info from the page automatically.

Web Server
^^^^^^^^^^

(Medium)

Write a very simple web server. Serve up files over port 80. Respond to GET
requests. Write this yourself. You can look at examples, but don't just copy
one.

Single Sign On
^^^^^^^^^^^^^^

(Medium)

Implement `Amazon's login service <http://login.amazon.com/>`_ yourself.
Do it on the Web, Android, or iOS.

http://login.amazon.com/

To get credit for this, you'll need to show and explain the code in operation.

See me if you'd like to do single sign on with Facebook, GitHub, or some other
service instead.
