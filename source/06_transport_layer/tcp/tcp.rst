.. _tcp_tutorial:

Send and Receive Data with TCP
==============================


Send TCP Message
----------------

This is a very simple example that will send a message.

.. literalinclude:: send_tcp.py
    :linenos:
    :language: python

Receive TCP Message, Blocking
-----------------------------

This will receive a message. It will wait forever to get the message. It is
very hard to stop this program because it does not respond to Ctrl-C. You need
to kill the process.

Normally, you don't use blocking calls to read from the network. But it is
an easy set of code to understand conceptually.

You *might* run blocking commands if they are in their own thread.

.. literalinclude:: receive_tcp_blocking.py
    :linenos:
    :language: python

Receive TCP Message, Non-Blocking
---------------------------------

Here we keep our loop going, so the program can be responsive. It is a bit
more complex however.

.. literalinclude:: receive_tcp_nonblocking.py
    :linenos:
    :language: python

Send a big TCP message
----------------------

Need to send a bigger message? Here's an example. It is like the original,
but uses multiplication to make a message of any size.

.. literalinclude:: send_tcp_large.py
    :linenos:
    :language: python

Receive a Big Multi-part Message
--------------------------------

Ok, the prior receive examples didn't work if you needed to get data that arrived
in more than one "chunk."
We can only receive so much data at a time. As soon as we got the first part,
we stopped listening. That only works for short messages.

This example keeps reading data until we get the whole
message. We signal that we are at the end of our message by a newline character,
\\n which is ASCII value 10.

.. literalinclude:: receive_tcp_nonblocking_large.py
    :linenos:
    :language: python

Send Lots of Messages
---------------------

This loops and sends lots of messages. Normally we send a bunch of X's followed
by a newline::

    XXXX\n

So that the receiver can know we are done, the last message is a Y (ASCII value
89)::

    Y\n

.. literalinclude:: send_tcp_multiple.py
    :linenos:
    :language: python

Receive Multiple Messages
-------------------------

Receive lots of messages, and calculate the data rate.

.. literalinclude:: receive_tcp_nonblocking_multiple.py
    :linenos:
    :language: python


Lots of Python networking examples:

https://github.com/crazyguitar/pysheeet/blob/master/docs/notes/python-socket.rst
