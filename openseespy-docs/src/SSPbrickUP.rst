.. include:: sub.txt

==================
SSPbrickUP Element
==================

This command is used to construct a SSPbrickUP element object.

.. function:: element('SSPbrickUP', eleTag,*eleNodes,matTag, fBulk, fDen, k1, k2, k3, void, alpha,<b1, b2, b3>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of eight element nodes in counter-clockwise order
   ``matTag`` |float|                    unique integer tag associated with previously-defined nDMaterial object
   ``fBulk`` |float|                     bulk modulus of the pore fluid
   ``fDen`` |float|                      mass density of the pore fluid
   ``k1``  ``k2``  ``k3`` |float|        permeability coefficients in global x-, y-, and z-directions, respectively
   ``void`` |float|                      voids ratio
   ``alpha`` |float|                     spatial pressure field stabilization parameter (see discussion below for more information)
   ``b1``  ``b2``  ``b3`` |float|        constant body forces in global x-, y-, and z-directions, respectively (optional, default = 0.0) - See Note 3
   ===================================   ===========================================================================

The SSPbrickUP element is an extension of the SSPbrick Element for use in dynamic 3D analysis of fluid saturated porous media. A mixed displacement-pressure (u-p) formulation is used, based upon the work of Biot as extended by Zienkiewicz and Shiomi (1984).

The physical stabilization necessary to allow for reduced integration incorporates an enhanced assumed strain field, resulting in an element which is free from volumetric and shear locking. The elimination of shear locking results in greater coarse mesh accuracy in bending dominated problems, and the elimination of volumetric locking improves accuracy in nearly-incompressible problems. Analysis times are generally faster than corresponding full integration elements.

Equal-order interpolation is used for the displacement and pressure fields, thus, the SSPbrickUP element does not inherently pass the inf-sup condition, and is not fully acceptable in the incompressible-impermeable limit (the brickUP Element has the same issue). A stabilizing parameter is employed to permit the use of equal-order interpolation for the SSPbrickUP element. This parameter $alpha can be computed as

.. math::

   \alpha = h^2/(4*(K_s + (4/3)*G_s))

where :math:`h` is the element size, and :math:`K_s` and :math:`G_s` are the bulk and shear moduli for the solid phase. The :math:`\alpha` parameter should be a small number. With a properly defined :math:`\alpha` parameter, the SSPbrickUP element can produce comparable results to a higher-order element such as the 20_8_BrickUP Element at a significantly lower computational cost and with a greater ease in mesh generation.

.. note::

   #. The SSPbrickUP element will only work in dynamic analysis.
   #. For saturated soils, the mass density input into the associated nDMaterial object should be the saturated mass density.
   #. When modeling soil, the body forces input into the SSPbrickUP element should be the components of the gravitational vector, not the unit weight.
   #. Fixing the pore pressure degree-of-freedom (dof 4) at a node is a drainage boundary condition at which zero pore pressure will be maintained throughout the analysis. Leaving the fourth dof free allows pore pressures to build at that node.
   #. Valid queries to the SSPbrickUP element when creating an ElementalRecorder object correspond to those for the nDMaterial object assigned to the element (e.g., 'stress', 'strain'). Material response is recorded at the single integration point located in the center of the element.
   #. The SSPbrickUP element was designed with intentions of duplicating the functionality of the brickUP Element. If an example is found where the SSPbrickUP element cannot do something that works for the brickUP Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/SSPbrickUP_Element>`_
