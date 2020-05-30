.. include:: sub.txt

==================
TzSimple1 Material
==================

.. function:: uniaxialMaterial('TzSimple1', matTag, soilType, tult, z50, c=0.0)
   :noindex:

   This command is used to construct a TzSimple1 uniaxial material object.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``soilType`` |int|                    soilType = 1 Backbone of t-z curve approximates Reese and O'Neill (1987).

                                         soilType = 2 Backbone of t-z curve approximates Mosher (1984) relation.
   ``tult`` |float|                      Ultimate capacity of the t-z material. SEE NOTE 1.
   ``z50`` |float|                       Displacement at which 50% of tult is mobilized in monotonic loading.
   ``c`` |float|                         The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). (optional Default = 0.0). See NOTE 2.
   ===================================   ===========================================================================

.. note::
   #. The argument tult is the ultimate capacity of the t-z material. Note that "t" or "tult" are shear stresses [force per unit area of pile surface] in common design equations, but are both loads for this uniaxialMaterial [i.e., shear stress times the tributary area of the pile].

   #. Nonzero c values are used to represent radiation damping effects

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/TzSimple1_Material>`_
