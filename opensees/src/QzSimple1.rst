.. include:: sub.txt

==================
QzSimple1 Material
==================

.. function:: uniaxialMaterial('QzSimple1', matTag,qzType, qult, Z50, suction=0.0, c=0.0)
   :noindex:

   This command is used to construct a QzSimple1 uniaxial material object.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``qzType`` |int|                      qzType = 1 Backbone of q-z curve approximates Reese and O'Neill's (1987) relation for drilled shafts in clay.

                                         qzType = 2 Backbone of q-z curve approximates Vijayvergiya's (1977) relation for piles in sand.
   ``qult`` |float|                      Ultimate capacity of the q-z material. SEE NOTE 1.
   ``Z50`` |float|                       Displacement at which 50% of qult is mobilized in monotonic loading. SEE NOTE 2.
   ``suction`` |float|                   Uplift resistance is equal to suction*qult. Default = 0.0. The value of suction must be 0.0 to 0.1.*
   ``c`` |float|                         The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). Default = 0.0. Nonzero c values are used to represent radiation damping effects.*
   ===================================   ===========================================================================

.. note::

   #. ``qult``: Ultimate capacity of the q-z material. Note that ``q1`` or ``qult`` are stresses [force per unit area of pile tip] in common design equations, but are both loads for this uniaxialMaterial [i.e., stress times tip area].
   #. ``Y50``: Displacement at which 50% of pult is mobilized in monotonic loading. Note that Vijayvergiya's relation (qzType=2) refers to a "critical" displacement (zcrit) at which qult is fully mobilized, and that the corresponding z50 would be 0. 125zcrit.
   #. optional args    ``suction`` and    ``c`` must either both be omitted or both provided.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/QzSimple1_Material>`_
