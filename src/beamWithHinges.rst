.. include:: sub.txt

========================
Beam With Hinges Element
========================

This command is used to construct a :ref:`forceBeamColumn-Element` element object, which is based on the non-iterative (or iterative) flexibility formulation. The locations and weights of the element integration points are based on so-called plastic hinge integration, which allows the user to specify plastic hinge lenghts at the element ends. Two-point Gauss integration is used on the element interior while two-point Gauss-Radau integration is applied over lengths of 4LpI and 4LpJ at the element ends, viz. "modified Gauss-Radau plastic hinge integration". A total of six integration points are used in the element state determination (two for each hinge and two for the interior).

Users may be familiar with the beamWithHinges command format (see below); however, the format shown here allows for the simple but important case of using a material nonlinear section model on the element interior. The previous beamWithHinges command constrained the user to an elastic interior, which often led to unconservative estimates of the element resisting force when plasticity spread beyond the plastic hinge regions in to the element interior.

The advantages of this new format over the previous beamWithHinges command are

* Plasticity can spread beyond the plastic hinge regions
* Hinges can form on the element interior, e.g., due to distributed member loads

To create a beam element with hinges, one has to
use a :ref:`forceBeamColumn-Element` element with following :func:`beamIntegration`.

.. note::

   * ``'HingeRadau'`` -- two-point Gauss-Radau applied to the hinge regions over 4LpI and 4LpJ (six element integration points)
   * ``'HingeRadauTwo'`` -- two-point Gauss-Radau in the hinge regions applied over LpI and LpJ (six element integration points)
   * ``'HingeMidpoint'`` -- midpoint integration over the hinge regions (four element integration points)
   * ``'HingeEndpoint'`` -- endpoint integration over the hinge regions (four element integration points)

.. seealso::


   For more information on the behavior, advantages, and disadvantages of these approaches to plastic hinge integration, see

   Scott, M.H. and G.L. Fenves. "Plastic Hinge Integration Methods for Force-Based Beam-Column Elements", Journal of Structural Engineering, 132(2):244-252, February 2006.

   Scott, M.H. and K.L. Ryan. "Moment-Rotation Behavior of Force-Based Plastic Hinge Elements", Earthquake Spectra, 29(2):597-607, May 2013.


   The primary advantages of HingeRadau are

   * The user can specify a physically meaningful plastic hinge length
   * The largest bending moment is captured at the element ends
   * The exact numerical solution is recovered for a linear-elastic prismatic beam
   * The characteristic length is equal to the user-specified plastic hinge length when deformations localize at the element ends

   while the primary disadvantages are

   * The element post-yield response is too flexible for strain-hardening section response (consider using HingeRadauTwo)
   * The user needs to know the plastic hinge length a priori (empirical equations are available)
