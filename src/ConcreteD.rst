.. include:: sub.txt

==================
 ConcreteD
==================

.. function:: uniaxialMaterial('ConcreteD', matTag, fc, epsc, ft, epst, Ec, alphac, alphat, cesp=0.25,etap=1.15)
   :noindex:

   This command is used to construct a concrete material based on the Chinese design code.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fc`` |float|                        concrete compressive strength
   ``epsc`` |float|                      concrete strain at corresponding to compressive strength
   ``ft`` |float|                        concrete tensile strength
   ``epst`` |float|                      concrete strain at corresponding to tensile strength
   ``Ec`` |float|                        concrete initial Elastic modulus
   ``alphac`` |float|                    compressive descending parameter
   ``alphat`` |float|                    tensile descending parameter
   ``cesp`` |float|                      plastic parameter, recommended values: 0.2~0.3
   ``etap`` |float|                      plastic parameter, recommended values: 1.0~1.3
   ===================================   ===========================================================================

.. note::

   #. Concrete compressive strength and the corresponding strain should be input as negative values.
   #. The value ``fc/epsc`` and ``ft/epst`` should be smaller than ``Ec``.


.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ConcreteD>`_
