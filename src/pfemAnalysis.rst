.. include:: sub.txt

.. _PFEM-Analysis:

===============
 PFEM analysis
===============

.. function:: analysis('PFEM',dtmax,dtmin,gravity,ratio=0.5)
   :noindex:

   Create a OpenSees PFEMAnalysis object. 

   ===============================   ======================================================================================
   ``dtmax`` |float|                 Maximum time steps.
   ``dtmin`` |float|                 Mimimum time steps.
   ``gravity`` |float|               Gravity acceleration used to move isolated particles.
   ``ratio`` |float|                 The ratio to reduce time steps if it was not converged. (optional)
   ===============================   ======================================================================================
