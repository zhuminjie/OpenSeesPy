.. include:: sub.txt

===============
 Fiber Section
===============

.. function:: section('Fiber', secTag, '-GJ', GJ)
   :noindex:

   This command allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers, with each fiber containing a UniaxialMaterial, an area and a location (y,z). The dofs for 2D section are ``[P, Mz]``,
   for 3D are ``[P,Mz,My,T]``.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``GJ`` |float|                     linear-elastic torsional stiffness assigned
                                      to the section
   ================================   ===========================================================================

.. function:: section('Fiber', secTag, '-torsion', torsionMatTag)
   :noindex:

   This command allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers, with each fiber containing a UniaxialMaterial, an area and a location (y,z). The dofs for 2D section are ``[P, Mz]``,
   for 3D are ``[P,Mz,My,T]``.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``torsionMatTag`` |int|            uniaxialMaterial tag assigned to the section
                                      for torsional response (can be nonlinear)
   ================================   ===========================================================================

.. note::


   #. The commands below should be called after the section command to generate all the fibers in the section.
   #. The patch and layer commands can be used to generate multiple fibers in a single command.


Commands to generate all fibers:

#. :doc:`fiber`
#. :doc:`patch`
#. :doc:`layer`
      
.. toctree::
   :maxdepth: 2
   :hidden:

   fiber
   patch
   layer
