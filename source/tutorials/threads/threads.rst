.. _thread_tutorial:

Thread Tutorial
===============

In computing, threads_ let you perform multiple lines of computing at the
same time. On multi-threaded CPUs it can let you take advantage of a lot more
CPU power.

Python lets you do threads. Kind of. The simplicity of Python also lends to
something called the `Global Interpreter Lock`_. This limits what you can do
with threads on Python. But for our purposes we can ignore it.

.. _threads: https://en.wikipedia.org/wiki/Thread_(computing)
.. _Global Interpreter Lock: https://wiki.python.org/moin/GlobalInterpreterLock

Simple Python Thread Example
----------------------------

Here is an example that spawns several threads that each count from 0 to 9. All
at the same time.

.. literalinclude:: thread_example.py
    :linenos:
    :language: python

Output (Threaded)
-----------------

The output will look something like what is below. You can see all four threads
are counting at the same time.

::

    Thread 0 count 0
    Thread 1 count 0
    Thread 2 count 0
    Thread 3 count 0
    Thread 3 count 1
    Thread 0 count 1
    Thread 1 count 1
    Thread 2 count 1
    Thread 3 count 2
    Thread 2 count 2
    Thread 1 count 2
    Thread 0 count 2
    Thread 3 count 3
    Thread 1 count 3
    Thread 2 count 3
    Thread 0 count 3
    Thread 3 count 4
    Thread 2 count 4
    Thread 1 count 4
    Thread 0 count 4
    Thread 3 count 5
    Thread 0 count 5
    Thread 1 count 5
    Thread 2 count 5
    Thread 3 count 6
    Thread 0 count 6
    Thread 2 count 6
    Thread 1 count 6
    Thread 3 count 7
    Thread 0 count 7
    Thread 1 count 7
    Thread 2 count 7
    Thread 3 count 8
    Thread 0 count 8
    Thread 2 count 8
    Thread 1 count 8
    Thread 3 count 9
    Thread 0 count 9
    Thread 1 count 9
    Thread 2 count 9
    [Finished in 2.6s]

Output (No Threads)
-------------------

If we DIDN'T use threads, we'd have output that looks like this:

::

    Thread 0 count 0
    Thread 0 count 1
    Thread 0 count 2
    Thread 0 count 3
    Thread 0 count 4
    Thread 0 count 5
    Thread 0 count 6
    Thread 0 count 7
    Thread 0 count 8
    Thread 0 count 9
    Thread 1 count 0
    Thread 1 count 1
    Thread 1 count 2
    Thread 1 count 3
    Thread 1 count 4
    Thread 1 count 5
    Thread 1 count 6
    Thread 1 count 7
    Thread 1 count 8
    Thread 1 count 9
    Thread 2 count 0
    Thread 2 count 1
    Thread 2 count 2
    Thread 2 count 3
    Thread 2 count 4
    Thread 2 count 5
    Thread 2 count 6
    Thread 2 count 7
    Thread 2 count 8
    Thread 2 count 9
    Thread 3 count 0
    Thread 3 count 1
    Thread 3 count 2
    Thread 3 count 3
    Thread 3 count 4
    Thread 3 count 5
    Thread 3 count 6
    Thread 3 count 7
    Thread 3 count 8
    Thread 3 count 9
    [Finished in 10.1s]
