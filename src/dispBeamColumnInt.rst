.. include:: sub.txt

================================================================
Flexure-Shear Interaction Displacement-Based Beam-Column Element
================================================================

This command is used to construct a dispBeamColumnInt element object, which is a distributed-plasticity, displacement-based beam-column element which includes interaction between flexural and shear components.



.. function:: element('dispBeamColumnInt', eleTag,*eleNodes,numIntgrPts, secTag, transfTag, cRot, <'-mass', massDens>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``numIntgrPts`` |int|                 number of integration points along the element.
   ``secTag`` |int|                      identifier for previously-defined section object
   ``transfTag`` |int|                   identifier for previously-defined coordinate-transformation (CrdTransf) object
   ``cRot`` |float|                      identifier for element center of rotation (or center of curvature distribution). Fraction of the height distance from bottom to the center of rotation (0 to 1)
   ``massDens`` |float|                  element mass density (per unit length), from which a lumped-mass matrix is formed (optional, default=0.0)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Flexure-Shear_Interaction_Displacement-Based_Beam-Column_Element>`_
