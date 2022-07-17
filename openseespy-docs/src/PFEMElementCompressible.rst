.. include:: sub.txt

=========================
 PFEMElementCompressible
=========================

.. function:: element('PFEMElementCompressible',eleTag,*eleNodes,rho,mu,b1,b2, <thickness,kappa>)
   :noindex:

   Create a PFEM compressible element, which is a fluid element for FSI analysis.

   ========================   =============================================================
   ``eleTag`` |int|           tag of the element
   ``eleNodes`` |listi|         A list of four element nodes, last one is middle node
   ``rho`` |float|            fluid density
   ``mu`` |float|             fluid viscosity
   ``b1`` |float|             body body acceleration in x direction
   ``b2`` |float|             body body acceleration in y direction
   ``thickness`` |float|      element thickness (optional)
   ``kappa`` |float|          fluid bulk modulus (optional)
   ========================   =============================================================

