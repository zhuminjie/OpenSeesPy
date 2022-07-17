.. include:: sub.txt

====================
 Arc-Length Control
====================

.. function:: integrator('ArcLength',s,alpha)
   :noindex:

   Create a ArcLength integrator. In an analysis step with ArcLength we seek to determine the time step that will result in our constraint equation being satisfied.

   ========================   ================================================================
   ``s`` |float|              The arcLength.
   ``alpha`` |float|          :math:`\alpha` a scaling factor on the reference loads.
   ========================   ================================================================
