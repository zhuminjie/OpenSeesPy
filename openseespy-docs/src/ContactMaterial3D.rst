.. include:: sub.txt

=========================
 ContactMaterial3D
=========================

.. function:: nDMaterial('ContactMaterial3D', matTag, mu, G, c, t)
   :noindex:

   This command is used to construct a ContactMaterial3D nDMaterial object.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``mu`` |float|                     interface frictional coefficient
   ``G`` |float|                      interface stiffness parameter
   ``c`` |float|                      interface cohesive intercept
   ``t`` |float|                      interface tensile strength
   ================================   ===========================================================================



The ContactMaterial3D nDMaterial defines the constitutive behavior of a frictional interface between two bodies in contact. The interface defined by this material object allows for sticking, frictional slip, and separation between the two bodies in a three-dimensional analysis. A regularized Coulomb frictional law is assumed. Information on the theory behind this material can be found in, e.g. Wriggers (2002).

.. note::

   #. The ContactMaterial3D nDMaterial has been written to work with the SimpleContact3D and BeamContact3D element objects.
   #. There are no valid recorder queries for this material other than those which are listed with those elements.


References:

Wriggers, P. (2002). Computational Contact Mechanics. John Wilely & Sons, Ltd, West Sussex, England.
