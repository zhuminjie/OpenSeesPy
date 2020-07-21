.. include:: sub.txt

.. _PFEMElementBubble:
   
===================
 PFEMElementBubble
===================

.. function:: element('PFEMElementBubble',eleTag,*eleNodes, rho,mu,b1,b2,<b3>,<thickness,kappa>)
   :noindex:

   Create a PFEM Bubble element, which is a fluid element for FSI analysis.

   ========================   =============================================================
   ``eleTag`` |int|           tag of the element
   ``eleNodes`` |listi|         A list of three or four element nodes, four are required for 3D
   ``nd4`` |int|              tag of node 4 (required for 3D)
   ``rho`` |float|            fluid density
   ``mu`` |float|             fluid viscosity
   ``b1`` |float|             body body acceleration in x direction
   ``b2`` |float|             body body acceleration in y direction
   ``b3`` |float|             body body acceleration in z direction (required for 3D)
   ``thickness`` |float|      element thickness (required for 2D)
   ``kappa`` |float|          fluid bulk modulus (optional)
   ========================   =============================================================

