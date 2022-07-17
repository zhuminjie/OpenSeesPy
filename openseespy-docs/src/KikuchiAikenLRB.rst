.. include:: sub.txt

========================
KikuchiAikenLRB Material
========================

.. function:: uniaxialMaterial('KikuchiAikenLRB', matTag, type, ar, hr, gr, ap, tp, alph, beta, <'-T', temp>, <'-coKQ', rk, rq>, <'-coMSS', rs, rf>)
   :noindex:

   This command is used to construct a uniaxial KikuchiAikenLRB material object. This material model produces nonlinear hysteretic curves of lead-rubber bearings.



   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``type`` |int|                        rubber type (see note 1)
   ``ar`` |float|                        area of rubber [unit: m^2]
   ``hr`` |float|                        total thickness of rubber [unit: m]
   ``gr`` |float|                        shear modulus of rubber [unit: N/m^2]
   ``ap`` |float|                        area of lead plug [unit: m^2]
   ``tp`` |float|                        yield stress of lead plug [unit: N/m^2]
   ``alph`` |float|                      shear modulus of lead plug [unit: N/m^2]
   ``beta`` |float|                      ratio of initial stiffness to yielding stiffness
   ``temp`` |float|                      temperature [unit: °C]
   ``rk``    ``rq`` |float|              reduction rate for yielding stiffness (   ``rk``) and force at zero displacement (   ``rq``)
   ``rs``    ``rf`` |float|              reduction rate for stiffness (   ``rs``) and force (   ``rf``) (see note 3)
   ===================================   ===========================================================================

.. note::

   1) Following rubber types for    ``type`` are available:

      * ``1`` lead-rubber bearing, up to 400% shear strain [Kikuchi et al., 2010 & 2012]
   2) This material uses SI unit in calculation formula. Input arguments must be converted into [m], [m^2], [N/m^2].

   3)    ``rs`` and    ``rf`` are available if this material is applied to multipleShearSpring (MSS) element. Recommended values are    ``rs`` = :math:`\frac{1}{\sum_{i=0}^{n-1}\sin(\pi*i/n)^2}` and    ``rf`` = :math:`\frac{1}{\sum_{i=0}{n-1}\sin(\pi*i/n)}`, where n is the number of springs in the MSS. For example, when n=8,    ``rs`` = 0.2500 and ``rf`` = 0.1989.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/KikuchiAikenLRB_Material>`_
