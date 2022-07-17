.. include:: sub.txt

====================
BbarQuad u-p Element
====================

bbarQuadUP is a four-node plane-strain mixed volume/pressure element, which uses a tri-linear isoparametric formulation. This element is implemented for simulating dynamic response of solid-fluid fully coupled material, based on Biot's theory of porous medium. Each element node has 3 degrees-of-freedom (DOF): DOF 1 and 2 for solid displacement (u) and DOF 3 for fluid pressure (p).



.. function:: element('bbarQuadUP', eleTag,*eleNodes,thick, matTag, bulk, fmass, hPerm, vPerm,<b1=0, b2=0, t=0>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order
   ``thick`` |float|                     Element thickness
   ``matTag`` |int|                      Tag of an NDMaterial object (previously defined) of which the element is composed
   ``bulk`` |float|                      Combined undrained bulk modulus Bc relating changes in pore pressure and volumetric strain, may be approximated by: :math:`B_c \approx B_f/n`

                                         where :math:`B_f` is the bulk modulus of fluid phase (:math:`2.2\times 10^6` kPa (or :math:`3.191\times 10^5` psi) for water), and n the initial porosity.
   ``fmass`` |float|                     Fluid mass density
   ``hPerm``, ``vPerm`` |float|          Permeability coefficient in horizontal and vertical directions respectively.
   ``b1``,  ``b2`` |float|               Optional gravity acceleration components in horizontal and vertical directions respectively (defaults are 0.0)
   ``t`` |float|                         Optional uniform element normal traction, positive in tension (default is 0.0)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/BbarQuad_u-p_Element>`_
