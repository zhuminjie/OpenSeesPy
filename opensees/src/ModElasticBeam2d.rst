.. include:: sub.txt

====================================================
Elastic Beam Column Element with Stiffness Modifiers
====================================================

This command is used to construct a ModElasticBeam2d element object. The arguments for the construction of an elastic beam-column element with stiffness modifiers is applicable for 2-D problems. This element should be used for modelling of a structural element with an equivalent combination of one elastic element with stiffness-proportional damping, and two springs at its two ends with no stiffness proportional damping to represent a prismatic section. The modelling technique is based on a number of analytical studies discussed in Zareian and Medina (2010) and Zareian and Krawinkler (2009) and is utilized in order to solve problems related to numerical damping in dynamic analysis of frame structures with concentrated plasticity springs.

.. function:: element('ModElasticBeam2d', eleTag,*eleNodes,Area, E_mod, Iz, K11, K33, K44, transfTag,<'-mass',massDens>,<'-cMass'>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``Area`` |float|                         cross-sectional area of element
   ``E_mod`` |float|                         Young's Modulus
   ``Iz`` |float|                        second moment of area about the local z-axis
   ``K11`` |float|                       stiffness modifier for translation
   ``K33`` |float|                       stiffness modifier for translation
   ``K44`` |float|                       stiffness modifier for rotation
   ``transfTag`` |int|                   identifier for previously-defined coordinate-transformation (CrdTransf) object
   ``massDens`` |float|                  element mass per unit length (optional, default = 0.0)
   ``'-cMass'`` |str|                    to form consistent mass matrix (optional, default = lumped mass matrix)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic_Beam_Column_Element_with_Stiffness_Modifiers>`_
