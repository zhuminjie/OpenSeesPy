.. include:: sub.txt

==================
 Concrete07
==================

.. function:: uniaxialMaterial('Concrete07', matTag, fc, epsc, Ec, ft, et, xp, xn, r)
   :noindex:

   Concrete07 is an implementation of Chang & Mander's 1994 concrete model with simplified unloading and reloading curves. Additionally the tension envelope shift with respect to the origin proposed by Chang and Mander has been removed. The model requires eight input parameters to define the monotonic envelope of confined and unconfined concrete in the following form:

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fc`` |float|                        concrete compressive strength (compression is negative)
   ``epsc`` |float|                        concrete strain at maximum compressive strength
   ``Ec`` |float|                        Initial Elastic modulus of the concrete
   ``ft`` |float|                        tensile strength of concrete (tension is positive)
   ``et`` |float|                        tensile strain at max tensile strength of concrete
   ``xp`` |float|                        Non-dimensional term that defines the strain at
                                         which the straight line descent begins in tension
   ``xn`` |float|                        Non-dimensional term that defines the strain at
                                         which the straight line descent begins in compression
   ``r`` |float|                         Parameter that controls the nonlinear descending branch
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete07_%E2%80%93_Chang_%26_Mander%E2%80%99s_1994_Concrete_Model>`_
