.. include:: sub.txt

===============================================================
SFI MVLEM - Cyclic Shear-Flexure Interaction Model for RC Walls
===============================================================

The SFI_MVLEM command is used to construct a Shear-Flexure Interaction Multiple-Vertical-Line-Element Model (SFI-MVLEM, Kolozvari et al., 2015a, b, c), which captures interaction between axial/flexural and shear behavior of RC structural walls and columns under cyclic loading. The SFI_MVLEM element (Figure 1) incorporates 2-D RC panel behavior described by the Fixed-Strut-Angle-Model (nDMaterial FSAM; Ulugtekin, 2010; Orakcal et al., 2012), into a 2-D macroscopic fiber-based model (MVLEM). The interaction between axial and shear behavior is captured at each RC panel (macro-fiber) level, which further incorporates interaction between shear and flexural behavior at the SFI_MVLEM element level.


.. function:: element('SFI_MVLEM', eleTag,*eleNodes,m,c, '-thick',*thick,'-width',*widths,'-mat',*mat_tags)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``m`` |int|                           Number of element macro-fibers
   ``c`` |float|                         Location of center of rotation with from the iNode, ``c`` = 0.4 (recommended)
   ``Thicknesses`` |listf|               a list of m macro-fiber thicknesses
   ``Widths`` |listf|                    a list of m macro-fiber widths
   ``Material_tags`` |listi|             a list of m macro-fiber nDMaterial1 tags
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/SFI_MVLEM_-_Cyclic_Shear-Flexure_Interaction_Model_for_RC_Walls>`_
