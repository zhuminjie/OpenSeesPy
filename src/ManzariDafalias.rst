.. include:: sub.txt

==================
 ManzariDafalias
==================

.. function:: nDMaterial('ManzariDafalias', matTag, G0, nu, e_init, Mc, c, lambda_c, e0, ksi, P_atm, m, h0, ch, nb, A0, nd, z_max, cz, Den)
   :noindex:

   This command is used to construct a multi-dimensional Manzari-Dafalias(2004) material.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``G0`` |float|                     shear modulus constant
   ``nu`` |float|                     poisson ratio
   ``e_init`` |float|                 initial void ratio
   ``Mc`` |float|                     critical state stress ratio
   ``c`` |float|                      ratio of critical state stress ratio in extension and compression
   ``lambda_c`` |float|               critical state line constant
   ``e0`` |float|                     critical void ratio at p = 0
   ``ksi`` |float|                    critical state line constant
   ``P_atm`` |float|                  atmospheric pressure
   ``m`` |float|                      yield surface constant (radius of yield surface in stress ratio space)
   ``h0`` |float|                     constant parameter
   ``ch`` |float|                     constant parameter
   ``nb`` |float|                     bounding surface parameter, :math:`nb \ge 0`
   ``A0`` |float|                     dilatancy parameter
   ``nd`` |float|                     dilatancy surface parameter :math:`nd \ge 0`
   ``z_max`` |float|                  fabric-dilatancy tensor parameter
   ``cz`` |float|                     fabric-dilatancy tensor parameter
   ``Den`` |float|                    mass density of the material
   ================================   ===========================================================================

The material formulations for the ManzariDafalias object are:

* ``'ThreeDimensional'``
* ``'PlaneStrain'``

See also `here <http://opensees.berkeley.edu/wiki/index.php/Manzari_Dafalias_Material>`_

References

Dafalias YF, Manzari MT. "Simple plasticity sand model accounting for fabric change effects". Journal of Engineering Mechanics 2004
