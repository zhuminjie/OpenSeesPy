.. include:: sub.txt

==================
PySimple1 Material
==================

.. function:: uniaxialMaterial('PySimple1', matTag, soilType, pult, Y50, Cd, c=0.0)
   :noindex:

   This command is used to construct a PySimple1 uniaxial material object.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``soilType`` |int|                    soilType = 1 Backbone of p-y curve approximates Matlock (1970) soft clay relation.

                                         soilType = 2 Backbone of p-y curve approximates API (1993) sand relation.
   ``pult`` |float|                      Ultimate capacity of the p-y material. Note that "p" or "pult" are distributed loads [force per length of pile] in common design equations, but are both loads for this uniaxialMaterial [i.e., distributed load times the tributary length of the pile].
   ``Y50`` |float|                       Displacement at which 50% of pult is mobilized in monotonic loading.
   ``Cd`` |float|                        Variable that sets the drag resistance within a fully-mobilized gap as Cd*pult.
   ``c`` |float|                         The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). (optional Default = 0.0). Nonzero c values are used to represent radiation damping effects
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/PySimple1_Material>`_
