Lab 6: Presentation Layer
--------------------

========  ===== ======
Step      Grade Points
========  ===== ======
No steps  F     0
Step 1    F     45
Step 2    D     65
Step 3    C     75
Step 4    B     85
Step 5    A     93
Step 6    A     100
========  ===== ======

HTML/CSS
^^^^^^^^

(Easy)

Get a server working using `Apache Tomcat <http://tomcat.apache.org/>`_.

Write a Java Servlet (no JSPs) to demonstrate display using HTML/CSS.
The CSS can be a static file, but generate the HTML with a Servlet. There are
several examples out there:

http://helloworldprograms.blogspot.com/2010/08/servlet-hello-world.html

Raster Images
^^^^^^^^^^^^^

(Hard)

Write a Java Servlet that serves up a dynamic image. (Don't read it from
a file, draw it.) Output in any raster graphics format.

http://searchdomino.techtarget.com/tip/Generating-dynamic-images-using-servlet

Then create a servlet that outputs the image. You'll need to set the content
type to ``image/png`` or ``image/jpg``.

Vector Images
^^^^^^^^^^^^^

(Medium)

Output an image in
`SVG format <https://en.wikipedia.org/wiki/Scalable_Vector_Graphics>`_. Make
it your own image, not something you copied.

You should use a static file that links in an image::

    <img src="my_image_servlet">

Then create a servlet that outputs the image. You'll need to set the content
type to ``image/svg``.

PDF
^^^

(Really hard)

Write a Java Servlet that serves up a PDF.

http://www.onjava.com/pub/a/onjava/excerpt/java_cookbook_ch18/?page=6

The PDF should be dynamically generated. Don't just read the PDF in from a
file.

JavaScript
^^^^^^^^^^

(Easy)

Write a demo that shows how to use JavaScript to draw on a Canvas.

http://www.w3schools.com/html/html5_canvas.asp

ANSI ASCII
^^^^^^^^^^

(Easy)

Write a program on the Raspberry Pi that uses
`ANSI ASCII <https://en.wikipedia.org/wiki/ANSI_escape_code>`_:

* Outputs text in different colors.
* Can clear the screen
* Can position a character exactly where you want it.

If you want to program in Python, see the
`Curses library <https://docs.python.org/2/library/curses.html>`_.
