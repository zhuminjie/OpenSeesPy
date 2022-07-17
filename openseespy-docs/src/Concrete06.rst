.. include:: sub.txt

==================
 Concrete06
==================

.. function:: uniaxialMaterial('Concrete06', matTag, fc, e0, n, k, alpha1, fcr, ecr, b, alpha2)
   :noindex:

   This command is used to construct a uniaxial concrete material object with tensile strength, nonlinear tension stiffening and compressive behavior based on Thorenfeldt curve.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fc`` |float|                        concrete compressive strength (compression is negative)
   ``e0`` |float|                        strain  at compressive strength
   ``n`` |float|                         compressive shape factor
   ``k`` |float|                         post-peak compressive shape factor
   ``alpha1`` |float|                    :math:`\alpha_1` parameter for compressive plastic strain definition
   ``fcr`` |float|                       tensile strength
   ``ecr`` |float|                       tensile strain at peak stress (fcr)
   ``b`` |float|                         exponent of the tension stiffening curve
   ``alpha2`` |float|                    :math:`\alpha_2` parameter for tensile plastic strain definition
   ===================================   ===========================================================================

.. note::

   #. Compressive concrete parameters should be input as negative values.


.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete06_Material>`_
