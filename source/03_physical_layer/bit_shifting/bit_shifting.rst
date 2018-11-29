Bit Shifting
------------

Ok, we know that numbers and letters are stored in binary. But how
do you convert from a number or a letter to binary? Perhaps you
forgot? Or you haven't taking "computer organization" yet as a
class?

No worries!

Here are a couple examples to help you get started. Be sure to
have your instructor step you through how they work.

This one shows, in detail, decoding one value.

.. literalinclude:: print_binary.py
    :linenos:
    :language: python

Wait, what does this weird line do? ``bit = 1 << bit_pos & number_to_encode``?

First off, the number 1 in binary is::

  0000 0001

The ``<<`` is a bit-shift operator. So::

  1 << 0 = 0000 0001 =   1
  1 << 1 = 0000 0010 =   2
  1 << 2 = 0000 0100 =   4
  1 << 3 = 0000 1000 =   8
  1 << 4 = 0001 0000 =  16
  1 << 5 = 0010 0000 =  32
  1 << 6 = 0100 0000 =  64
  1 << 7 = 1000 0000 = 128

The ``&`` is a bitwise 'and'. So::

  'z' in ASCII = 122 = 0111 1010

  First bit
    0111 1010
  & 0000 0001
    ---------
    0000 0000 = 0

  Second bit
    0111 1010
  & 0000 0010
    ---------
    0000 0010 = 2 (non-zero)

  Third bit
    0111 1010
  & 0000 0100
    ---------
    0000 0000 = 0

  Fourth bit
    0111 1010
  & 0000 1000
    ---------
    0000 1000 = 8 (non-zero)

  ..and so on.

This next code listing takes it a step further by decoding a list/array of
values.

.. literalinclude:: print_bytes.py
    :linenos:
    :language: python
