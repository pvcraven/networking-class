.. _tomcat_tutorial:

Tomcat Tutorial
===============

Getting set up
--------------

* To begin with,
  `download Tomcat <http://tomcat.apache.org/download-90.cgi>`_.
  There are a lot of versions, but I chose
  Tomcat 9, the Windows "64-bit Windows zip" .zip file.
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

Serving static files
--------------------

* Ok, if it is running, let's create an app. Create a new directory under the
  ``webapps`` folder in Tomcat. Keep it lower case and don't use spaces. Like
  ``test-app``.
* Create a test html file in that folder. I created ``webapps\test-app\test.html``
* Restart Tomcat
* Go to ``http://localhost:8080/test-app/test.html`` and you should be able to
  see the static file you created. This is where your static images, css, and
  other files that don't change go.

Creating a servlet
------------------

* Create a ``WEB-INF`` folder in the ``test-app`` folder.
* Create a ``classess`` folder in the ``WEB-INF`` folder.
* Inside the ``WEB-INF`` folder make your Servlet. Here's a sample:

.. literalinclude:: TestServlet.java
    :linenos:
    :language: java

* Inside the ``WEB-INF`` folder create a file named ``web.xml``. Inside of
  ``web.xml`` put the following::

    <web-app>
      <servlet>
        <servlet-name>TestServlet</servlet-name>
        <servlet-class>TestServlet</servlet-class>
      </servlet>

      <servlet-mapping>
        <servlet-name>TestServlet</servlet-name>
        <url-pattern>/test</url-pattern>
      </servlet-mapping>
    </web-app>

* Compile the code. You'll probably need something like ``javac TestServlet.java``
* Wait! You need to include a library to compile it. You'll need something like
  ``javac -classpath ..\..\..\..\lib\servlet-api.jar TestServlet.java``
* Restart Tomcatg
* Try your servlet: ``http://localhost:8080/test-app/test``
