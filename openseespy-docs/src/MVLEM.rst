.. include:: sub.txt

=========================================================
MVLEM - Multiple-Vertical-Line-Element-Model for RC Walls
=========================================================

| Developed and implemented by: 
| `Kristijan Kolozvari <mailto:kkolozvari@fullerton.edu>`_ (CSU Fullerton)
| Kutay Orakcal (Bogazici University)
| John Wallace (UCLA)

The MVLEM element command is used to generate a two-dimensional Multiple-Vertical-Line-Element-Model (MVLEM; Vulcano et al., 1988; Orakcal et al., 2004, Kolozvari et al., 2015) for simulation of flexure-dominated RC wall behavior. A single model element incorporates six global degrees of freedom, three of each located at the center of rigid top and bottom beams, as illustrated in Figure 1a. The axial/flexural response of the MVLEM is simulated by a series of uniaxial elements (or macro-fibers) connected to the rigid beams at the top and bottom (e.g., floor) levels, whereas the shear response is described by a shear spring located at height ch from the bottom of the wall element (Figure 1a). Shear and flexural responses of the model element are uncoupled. The relative rotation between top and bottom faces of the wall element occurs about the point located on the central axis of the element at height ch (Figure 1b). Rotations and resulting transverse displacements are calculated based on the wall curvature, derived from section and material properties, corresponding to the bending moment at height ch of each element (Figure 1b). A value of c=0.4 was recommended by Vulcano et al. (1988) based on comparison of the model response with experimental results.

.. function:: element('MVLEM', eleTag,Dens,*eleNodes,m, c, '-thick', *thick,'-width',*widths,'-rho',*rho,'-matConcrete',*matConcreteTags,'-matSteel',*matSteelTags,'-matShear',matShearTag)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``Dens`` |float|                      Wall density
   ``eleNodes`` |listi|                  a list of two element nodes
   ``m`` |int|                           Number of element macro-fibers
   ``c`` |float|                         Location of center of rotation from the iNode, ``c`` = 0.4 (recommended)
   ``thick`` |listf|                     a list of ``m`` macro-fiber thicknesses
   ``widths`` |listf|                    a list of ``m`` macro-fiber widths
   ``rho`` |listf|                       a list of m reinforcing ratios corresponding to macro-fibers; for each fiber: :math:`rho_i = A_{s,i}/A_{gross,i} (1 < i < m)`
   ``matConcreteTags`` |listi|           a list of ``m`` uniaxialMaterial tags for concrete
   ``matSteelTags`` |listi|              a list of ``m`` uniaxialMaterial tags for steel
   ``matShearTag`` |int|                 Tag of uniaxialMaterial for shear material
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/MVLEM_-_Multiple-Vertical-Line-Element-Model_for_RC_Walls>`_
   
	Kolozvari K., Orakcal K., and Wallace J. W. (2015a). "New opensees models for simulating nonlinear flexural and coupled shear-flexural behavior of RC walls and columns", Computers and Structures, Volume 196, February 2018, Pages 246-262, `doi <https://doi.org/10.1016/j.compstruc.2017.10.010>`_

