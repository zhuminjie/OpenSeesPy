.. include:: sub.txt

=======================
 Fiber Thermal Section
=======================

.. function:: section('FiberThermal', secTag, '-GJ', GJ=0.0)
   :noindex:

   This command create a FiberSectionThermal object.
   The dofs for 2D section are ``[P, Mz]``,
   for 3D are ``[P,Mz,My]``.


.. note::


   #. The commands below should be called after the section command to generate all the fibers in the section.
   #. The patch and layer commands can be used to generate multiple fibers in a single command.

Commands to generate all fibers:

#. :doc:`fiber`
#. :doc:`patch`
#. :doc:`layer`