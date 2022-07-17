.. include:: sub.txt

===================================
Twenty Eight Node Brick u-p Element
===================================

Twenty_Eight_Node_BrickUP is a 20-node hexahedral isoparametric element.

The eight corner nodes have 4 degrees-of-freedom (DOF) each: DOFs 1 to 3 for solid displacement (u) and DOF 4 for fluid pressure (p). The other nodes have 3 DOFs each for solid displacement. This element is implemented for simulating dynamic response of solid-fluid fully coupled material, based on Biot's theory of porous medium.

.. function:: element('20_8_BrickUP', eleTag,*eleNodes,matTag, bulk, fmass, permX, permY, permZ,<bX=0, bY=0, bZ=0>)
   :noindex:

   ==========================================   ===========================================================================
   ``eleTag`` |int|                             unique element object tag
   ``eleNodes`` |listi|                         a list of twenty element nodes
   ``matTag`` |int|                             Tag of an NDMaterial object (previously defined) of which the element is composed
   ``bulk`` |float|                             Combined undrained bulk modulus Bc relating changes in pore pressure and volumetric strain, may be approximated by: :math:`B_c \approx B_f/n`

                                                where :math:`B_f` is the bulk modulus of fluid phase (:math:`2.2\times 10^6` kPa (or :math:`3.191\times 10^5` psi) for water), and n the initial porosity.
   ``fmass`` |float|                            Fluid mass density
   ``permX``, ``permY``, ``permZ`` |float|      Permeability coefficients in x, y, and z directions respectively.
   ``bX``, ``bY``, ``bZ`` |float|               Optional gravity acceleration components in x, y, and z directions directions respectively (defaults are 0.0)
   ==========================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Twenty_Eight_Node_Brick_u-p_Element>`_
