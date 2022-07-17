.. include:: sub.txt

===========================
 Elastic Uniaxial Material
===========================

.. function:: uniaxialMaterial('Elastic', matTag, E, eta=0.0, Eneg=E)
   :noindex:

   This command is used to construct an elastic uniaxial material object.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``E`` |float|                         tangent
   ``eta`` |float|                       damping tangent (optional, default=0.0)
   ``Eneg`` |float|                      tangent in compression (optional, default=E)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic_Uniaxial_Material>`_
