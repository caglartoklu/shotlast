shotlast
=============================

Watches clipboard and automatically saves any new images, text and files.

After run, this program will watch the clipboard.

When a new image/text/file is detected, it saves the contents of clipboard with date and time
(year to second) information, such as: `clip_20201203_101701.png`

- It never deletes a previous image/text/file.
- It is fully automatic, you simply fill the clipboard from any source. shotlast does the rest.
- It is useful to save repetitive screenshots from Youtube, Udemy, online meetings, books etc.

In a session, your set of files will look like this:

.. image:: https://user-images.githubusercontent.com/2071639/101167570-2409c800-364b-11eb-9393-7dd7daff8cd9.png

.. image:: https://user-images.githubusercontent.com/2071639/101167591-2ff58a00-364b-11eb-9f6e-f1b9077468a6.png



Installation
=============================

::

    pip install git+https://github.com/caglartoklu/shotlast

After installation, `pip` will create an executable (`shotlast`) for shotlast.

shotlast then can be used from command line as follows:

::

    shotlast
    shotlast C:\Downloads\Pictures


Installation Notes for Windows
------------------------------------

1 PATH variables
....................................

Note that, on Windows, ``C:\Python3x\Scripts`` directory is NOT automatically added to `PATH` variables.
It is advised to add this directory to `PATH` variables.

or, launch it with a command like this:

::

    C:\Python37\Scripts\shotlast.exe


Installation Notes for Linux
------------------------------------

1 Tkinter
....................................


Tkinter is not installed on some Linux derivatives by default.
For Debian Linux derivatives, it is installed by:

::

    sudo apt-get install python3-tk


2 copy/paste mechanism
....................................

pyperclip (the clipboard library used by shotlast)
requires a copy/paste mechanisms for Linux derivatives.
If no mechanism is found, pyperclip will raise a
`NotImplementedError <https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error>`_
.

A copy/paste mechanisms must be provided by installing one of the following:

``sudo apt-get install xsel`` to install the xsel utility.

``sudo apt-get install xclip`` to install the xclip utility.

``pip install gtk`` to install the gtk Python module.

``pip install PyQt4`` to install the PyQt4 Python module.




Command Line Options
=============================

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

- Required Python packages are defined in `setup.py <setup.py>`_ file.
- Officially, minimum tested Python version supported is 3.7
- Untested: should work with Python 3.5 and above, but not lower, since it uses argparse and pathlib.

**Windows 10**

Tested and developed with Python 3.7.4 on Windows 10.


**Linux**

Untested but it is expected to work.
Waiting for comments from Linux users.


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

Development Environment
---------------------------------

::

    pip -m venv v1
    cd v1
    cd Scripts
    activate
    cd /path/to/shotlast_source_dir
    pip install -r requirements.txt

makepile can also use `cloc <https://github.com/AlDanial/cloc>`_ to count the lines in the project.



Licence
==============================

MIT Licensed.
See the `LICENSE.txt <LICENSE.txt>`_ file.

