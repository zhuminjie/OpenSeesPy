.. include:: sub.txt

==================
 FSAM
==================

.. function:: nDMaterial('FSAM', matTag, rho, sXTag, sYTag, concTag, rouX, rouY, nu, alfadow)
   :noindex:

   This command is used to construct a nDMaterial FSAM (Fixed-Strut-Angle-Model, Figure 1, Kolozvari et al., 2015), which is a plane-stress constitutive model for simulating the behavior of RC panel elements under generalized, in-plane, reversed-cyclic loading conditions (Ulugtekin, 2010; Orakcal et al., 2012). In the FSAM constitutive model, the strain fields acting on concrete and reinforcing steel components of a RC panel are assumed to be equal to each other, implying perfect bond assumption between concrete and reinforcing steel bars. While the reinforcing steel bars develop uniaxial stresses under strains in their longitudinal direction, the behavior of concrete is defined using stress-strain relationships in biaxial directions, the orientation of which is governed by the state of cracking in concrete. Although the concrete stress-strain relationship used in the FSAM is fundamentally uniaxial in nature, it also incorporates biaxial softening effects including compression softening and biaxial damage. For transfer of shear stresses across the cracks, a friction-based elasto-plastic shear aggregate interlock model is adopted, together with a linear elastic model for representing dowel action on the reinforcing steel bars (Kolozvari, 2013). Note that FSAM constitutive model is implemented to be used with Shear-Flexure Interaction model for RC walls (SFI_MVLEM), but it could be also used elsewhere.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``rho`` |float|                    Material density
   ``sXTag`` |int|                    Tag of uniaxialMaterial simulating horizontal (x) reinforcement
   ``sYTag`` |int|                    Tag of uniaxialMaterial simulating vertical (y) reinforcement
   ``concTag`` |int|                  Tag of uniaxialMaterial simulating concrete,
                                      shall be used with uniaxialMaterial ConcreteCM
   ``rouX`` |float|                   Reinforcing ratio in horizontal (x) direction
                                      (:math:`rouX = _{s,x}/A_{gross,x}`)
   ``rouY`` |float|                   Reinforcing ratio in vertical (x) direction
                                      (:math:`rouY = _{s,y}/A_{gross,y}`)
   ``nu`` |float|                     Concrete friction coefficient (:math:`0.0 < \nu < 1.5`)
   ``alfadow`` |float|                Stiffness coefficient of reinforcement dowel action
                                      (:math:`0.0 < alfadow < 0.05`)
   ================================   ===========================================================================

See also `here <http://opensees.berkeley.edu/wiki/index.php/FSAM_-_2D_RC_Panel_Constitutive_Behavior>`_


References:

1) Kolozvari K., Orakcal K., and Wallace J. W. (2015). "Shear-Flexure Interaction Modeling of reinforced Concrete Structural Walls and Columns under Reversed Cyclic Loading", Pacific Earthquake Engineering Research Center, University of California, Berkeley, PEER Report No. 2015/12

2) Kolozvari K. (2013). "Analytical Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural Walls", PhD Dissertation, University of California, Los Angeles.

3) Orakcal K., Massone L.M., and Ulugtekin D. (2012). "Constitutive Modeling of Reinforced Concrete Panel Behavior under Cyclic Loading", Proceedings, 15th World Conference on Earthquake Engineering, Lisbon, Portugal.

4) Ulugtekin D. (2010). "Analytical Modeling of Reinforced Concrete Panel Elements under Reversed Cyclic Loadings", M.S. Thesis, Bogazici University, Istanbul, Turkey.
