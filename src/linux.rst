.. include:: sub.txt

.. _linux-install-settings:

=======================================
 OpenSeesPy |opspy_version| for Linux:
=======================================

* Install libgfortran3, libtcl8.5, libtk8.5

* Install `Anaconda 2018.12 Linux`_
   
* Download `OpenSeesPy Linux Library`_


Two files, ``opensees.so`` and ``LICENSE.rst``, are included in the zip file.
Put the library file ``opensees.so`` in a directory, which path should be copied
to

::

   sys.path.append('/path/to/OpenSeesPy')

Alternatively, you can set ``PYTHONPATH`` environment variable in
``.bash_profile`` or ``.bashrc``, for example:

::

   export PYTHONPATH="$PYTHONPATH:$HOME/OpenSeesPy"

and then you can remove or comment the ``sys.path.append`` line from your
Opensees files.
