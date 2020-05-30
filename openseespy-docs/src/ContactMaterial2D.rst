.. include:: sub.txt

=========================
 ContactMaterial2D
=========================

.. function:: nDMaterial('ContactMaterial2D', matTag, mu, G, c, t)
   :noindex:

   This command is used to construct a ContactMaterial2D nDMaterial object.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``mu`` |float|                     interface frictional coefficient
   ``G`` |float|                      interface stiffness parameter
   ``c`` |float|                      interface cohesive intercept
   ``t`` |float|                      interface tensile strength
   ================================   ===========================================================================


The ContactMaterial2D nDMaterial defines the constitutive behavior of a frictional interface between two bodies in contact. The interface defined by this material object allows for sticking, frictional slip, and separation between the two bodies in a two-dimensional analysis. A regularized Coulomb frictional law is assumed. Information on the theory behind this material can be found in, e.g. Wriggers (2002).

.. note::

   #. The ContactMaterial2D nDMaterial has been written to work with the SimpleContact2D and BeamContact2D element objects.
   #. There are no valid recorder queries for this material other than those which are listed with those elements


References:

Wriggers, P. (2002). Computational Contact Mechanics. John Wilely & Sons, Ltd, West Sussex, England.
