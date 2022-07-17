.. include:: sub.txt

=======================================
 Windows Subsystem for Linux (Windows)
=======================================

This is a real Linux subsystem for you
to run OpenSeesPy Linux version on Windows.


Install the Windows Subsystem for Linux
---------------------------------------

Follow the instruction on `here <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_
to install Windows Subsystem for Linux on Windows 10.
There are a couple of Linux distributions available and Ubuntu is recommended.
Once the Linux is installed, it will show as an application in the start menu.

.. image:: /_static/start.png

Install Anaconda and start Jupyter Notebook
--------------------------------------------

- Run the subsystem from start menu and a terminal window will show.

  .. image:: /_static/wslterminal.png

- Download Anaconda Linux version with command

  ::

     ~$ wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh


- Install Anconda Linux version with commands

  ::

     ~$ bash Anaconda3-2021.05-Linux-x86_64.sh

     >>> Please answer 'yes' or 'no':
     >>> yes

     >>> Anaconda3 will not be installed into this location:

     [/home/username/anaconda3] >>> (enter)


- Start Jupyter Notebook

     ::

          ~$ /home/username/anaconda3/bin/jupyter-notebook

- Copy the address in red box to a web browser

     .. image:: /_static/wsljupyter.png

     .. image:: /_static/wsljupyter2.png


In Jupyter Notebook
---------------------

Start a new notebook and then

.. image:: /_static/wsljupyter3.png



In the command line (optional)
-----------------------------------------------

- Run Anaconda with following command,
  where `username` is your username of your computer. Please use
  the `username` shown in last step

  ::

     ~$ /home/username/anaconda3/bin/python3.8

  .. image:: /_static/wslanaconda.png

- Install or Upgrade OpenSeesPy with commands

  ::

     ~$ /home/username/anaconda3/bin/python3.8 -m pip install openseespy
     ~$ /home/username/anaconda3/bin/python3.8 -m pip install --upgrade openseespy

  .. image:: /_static/wslinstall.png

- Run OpenSeesPy

  First run Anaconda with

  ::

     ~$ /home/username/anaconda3/bin/python3.8

  Then import OpenSeesPy with

  ::

     import openseespy.opensees as ops
     ops.printModel()

  .. image:: /_static/wslrun.png



- run OpenSeesPy scripts

     ::

          /home/username/anaconda3/bin/python3.8 script.py

