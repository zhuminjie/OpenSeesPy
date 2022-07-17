=======================
 Compilation for MacOS
=======================

This is a suggestive guide for MacOS.

* Download OpenSees Source code

   ::

      git clone https://github.com/OpenSees/OpenSees.git

* Install `MacPorts <https://www.macports.org/install.php>`_ for your macOs.

* Install `gcc8 <https://ports.macports.org/port/gcc8>`_

  ::
     
     sudo port install gcc8


* Install Python 3.8 using MacPorts

  ::

     sudo port install python38 python38-devel


* Install boost using Macports

  ::

     sudo port install boost

* Create Makefile.def

  * Copy one of ``MAKES/Makefile.def.MacOS10.x`` to the root and rename to ``Makefile.def``
  * Change the path and variables for your system

* Compile

  * Run ``make python -j`` from root
  * The library file will be at ``SRC/interpreter/opensees.so``
