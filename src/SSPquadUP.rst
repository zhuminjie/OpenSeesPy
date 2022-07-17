.. include:: sub.txt

=================
SSPquadUP Element
=================

This command is used to construct a SSPquadUP element object.


.. function:: element('SSPquadUP', eleTag,*eleNodes,matTag, thick, fBulk, fDen, k1, k2, void, alpha,<b1=0.0, b2=0.0>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order
   ``matTag`` |int|                      unique integer tag associated with previously-defined nDMaterial object
   ``thick`` |float|                     thickness of the element in out-of-plane direction
   ``fBulk`` |float|                     bulk modulus of the pore fluid
   ``fDen`` |float|                      mass density of the pore fluid
   ``k1`` ``k2`` |float|                 permeability coefficients in global x- and y-directions, respectively
   ``void`` |float|                      voids ratio
   ``alpha`` |float|                     spatial pressure field stabilization parameter (see discussion below for more information)
   ``b1``  ``b2`` |float|                constant body forces in global x- and y-directions, respectively (optional, default = 0.0) - See Note 3
   ===================================   ===========================================================================

      The SSPquadUP element is an extension of the SSPquad Element for use in dynamic plane strain analysis of fluid saturated porous media. A mixed displacement-pressure (u-p) formulation is used, based upon the work of Biot as extended by Zienkiewicz and Shiomi (1984).

The physical stabilization necessary to allow for reduced integration incorporates an assumed strain field in which the volumetric dilation and the shear strain associated with the the hourglass modes are zero, resulting in an element which is free from volumetric and shear locking. The elimination of shear locking results in greater coarse mesh accuracy in bending dominated problems, and the elimination of volumetric locking improves accuracy in nearly-incompressible problems. Analysis times are generally faster than corresponding full integration elements.

Equal-order interpolation is used for the displacement and pressure fields, thus, the SSPquadUP element does not inherently pass the inf-sup condition, and is not fully acceptable in the incompressible-impermeable limit (the QuadUP Element has the same issue). A stabilizing parameter is employed to permit the use of equal-order interpolation for the SSPquadUP element. This parameter $alpha can be computed as

.. math::
   \alpha = 0.25*(h^2)/(den*c^2)

where h is the element size, c is the speed of elastic wave propagation in the solid phase, and den is the mass density of the solid phase. The $alpha parameter should be a small number. With a properly defined $alpha parameter, the SSPquadUP element can produce comparable results to a higher-order element such as the 9_4_QuadUP Element at a significantly lower computational cost and with a greater ease in mesh generation.

The full formulation for the SSPquadUP element can be found in McGann et al. (2012) along with several example applications.

.. note::

   #. The SSPquadUP element will only work in dynamic analysis.
   #. For saturated soils, the mass density input into the associated nDMaterial object should be the saturated mass density.
   #. When modeling soil, the body forces input into the SSPquadUP element should be the components of the gravitational vector, not the unit weight.
   #. Fixing the pore pressure degree-of-freedom (dof 3) at a node is a drainage boundary condition at which zero pore pressure will be maintained throughout the analysis. Leaving the third dof free allows pore pressures to build at that node.
   #. Valid queries to the SSPquadUP element when creating an ElementalRecorder object correspond to those for the nDMaterial object assigned to the element (e.g., 'stress', 'strain'). Material response is recorded at the single integration point located in the center of the element.
   #. The SSPquadUP element was designed with intentions of duplicating the functionality of the QuadUP Element. If an example is found where the SSPquadUP element cannot do something that works for the QuadUP Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/SSPquadUP_Element>`_
