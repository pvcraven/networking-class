Tutorial: Basic Command Line
============================

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

Oh, didn't remember it all from class? Or you weren't in class that day?
Or you want to learn more?

No problem. I recommend reading through this site:

http://linuxcommand.org/learning_the_shell.php

The Bash shell is a full programmable language. Linux machines are nice because
you can script and automate many things that aren't possible to do with a GUI.
But it takes longer to learn.

Vim
^^^

You should learn how to use the Vi editor. Vi and Emacs are two text editors
that most people who work with networks know. We'll just show Vi. Vim is an
enhanced version of Vi. Most people mean Vim now when they say Vi.

Here is an interactive tutorial:

http://www.openvim.com/

After you go through that, here are a couple jokes that will make sense afterwards:

* Vi is a text editor. Vi stands for "Very Intuitive."
* Vi is a very popular editor. Because people can't figure out how to quit.

If you just can't take learning Vi, then use ``nano`` instead.