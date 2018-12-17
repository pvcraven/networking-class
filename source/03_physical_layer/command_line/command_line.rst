.. _command-line-tutorial:

Tutorial: Basic Command Line
============================


Command Line Tutorial
=====================

Managing a server via command-line can be better than using a graphical interface
with windows and menus. Why?

* It is faster to send text than graphics.
* Commands are reproducable and scriptable. If you document the 45 commands
  (or whatever) you need to set up your server, you can put those 45 commands
  in a script. Then run the script and your server is all set up!

Command Prompt
--------------

The *command prompt* is the bit of text that the computer prints out before
you type in commands. You can `customize this prompt <http://ezprompt.net/>`_, but what UNIX uses
is pretty good by default::

    ubuntu@ip-172-31-39-218:/var/www/sample-web-project/public_html$

This tells me I'm logged in under the user account ``ubuntu`` on the machine
named ``ip-172-31-39-218`` and my current directory is
``/var/www/sample-web-project/public_html``.
I am also logged in as a "normal user" because I have a ``$`` as a command
prompt. If I was an administrator, I would see a ``#``.

It is easy to get confused with terminal windows, and start typing in commands
that are going to a different machine than you expected. Be careful, it is easy
to delete files on a "production" server instead of your own local computer if
you mix up windows.

Directories and Files
---------------------

List files
^^^^^^^^^^
You list files in a directory with the command ``ls`` which is short for "list".
For example::


    ubuntu@ip-172-31-39-218:/etc/apache2$ ls
    apache2.conf  conf-available  conf-enabled  envvars  magic  mods-available  mods-enabled  ports.conf  sites-available  sites-enabled


This is a "short listing" of files. There are
`a lot of options <http://www.rapidtables.com/code/linux/ls.htm>`_ while listing
files. I often use ``ls -la``::

    ubuntu@ip-172-31-39-218:/etc/apache2$ ls -la
    total 88
    drwxr-xr-x  8 root root  4096 Oct 13 15:06 .
    drwxr-xr-x 92 root root  4096 Oct 17 17:44 ..
    -rw-r--r--  1 root root  7115 Jan  7  2014 apache2.conf
    drwxr-xr-x  2 root root  4096 Oct 13 15:06 conf-available
    drwxr-xr-x  2 root root  4096 Oct 13 15:06 conf-enabled
    -rw-r--r--  1 root root  1782 Jan  3  2014 envvars
    -rw-r--r--  1 root root 31063 Jan  3  2014 magic
    drwxr-xr-x  2 root root 12288 Oct 13 15:06 mods-available
    drwxr-xr-x  2 root root  4096 Oct 13 15:06 mods-enabled
    -rw-r--r--  1 root root   320 Jan  7  2014 ports.conf
    drwxr-xr-x  2 root root  4096 Oct 13 15:27 sites-available
    drwxr-xr-x  2 root root  4096 Oct 13 15:06 sites-enabled


The ``l`` gives a "long listing" format. The ``a`` shows "hidden files."

Hidden Files
^^^^^^^^^^^^

You can hide files or directories by default if the name starts with a period (``.``).

Case Sensitivity
^^^^^^^^^^^^^^^^

File and directory names are case sensitive. ``Myfile.txt`` is a completely
different file than ``myfile.txt``.

On Windows, files are not case sensitive, so
when people move to a Linux or Mac environment, links may break because the
web page links to ``Index.html`` when the file name is actually ``index.html``.

Directory Navigation
^^^^^^^^^^^^^^^^^^^^

You can change directories with ``cd <directory>``. For example::

    ubuntu@ip-172-31-39-218:/etc$ cd apache2
    ubuntu@ip-172-31-39-218:/etc/apache2$

Directories are separated by a forward slash: ``/``. This is different than
windows which uses a backslash. ``\``.

When you change directories, everything is relative by default. So if you are
in the ``/home`` directory and type ``cd craven`` you will then be in the
``/home/craven`` directory. You can select more than one directory, so typing
in ``cd craven/documents`` will go into the ``craven`` folder, and inside that
look for a ``documents`` folder.

Sometimes you need to go up a directory. The shorthand for that is ``..``. So
``cd ..`` goes up one directory. Also, ``cd ../..`` goes up two directories.

Occasionally you don't care where you are now. You just want to go to
"exactly this place." If you start a path with a ``/`` you have an *absolute*
directory reference. So going to:

``cd /home/craven``

This will always go to ``/home/craven`` no matter where you are.

Typing ``cd /`` goes to the *root folder* where everything starts.

Typing ``cd ~`` or even just ``cd`` goes to your home directory.
The tilde (~) is often used as a
shortcut for your "home" directory. Usually your home directory is
``/home/my_account_name``.

You can find your current directory with ``pwd``. That is short for Print
Working Directory.

Auto-Complete
^^^^^^^^^^^^^

When working with ``cd`` and other commands, you can often type the first
few letters of a file and hit the "tab" key to auto-fill in the rest. If multiple
files match, keep hitting "tab" until the right one shows up.

Important directories
^^^^^^^^^^^^^^^^^^^^^

How are files on UNIX systems organized? See the
`Wikipedia article <https://en.wikipedia.org/wiki/Unix_filesystem>`_ for
details. The important ones:

* ``/home/<username>`` - All of your user account files are stored here. About
  the same as ``C:\Users\<username>`` on Windows.
* ``/var/www/html`` - This is where your web site files go by default. If you
  have multiple websites served from the same computer, you might instead organize
  them like ``/var/www/site1.com`` and ``/var/www/site2.com``.
* ``/var/log`` - All your log files go here
* ``/var/log/apache2`` - All your web server log files go here
* ``/etc`` - Configuration files
* ``/etc/apache2`` - All your web server configuration files go here
* ``/etc/apache2/sites-enabled`` - All your web server **site** configuration
  files go here

Making Directories
^^^^^^^^^^^^^^^^^^

You can make a directory with the ``mkdir <directory name>`` command. For example
``mkdir music`` will make a directory named ``music`` inside your current
directory.

Copying Files
^^^^^^^^^^^^^

The ``cp`` command will copy files. Here are some examples:

Copy file1.txt into a new file called file2.txt
UNLESS you have a directory named file2.txt, then it
would copy file1.txt into that directory.
(But file2.txt would be a strange directory name.)::

    cp file1.txt file2.txt

Copy file1.txt up one directory::

    cp file1.txt ..

Wildcard
^^^^^^^^

The asterisk (*) is a "wildcard" character. We can use it to copy all files in
the current directory into another directory named 'thumbnails'::

    cp * thumbnails

You can also use it to specify part of a file name. The following command will
only copy ``.jpg`` files::

    cp *.jpg thumbnails

Moving and Renaming Files
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``mv`` command can move and/or rename files. For example:

Rename file1.txt to file2.txt::

    mv file1.txt file2.txt

Move file1 up one directory::

    mv file1.txt ..

Rename file1.txt to 'backup'
OR if a directory named 'backup' exists,
move file1 into the 'backup' directory.::

    mv file1.txt backup

Deleting Files
^^^^^^^^^^^^^^

You can delete a file with the ``rm`` command, which is short for "remove."

This will delete file1.txt::

    rm file1.txt

Deleting Directories
^^^^^^^^^^^^^^^^^^^^

You can delete a directory with ``rmdir``. But the directory must be empty
to do this. If you want to delete directories with files, you can do
``rmdir -rf``

Looking at Files
----------------

cat
^^^

You can display the contents of a file with the ``cat`` command. For example::

    cat myfile.txt

If the file is too big, just hit Ctrl-C to stop the listing.

less
^^^^

The ``less`` command works a lot like ``cat``, but allows you to page through
the file if it is long.

head
^^^^

Sometimes cat displays *too* many lines. You only want to look at the first few
lines. You can use the ``head`` command to look at any number of lines that are
at the beginning. The default is 10.::

    head myfile.txt

tail
^^^^

The ``tail`` command lets you look at the last few lines of the file. For example::

    tail myfile.txt

One of the most useful features of ``tail`` is the ability to *follow* a file. As
a file gets more lines added to it, you can see it update live. For example, if you
want to see what is happening on your web server, live, use::

    tail -f /var/log/apache2/access.log

The ``-f`` tells the computer to "follow" the file, in this case the web access log.
Run this command, and then start accessing your web server. You'll see new lines
appear.

Hit Ctrl-C to stop following.

Editing Files
-------------

There are a lot of ways to edit files. The easiest editor built into most
Linux systems is the ``nano`` editor. It is also slow and quickly frustrating.

The ``vim`` editor is based off an older ``vi`` editor. Once you learn the key
commands and get practiced using it, it is one of the fastest ways to
edit text. Even if you are shelled to another computer and can't use the mouse,
you'll still be faster than someone that has to use a mouse.

Restarting Services
-------------------

There are multiple ways to restart services. The only one you'll really
need to know for this class is::

    sudo service apache2 restart

This will restart the Apache web server. You can also do ``stop`` and
``start``.

All background services available on a UNIX style system are usually in
the directory ``/etc/init.d``. The ``etc`` is the configuration directory.
The ``init`` stands for *initialize* and the ``.d`` is for ``daemon``, which
is the term for a background process.

If you do the following::

    cd /etc/init.d
    ls -la

You can see all the available processes. You can start/stop/restart any
process by putting in the name of the process like this::

    ./apache2 restart

Understanding sudo
------------------

In order to help protect the computer, certain risky changes to
the computer's configuration requires "administrator" privileges.
There are two ways to do this.

First, a person can log in as
an administrator. This is the "root" account on a Linux system.
This is NOT the recommended way of doing things.

Second, a person can be part of the "sudo" group that allows
a normal account to perform administrator actions. You have to
specifically ask for administrator privileges. You can
do with with the "Super-User Do" command.

For example this command will fail if you don't have admin
privileges::

    /etc/init.d/apache2 restart

But this command will work:

    sudo /etc/init.d/apache2 restart

You can also execute any command as someone else with the ``-u``
directive. The web server runs under a user account called
``www-data``. So the following will run the command as if it was
run by ``www-data``::

    sudo -u www-data <my command here>


Installing Software
-------------------

Updating and installing software on a Linux system is usually easy.
The command ``apt-get`` controls adding, updating, and removing software
packages.

Before adding or updating software, you should get the list of what is
available::

    sudo apt-get update

This is similar to Windows "check for updates." We have not updated
anything, we've just seen what is out there.

We can install updates with::

    sudo apt-get upgrade

This will get new software packages. Rarely do you need to restart
your computer like you do with Windows. It is not unusual for
Linux systems to go years without a reboot.

If you want to install new software, you just have to find the
name of the software and install it like this::

    sudo apt-get install apache2

You can list lots of packages on the same line if you like::

    sudo apt-get install apache2 php

You can see all the currently installed software on a system with::

    apt --installed list

The super-cool part of this, is that if you have a working server
you can list all the packages installed with that command. Copy the
list. Then install all those packages on a new server with one
command. Try that on Windows.

Log Out
-------

To log out of the server, type `exit`.


Vim
---

You should learn how to use the Vi editor. Vi and Emacs are two text editors
that most people who work with networks know. We'll just show Vi. Vim is an
enhanced version of Vi. Most people mean Vim now when they say Vi.

Here is an interactive tutorial:

http://www.openvim.com/

After you go through that, here are a couple jokes that will make sense afterwards:

* Vi is a text editor. Vi stands for "Very Intuitive."
* Vi is a very popular editor. Because people can't figure out how to quit.

If you just can't take learning Vi, then use ``nano`` instead.

Other
-----

Here are some other useful commands:

* ``uptime`` - How long has this computer been up and running?
* ``who`` - Who else is logged into the system?
* ``cat /proc/cpuinfo`` – CPU information
* ``cat /proc/meminfo`` – Memory information
* ``df -h`` – Show disk usage
* ``uname -a`` - Show info about the operating system.
* ``top`` - Show a list processes that are taking up the most CPU
* ``ps`` - Show a list of processes that are associated with your account
* ``ps -ef`` - Show extended details about all processes running

Command Line Reference
----------------------

Below is a list of commands you should know. We'll go over them in class:

+---------------------------+------------------------------------------------------+
| Command                   | Action                                               |
+================+=================================================================+
| **Listing Files**                                                                |
+---------------------------+------------------------------------------------------+
| ls                        | Directory listing for the current working directory  |
+---------------------------+------------------------------------------------------+
| ls \*.py                  | List all files ending in .py                         |
+---------------------------+------------------------------------------------------+
| ls -la                    | Directory listing with details and hidden files      |
+---------------------------+------------------------------------------------------+
| ls /                      | List all the files in the root directory             |
+---------------------------+------------------------------------------------------+
| **Directories**                                                                  |
+---------------------------+------------------------------------------------------+
| pwd                       | Print our Working Directory                          |
+---------------------------+------------------------------------------------------+
| cd dir                    | Change current directory to dir. Assumes dir is      |
|                           | in the current directory.                            |
+---------------------------+------------------------------------------------------+
| cd ..                     | Go up one directory                                  |
+---------------------------+------------------------------------------------------+
| cd ../dir                 | Go up one directory, then down into *dir*            |
+---------------------------+------------------------------------------------------+
| cd /                      | Switch to the root directory                         |
+---------------------------+------------------------------------------------------+
| cd /home                  | Switch to the root directory, then look for the      |
|                           | home directory                                       |
+---------------------------+------------------------------------------------------+
| cd                        | Switch to the home directory                         |
+---------------------------+------------------------------------------------------+
| cd ~                      | Switch to the home directory                         |
+---------------------------+------------------------------------------------------+
| cd ~/docs                 | Switch to the docs directory inside the home         |
|                           | directory.                                           |
+---------------------------+------------------------------------------------------+
| mkdir mydir               | Make a new directory called mydir in the current     |
|                           | working directory.                                   |
+---------------------------+------------------------------------------------------+
| **Removing Files**                                                               |
+---------------------------+------------------------------------------------------+
| rm file                   | Remove (delete) file named 'file'.                   |
+---------------------------+------------------------------------------------------+
| rm -rf  mydir             | Remove (delete) directory named 'mydir' and          |
|                           | everything in it.                                    |
+---------------------------+------------------------------------------------------+
| rm -rf  /                 | Remove everything on the computer. THIS IS BAD.      |
+---------------------------+------------------------------------------------------+
| **Moving and Copying Files**                                                     |
+---------------------------+------------------------------------------------------+
| cp file1 file2            | Copy file1, name the copy file2.                     |
+---------------------------+------------------------------------------------------+
| cp file1 ../backup        | Copy file1 up one directory, then either name it     |
|                           | 'backup' or put 'file1' in the directory 'backup' if |
|                           | it already exists.                                   |
+---------------------------+------------------------------------------------------+
| cp \* ../backup           | Copy every file in the current directory up one      |
|                           | directory, and then down into a directory named      |
|                           | 'backup'. This does NOT recurse into subdirectories. |
+---------------------------+------------------------------------------------------+
| cp -r \* ../backup        | Copy every file in the current directory up one      |
|                           | directory, and then down into a directory named      |
|                           | 'backup'. This does DOES recurse into subdirectories.|
+---------------------------+------------------------------------------------------+
| mv file1 file2            | Rename file1 to file2                                |
+---------------------------+------------------------------------------------------+
| mv file1 ..               | Move file1 up one directory.                         |
+---------------------------+------------------------------------------------------+
| mv file1 mydir            | Move file1 into mydir.                               |
+---------------------------+------------------------------------------------------+
| **Displaying Files**                                                             |
+---------------------------+------------------------------------------------------+
| cat myfile                | Displays the contents of myfile                      |
+---------------------------+------------------------------------------------------+
| more myfile               | Displays the contents of myfile, pauses at each page.|
+---------------------------+------------------------------------------------------+
| less myfile               | Displays the contents of myfile, allows page up/down.|
+---------------------------+------------------------------------------------------+
| head myfile               | Displays the first few lines of myfile               |
+---------------------------+------------------------------------------------------+
| tail myfile               | Displays the last few lines of myfile                |
+---------------------------+------------------------------------------------------+
| tail -f myfile            | Displays the last few lines of myfile, then pauses   |
|                           | and will keep printing additional lines as they are  |
|                           | added. Great for following log files.                |
+---------------------------+------------------------------------------------------+
| **Process Management**                                                           |
+---------------------------+------------------------------------------------------+
| ps                        | List active processes                                |
+---------------------------+------------------------------------------------------+
| ps -ef                    | List active processes and details                    |
+---------------------------+------------------------------------------------------+
| top                       | Continually updated list of CPU heavy processes.     |
+---------------------------+------------------------------------------------------+
| kill PID                  | Kill the specified process id with SIGTERM.          |
+---------------------------+------------------------------------------------------+
| kill -9 PID               | Kill the specified process id with                   |
|                           | `SIGKILL <http://turnoff.us/geek/dont-sigkill/>`_.   |
+---------------------------+------------------------------------------------------+
| ctrl-z                    | Move currently running process to background.        |
+---------------------------+------------------------------------------------------+
| command &                 | Run command in the background.                       |
+---------------------------+------------------------------------------------------+
| bg                        | List background processes.                           |
+---------------------------+------------------------------------------------------+
| fg                        | Bring job to forground.                              |
+---------------------------+------------------------------------------------------+
