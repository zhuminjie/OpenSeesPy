.. include:: sub.txt

==================
 Concrete04
==================

.. function:: uniaxialMaterial('Concrete04', matTag, fc, epsc, epscu, Ec, fct, et, beta)
   :noindex:

   This command is used to construct a uniaxial Popovics concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and tensile strength with exponential decay.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fc`` |float|                        floating point values defining concrete
                                         compressive strength at 28 days (compression is negative)
   ``epsc`` |float|                        floating point values defining concrete strain at maximum strength
   ``epscu`` |float|                       floating point values defining concrete strain at crushing strength
   ``Ec`` |float|                        floating point values defining initial stiffness
   ``fct`` |float|                       floating point value defining the maximum tensile strength of concrete (optional)
   ``et`` |float|                        floating point value defining ultimate tensile strain of concrete (optional)
   ``beta`` |float|                      loating point value defining the exponential curve parameter to define the residual
                                         stress (as a factor of ft) at etu
   ===================================   ===========================================================================

.. note::

   #. Compressive concrete parameters should be input as negative values.
   #. The envelope of the compressive stress-strain response is defined using the model proposed by Popovics (1973). If the user defines :math:`Ec = 57000*sqrt(|fcc|)` (in psi)' then the envelope curve is identical to proposed by Mander et al. (1988).
   #. Model Characteristic: For loading in compression, the envelope to the stress-strain curve follows the model proposed by Popovics (1973) until the concrete crushing strength is achieved and also for strains beyond that corresponding to the crushing strength. For unloading and reloading in compression, the Karsan-Jirsa model (1969) is used to determine the slope of the curve. For tensile loading, an exponential curve is used to define the envelope to the stress-strain curve. For unloading and reloading in tensile, the secant stiffness is used to define the path.


.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete04_Material_--_Popovics_Concrete_Material>`_
