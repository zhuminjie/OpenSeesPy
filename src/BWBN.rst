.. include:: sub.txt

=============
BWBN Material
=============

.. function:: uniaxialMaterial('BWBN', matTag,alpha, ko, n, gamma, beta, Ao, q, zetas, p, Shi, deltaShi, lambda, tol, maxIter)
   :noindex:

   This command is used to construct a uniaxial Bouc-Wen pinching hysteretic material object. This material model is an extension of the original Bouc-Wen model that includes pinching (Baber and Noori (1986) and Foliente (1995)).



   =============================================================================   ===========================================================================
   ``matTag`` |int|                                                                integer tag identifying material
   ``alpha`` |float|                                                               ratio of post-yield stiffness to the initial elastic stiffenss (0< alpha <1)
   ``ko`` |float|                                                                  initial elastic stiffness
   ``n`` |float|                                                                   parameter that controls transition from linear to nonlinear range (as n increases the transition becomes sharper; n is usually grater or equal to 1)
   ``gamma``    ``beta`` |float|                                                   parameters that control shape of hysteresis loop; depending on the values of gamma and beta softening, hardening or quasi-linearity can be simulated (look at the BoucWen Material)
   ``Ao`` |float|                                                                  parameter that controls tangent stiffness
   ``q``  ``zetas``  ``p``  ``Shi``  ``deltaShi``  ``lambda`` |float|              parameters that control pinching
   ``tol`` |float|                                                                 tolerance
   ``maxIter`` |float|                                                             maximum iterations
   =============================================================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/BWBN_Material>`_
