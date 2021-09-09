.. include:: sub.txt

===============================================================
SFI MVLEM - Cyclic Shear-Flexure Interaction Model for RC Walls
===============================================================

| Developed and implemented by: 
| `Kristijan Kolozvari <mailto:kkolozvari@fullerton.edu>`_ (CSU Fullerton)
| Kutay Orakcal (Bogazici University)
| Leonardo Massone (University of Chile, Santiago)
| John Wallace (UCLA)

The SFI_MVLEM command is used to construct a Shear-Flexure Interaction Multiple-Vertical-Line-Element Model (SFI-MVLEM, Kolozvari et al., 2018, 2015a, b, c; Kolozvari 2013), which captures interaction between axial/flexural and shear behavior of RC structural walls and columns under cyclic loading. The SFI_MVLEM element (Figure 1) incorporates 2-D RC panel behavior described by the Fixed-Strut-Angle-Model (nDMaterial FSAM; Ulugtekin, 2010; Orakcal et al., 2012), into a 2-D macroscopic fiber-based model (MVLEM). The interaction between axial and shear behavior is captured at each RC panel (macro-fiber) level, which further incorporates interaction between shear and flexural behavior at the SFI_MVLEM element level.


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
   
	Kolozvari K., Orakcal K., and Wallace J. W. (2015a). "New opensees models for simulating nonlinear flexural and coupled shear-flexural behavior of RC walls and columns", Computers and Structures, Volume 196, February 2018, Pages 246-262, `doi <https://doi.org/10.1016/j.compstruc.2017.10.010>`_

	Kolozvari K., Orakcal K., and Wallace J. W. (2015a). ”Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural Walls. I: Theory”, ASCE Journal of Structural Engineering, 141(5), 04014135 `doi <https://ascelibrary.org/doi/10.1061/%28ASCE%29ST.1943-541X.0001059>`_

	Kolozvari K., Tran T., Orakcal K., and Wallace, J.W. (2015c). ”Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural Walls. II: Experimental Validation”, ASCE Journal of Structural Engineering, 141(5), 04014136 `doi <https://ascelibrary.org/doi/10.1061/%28ASCE%29ST.1943-541X.0001083>`_

	Kolozvari K., Orakcal K., and Wallace J. W. (2015c). "Shear-Flexure Interaction Modeling of reinforced Concrete Structural Walls and Columns under Reversed Cyclic Loading", Pacific Earthquake Engineering Research Center, University of California, Berkeley, PEER Report No. 2015/12

	Kolozvari K. (2013). “Analytical Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural Walls”, PhD Dissertation, University of California, Los Angeles.