.. include:: sub.txt

================
 PyPi (Mac)
================

Install Dependencies
--------------------

* Install `MacPorts <https://www.macports.org/install.php>`_ for your macOs.
* Install `gcc8 <https://ports.macports.org/port/gcc8>`_

  ::
     
     sudo port install gcc8
	     
Install Python
--------------

* Install Python 3.8 using MacPorts

  ::

     sudo port install python38 py38-pip


Install in terminal
-------------------

* To install

   ::

      python3.8 -m pip install openseespy

      python3.8 -m pip install --user openseespy

* To upgrade

   ::

      python3.8 -m pip install --upgrade openseespy

      python3.8 -m pip install --user --upgrade openseespy

* To import

   ::

      import openseespy.opensees as ops





