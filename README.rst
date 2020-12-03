shotlast
=============================

**This software is in beta state.**

Watches clipboard and automatically saves any new images.

After run, this program will watch the clipboard.

When a new image is detected, it saves the contents of clipboard with date and time
(year to second) information, such as:
`clip_20201203_101701.png`

- It never deletes a previous image.
- It is fully automatic, you simply fill the clipboard from any source. shotlast does the rest.
- It is useful to save repetitive screenshots from Youtube, Udemy, online meetings, books etc.

In a session, your set of files will look like this:

::

    clip_20201203_101701.png
    clip_20201203_101718.png
    clip_20201203_102226.png
    clip_20201203_102400.png
    clip_20201203_113519.png



Installation
=============================

::

    pip install git+https://github.com/caglartoklu/shotlast

After installation, `pip` will create an executable (`shotlast`) for shotlast.

shotlast then can be used from command line as follows:

::

    shotlast
    shotlast C:\Downloads\Pictures

Note that, on Windows, ``C:\Python3x\Scripts`` directory is NOT automatically added to `PATH` variables.
It is advised to add this directory to `PATH` variables.

or, launch it with a command like this:

::

    C:\Python37\Scripts\shotlast.exe



Command Line Options
----------------------

::

    C:\projects> shotlast --help
    usage: shotlast [-h] [--period [PERIOD]] [target_dir]

    positional arguments:
      target_dir         Target directory to store the saved clipboard files.

    optional arguments:
      -h, --help         show this help message and exit
      --period [PERIOD]  Sleep duration (in seconds) between two clipboard checks.


Examples:

::

    # make the user select the target directory to save clipboard images:
    # period will be 2 (the default value)
    shotlast

    # make the user select the target directory to save clipboard images:
    # period will be 3, the provided value.
    shotlast --period 3

    # use the values as provided:
    shotlast --period 3 c:\Pictures\



Compatibility and Requirements
===================================

**Runtime Requirements**

- Officially, minimum tested Python version supported is 3.7
- Untested: should work with Python 3.5 and above, but not lower, since it uses argparse and pathlib.

**Windows 10**

Tested and developed with Python 3.7.4 on Windows 10.


**Linux**

Untested but it is expected to work.
Waiting for comments from macOS users.


**macOS**

Untested but it is expected to work.
Waiting for comments from macOS users.



Development
==============================

makefile: ``makepile.py``
--------------------------

``makepile.py`` is the make file of this project.
It has no dependencies and it is written in pure Python.

It provides the following commands that can be run from command line:

python makepile.py
--------------------

Shows the main menu of makepile.py and possible targets.

::

    python makepile.py
    Possible targets:
    ['clean', 'install', 'linecount', 'pyinstaller', 'readme', 'uninstall']



To Do
==============================

- ``[ ]`` 3 add requirements file.
- ``[ ]`` 4 create a sub folder in target_dir
- ``[ ]`` 4 upload to Github.
- ``[ ]`` 5 better/colorful output using click.
- ``[ ]`` 5 icon for standalone Windows version.
- ``[ ]`` 5 if there is a file name clash, automatically add a UID.
- ``[ ]`` 5 open the target directory in explorer/finder etc.
- ``[ ]`` 5 standalone Windows version.
- ``[ ]`` 5 test on Linux.
- ``[ ]`` 5 test on macOS.
- ``[ ]`` 5 upload to pypi.
- ``[ ]`` 8 text is not supported yet, should we support it?
- ``[x]`` 5 using makepile.py as makefile.



Licence
==============================

MIT Licensed.
See the `LICENSE.txt <LICENSE.txt>`_ file.

