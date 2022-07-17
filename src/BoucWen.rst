.. include:: sub.txt

=============================
BoucWen Material
=============================

.. function:: uniaxialMaterial('BoucWen', matTag,alpha, ko, n, gamma, beta, Ao, deltaA, deltaNu, deltaEta)
   :noindex:

   This command is used to construct a uniaxial Bouc-Wen smooth hysteretic material object. This material model is an extension of the original Bouc-Wen model that includes stiffness and strength degradation (Baber and Noori (1985)).



   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``alpha`` |float|                     ratio of post-yield stiffness to the initial elastic stiffenss (0< alpha <1)
   ``ko`` |float|                        initial elastic stiffness
   ``n`` |float|                         parameter that controls transition from linear to nonlinear range (as n increases the transition becomes sharper; n is usually grater or equal to 1)
   ``gamma``    ``beta`` |float|         parameters that control shape of hysteresis loop; depending on the values of gamma and beta softening, hardening or quasi-linearity can be simulated (look at the NOTES)
   ``Ao``    ``deltaA`` |float|          parameters that control tangent stiffness
   ``deltaNu``    ``deltaEta`` |float|   parameters that control material degradation
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/BoucWen_Material>`_
