.. _raw-ethernet-tutorial:

Sending Raw Ethernet Tutorial
-----------------------------

Here is C code that will send raw Ethernet packets:

https://gist.github.com/austinmarton/1922600

How do you run this? Save it in a file on your computer. C files should end in
``.c``. Let's call this file ``sendRawEth.c`` because that is what the author
called it.

Now we have to compile it to a computer program. We will use the
`Gnu C Compiler`_. That program is available on the command line of your
Raspberry Pi with ``gcc``

You can compile the code with:

``gcc sendRawEth.c``

But wait! That will make the output of the compile have a default name of
``a.out``. That isn't a good name. Instead let's use:

``gcc sendRawEth.c -o send``

This will use the Gnu C Compiler ``gcc`` to compile the C program ``sendRawEth.c``
and save the output into a file named ``send``.

Now we need to run the program. C compiles into the native language. We don't
need a Java run time, or Python, or whatever. We can just run it.

You can the program with:

``send``

Ah, but wait! We need admin privileges to do something so low-level on the
network. So you might want do use:

``sudo send``

But that doesn't work either. Because by default the admin user only runs command
from directories we know are 'safe.' We need to tell the computer it is ok to run
the command from *this* directory.

You can run the program with:

``sudo ./send``

Want to receive? Here is a program to receive packets:

https://gist.github.com/austinmarton/2862515

.. _Gnu C Compiler: https://en.wikipedia.org/wiki/GNU_Compiler_Collection
