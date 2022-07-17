.. include:: sub.txt

=============================
KikuchiAikenHDR Material
=============================

.. function:: uniaxialMaterial('KikuchiAikenHDR', matTag, tp, ar, hr, <'-coGHU', cg, ch, cu>, <'-coMSS', rs, rf>)
   :noindex:

   This command is used to construct a uniaxial KikuchiAikenHDR material object. This material model produces nonlinear hysteretic curves of high damping rubber bearings (HDRs).



   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``tp`` |str|                          rubber type (see note 1)
   ``ar`` |float|                        area of rubber [unit: m^2] (see note 2)
   ``hr`` |float|                        total thickness of rubber [unit: m] (see note 2)
   ``cg``  ``ch``  ``cu`` |float|        correction coefficients for equivalent shear modulus (``cg``), equivalent viscous daming ratio (``ch``), ratio of shear force at zero displacement (``cu``).
   ``rs``  ``rf`` |float|                reduction rate for stiffness (``rs``) and force (``rf``) (see note 3)
   ===================================   ===========================================================================

.. note::

   1) Following rubber types for    ``tp`` are available:

      * ``'X0.6'`` Bridgestone X0.6, standard compressive stress, up to 400% shear strain
      * ``'X0.6-0MPa'`` Bridgestone X0.6, zero compressive stress, up to 400% shear strain
      * ``'X0.4'`` Bridgestone X0.4, standard compressive stress, up to 400% shear strain
      * ``'X0.4-0MPa'`` Bridgestone X0.4, zero compressive stress, up to 400% shear strain
      * ``'X0.3'`` Bridgestone X0.3, standard compressive stress, up to 400% shear strain
      * ``'X0.3-0MPa'`` Bridgestone X0.3, zero compressive stress, up to 400% shear strain

   2) This material uses SI unit in calculation formula.    ``ar`` and    ``hr`` must be converted into [m^2] and [m], respectively.

   3)    ``rs`` and    ``rf`` are　available if this material is applied to multipleShearSpring (MSS) element. Recommended values are    ``rs`` = :math:`\frac{1}{\sum_{i=0}^{n-1}\sin(\pi*i/n)^2}` and    ``rf`` = :math:`\frac{1}{\sum_{i=0}^{n-1}\sin(\pi*i/n)}`, where n is the number of springs in the MSS. For example, when n=8,    ``rs`` =0.2500,    ``rf`` =0.1989.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/KikuchiAikenHDR_Material>`_
