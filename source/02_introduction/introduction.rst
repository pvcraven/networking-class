Introduction
============

There are many organizations that make standards used in networking. One
such organization is the International Organization for Standardization (ISO)
based in Switzerland. ISO created a standard called the
Open Systems Interconnection model (OSI model).

OSI Model
---------

OSI divides up the concept of networking into seven layers:

1. Physical
2. Data-Link
3. Networking
4. Transport
5. Session
6. Presentation
7. Application

This book is organized around these layers. We are going to start at the Physical
Layer and work our way up to the Presentation Layer. As for the Application
Layer? There are many other books
that cover how to write computer applications, so we won't dive into that part
very much.

OSI is a *conceptual* model. There isn't a specific "implementation" of any layer
specified by this model.
What the OSI model does is help when you talk to other people about networking, or when
you want to break apart a complex networking problem into smaller logical parts.

If you have trouble remembering the layers, remember "Please Do Not Touch
Steve's Pet Alligator." Take the first letter from each word of that sentence,
and you have the first letter of each layer.

It is worth remembering the name of each layer and their order.
If you talk to a networking expert and mention that some process happens at
the "networking layer", or "layer 3" they will know what you are talking about.
It is such a popular way to talk about networking that there are even companies
named after "Layer 3".

What does each layer do?

1. Physical: Translates the computer's 1's and 0's to and from pulses of electricity,
   radio waves, or light.
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

OSI Model vs. Reality
---------------------

Some commonly used protocols don't fit neatly into the OSI model.

* Ethernet is often considered as layers 1 and 2.
* TCP/IP runs on layers 3 and 4.
* Web, e-mail, SSH run on layers 5-7.

In this book we will cover the lower networking layers one through six, starting
with the Physical Layer.


Review
------

* What does ISO stand for, and what is it?
* What does OSI stand for?
* What is each layer of the OSI model and what does it do?
* Do real networking implementation fall neatly into the OSI model?