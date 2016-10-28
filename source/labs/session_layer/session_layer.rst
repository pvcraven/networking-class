Lab 5: Session Layer
--------------------

========  ===== ======
Step      Grade Points
========  ===== ======
No steps  F     0
Step 1    F     55
Step 2    D     65
Step 3    C     75
Step 4    B     85
Step 5    A     95
Step 6    A     100
========  ===== ======

Vocabulary
^^^^^^^^^^

Explain in-person (ideally) or write-up the following vocabulary:

* Explain the following vocabulary:
    * Plaintext_ / Cleartext
    * Ciphertext_
    * `Block Cipher`_
    * `Symmetric Key`_ / Secret key
        * DES_
        * AES_
    * `Asymmetric Key`_
        * What is the "public key" and the "private key"
        * `Diffie-Hellman`_
        * RSA_
    * `Cryptographic hash function`_
        * MD5_
        * SHA_: SHA-1, SHA-2, SHA-3
        * `Rainbow table`_
        * Salt_
    * `Digital Signature`_
    * Two-factor / `multi-factor authentication`_

Note, it is best to store passwords as hashes. SSN and Credit Cards should
always be stored encrypted. It is very likely you will run into this need
during your career.

In my opinion, it should be crimsaving passwords as anything but secure hashes
credit card numbers,

Encryption Coding
^^^^^^^^^^^^^^^^^

* Use libraries in Java or Python to perform:
    * Secret Key Encryption
    * Asymmetric Key Encrypting
    * Hash function

SSH Using Public/Private Keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Figure out how to shell to another computer using SSH and a public/private key. Do this
  with two Linux/Mac computers using the ``.ssh`` directory.

Understanding Cookies
^^^^^^^^^^^^^^^^^^^^^

* Demonstrate and show what happens with a cookie to manage a session via Wireshark

Understanding UNIX Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Create groups and accounts on Raspberry Pi
* Understand ``chmod`` command.

Other stuff
^^^^^^^^^^^

* Set up HTTPS with web?
* Use AWS for login?
* File sharing?

.. _multi-factor authentication: https://en.wikipedia.org/wiki/Multi-factor_authentication
.. _SHA: https://en.wikipedia.org/wiki/Secure_Hash_Algorithm
.. _MD5: https://en.wikipedia.org/wiki/MD5
.. _Rainbow table: https://en.wikipedia.org/wiki/Rainbow_table
.. _Plaintext: https://en.wikipedia.org/wiki/Plaintext
.. _Ciphertext:  https://en.wikipedia.org/wiki/Ciphertext
.. _Symmetric Key: https://en.wikipedia.org/wiki/Symmetric-key_algorithm
.. _DES: https://en.wikipedia.org/wiki/Data_Encryption_Standard
.. _Block Cipher: https://en.wikipedia.org/wiki/Block_cipher
.. _AES: https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
.. _Asymmetric Key: https://en.wikipedia.org/wiki/Public-key_cryptography
.. _Diffie-Hellman: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
.. _RSA: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
.. _Cryptographic hash function: https://en.wikipedia.org/wiki/Cryptographic_hash_function
.. _Salt: https://en.wikipedia.org/wiki/Salt_(cryptography)
.. _Digital Signature: https://en.wikipedia.org/wiki/Digital_signature
