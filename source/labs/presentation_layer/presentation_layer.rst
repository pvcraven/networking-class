Lab 6: Presentation Layer
-------------------------

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

* To begin with, download Tomcat. There are a lot of versions, but I chose
  Tomcat 9, the Windows .zip file.
* Expand the Tomcat zip file somewhere to work with.
* Make sure you have Java installed. Use your file browser to find it. You are
  looking for a folder that starts with ``jdk`` and **not** ``jre``. The
  JDK allows you to compile, the JRE just allows you to run Java. For me it was
  in ``C:\Program Files\Java\jdk1.8.0_31``. Create an environment variable called
  ``JAVA_HOME`` and set it to this path. If you don't know how to set an environment
  variable, then ask.
* Make sure you have the ``bin`` directory in your path. For me it looks like
  ``C:\Program Files\Java\jdk1.8.0_31\bin``. If you don't know how to add something
  to your path, or what it does, please ask.
* If you don't have Java installed, then Google it up. Or
  `this link <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`_
  might work.
* Next, to start Tomcat, open up a command prompt and change to the Tomcat
  ``bin`` directory. Type ``catalina start``. This will open up a new window
  with the running Tomcat. You can then direct your web browser to
  ``http:\\localhost:8080`` and check to make sure it is running.
* Ok, if it is running, let's create an app. Create a new directory under the
  ``webapps`` folder in Tomcat. Keep it lower case and don't use spaces. Like
  ``test-app``.
* Create a test html file in that folder. I created ``webapps\test-app\test.html``
* Create a ``WEB-INF`` folder in the ``test-app`` folder.
* Inside the ``WEB-INF`` folder create a file named ``web.xml``. Inside of
  ``web.xml`` put the following::

    <web-app>
    </web-app>

* Restart Tomcat
* Go to ``http://localhost:8080/test-app/test.html`` and you should be able to
  see the static file you created. This is where your static images, css, and
  other files that don't change go.

Raster Images
^^^^^^^^^^^^^

(Hard)

Write a Java Servlet that serves up a dynamic image. (Don't read it from
a file, draw it.) Output in any raster graphics format.

http://searchdomino.techtarget.com/tip/Generating-dynamic-images-using-servlet

Vector Images
^^^^^^^^^^^^^

(Hard)

Output an image in SVG format.

PDF
^^^

(Really hard)

Write a Java Servlet that serves up a PDF.

http://www.onjava.com/pub/a/onjava/excerpt/java_cookbook_ch18/?page=6

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
