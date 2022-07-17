.. include:: sub.txt

=============================
Viscous Material
=============================

.. function:: uniaxialMaterial('Viscous', matTag, C, alpha)
   :noindex:

   This command is used to construct a uniaxial viscous material object. stress =C(strain-rate)^alpha

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``C`` |float|                         damping coeficient
   ``alpha`` |float|                     power factor (=1 means linear damping)
   ===================================   ===========================================================================

.. note::

   1. This material can only be assigned to truss and zeroLength elements.

   2. This material can not be combined in parallel/series with other materials. When defined in parallel with other materials it is ignored.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Viscous_Material>`_
