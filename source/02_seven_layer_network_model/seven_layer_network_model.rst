Seven Layer Network Model
=========================

Networking computers requires standards. We want to be able to have our computers,
routers, cables, and wireless all work together regardless as to what vendor created
the product.

There are many organizations that make standards used in networking. One
such organization is the International Organization for Standardization (ISO)
based in Switzerland. ISO created a standard called the
Open Systems Interconnection model (OSI model).

OSI divides up the concept of networking into seven layers.

1. Physical
2. Data-Link
3. Networking
4. Transport
5. Session
6. Presentation
7. Application

If you have trouble remembering the layers, remember "Please Do Not Touch
Steve's Pet Alligator." Take the first letter from each word of that sentence,
and you have the first letter of each layer.

What does each layer do?

1. Physical: Takes pulses of electricity, radio waves, or light to transmit
   1's and 0's.
2. Data-Link: Transfers chunks of data called **frames** direct from one computer to
   another. A networking hub or switch operates at this level.    
3. Networking: Transfers chunks of data called **packets** from one computer to another
   across multiple hops or through devices called routers.
4. Transport: Figures out how to break large files or streams of data into packets.
   Figure out when to acknowledge packets sent.
5. Session: Open and close networking "sessions". Can be used to keep networking
   traffic from one program on your computer separate from a different program
   (ports).
   Can keeps track of a person across multiple requests on the network.
   Handling
   a log in and tracking what they do happens here.
6. Presentation: Know how to display information. Such as web pages, PDF documents,
   images, text screens. Data compression and encryption typically happen here.
7. Application: A computer program that responds to user input or runs as a
   background service. Such as a web browser, a networked video game, or social
   app.

The idea that information is passed up and down the different layers:

.. image:: osi_model.svg
    :align: center
    :alt: alternate text

OSI is a *conceptual* model. There isn't a specific "implementation" of any layer.
What it does help is when you talk to other people about networking, or when
you want to break apart a complex networking problem into smaller logical parts.

Some commonly used protocols don't fit neatly into the OSI model.

* Ethernet is often considered as layers 1 and 2.
* TCP/IP runs on layers 3 and 4.
* Web, e-mail, SSH run on layers 5-7.

If you talk to a networking expert and mention that some process happens at
the "networking layer", or "layer 3" they will know what you are talking about.
It is such a popular way to talk about networking that there are even companies
named after "Layer 3".

In this book we will cover the lower networking layers one through six, starting
with the Physical Layer.


Review
------

* What is ISO_?

* What is the `OSI model`_?

  * Make sure you can briefly name each layer
  * Make sure you can describe each layer
  * Be ready to be called on in class to do so

* Learn "Please Do No Touch Steve's Pet Alligator" as a mnemonic to learn
  the different OSI model layers.

For quick reference and explanation, I like this graphic I got from
`Building Automation Monthly`_.

Study it in detail.

A good portion of the class will be dedicated to understanding all seven layers.
We will start with the physical layer and work our way up. The end of class
will be focused on the security aspects of networking.

.. _ISO: https://en.wikipedia.org/wiki/International_Organization_for_Standardization
.. _OSI Model: https://en.wikipedia.org/wiki/OSI_model
.. _Building Automation Monthly: http://blog.buildingautomationmonthly.com/what-is-the-osi-model/