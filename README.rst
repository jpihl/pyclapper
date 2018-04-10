pyclapper
=========
pyclapper a python tribute to the 80s classic, The Clapper!

.. image:: https://raw.githubusercontent.com/jpihl/pyclapper/master/clapper.gif
   :target: https://youtu.be/Ny8-G8EoWOw

Installation
------------
pyclapper have been tested on Linux, and requires the following python libraries available:

* ``pygame`` version ``1.9.1release``
* ``pyaudio`` version ``0.2.8``

Other versions may work as well, these are simply the ones which have been tested.

Usage
-----
The pyclapper repository contains 3 files:

* ``clapper.py`` contains a function that calls a given callback when a double clap is detected.
* ``light.py`` contains a simple pygame class which creates a full screen application that can
  toggle between black and white - simulating a light.
* ``main.py`` application combining ``clapper.py`` and ``light.py`` to toggle the light.

Test it out by running the ``main.py`` file::

    python main.py
