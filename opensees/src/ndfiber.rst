.. include:: sub.txt

=================
 NDFiber Section
=================

.. function:: section('NDFiber', secTag)
   :noindex:

   This command allows the user to construct an NDFiberSection object. Each NDFiberSection object is composed of NDFibers, with each fiber containing an NDMaterial, an area, and a location (y,z). The NDFiberSection works for 2D and 3D frame elements and it queries the NDMaterial of each fiber for its axial and shear stresses. In 2D, stress components 11 and 12 are obtained from each fiber in order to provide stress resultants for axial force, bending moment, and shear ``[P, Mz, Vy]``. Stress components 11, 12, and 13 lead to all six stress resultants in 3D ``[P, Mz, Vy, My, Vz, T]``.

   The NDFiberSection works with any NDMaterial via wrapper classes that perform static condensation of the stress vector down to the 11, 12, and 13 components, or via specific NDMaterial subclasses that implement the appropriate fiber stress conditions.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ================================   ===========================================================================

.. note::


   #. The commands below should be called after the section command to generate all the fibers in the section.
   #. The patch and layer commands can be used to generate multiple fibers in a single command.

#. :func:`fiber`
#. :func:`patch`
#. :func:`layer`
