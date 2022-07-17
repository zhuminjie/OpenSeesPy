.. include:: sub.txt

==================
 Damage2p
==================

.. function:: nDMaterial('Damage2p', matTag, fcc, '-fct', fct, '-E', E, '-ni', ni, '-Gt', Gt, '-Gc', Gc, '-rho_bar', rho_bar, '-H', H, '-theta', theta, '-tangent', tangent)
   :noindex:

   This command is used to construct a three-dimensional material object that has a Drucker-Prager plasticity model coupled with a two-parameter damage model.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``fcc`` |float|                    concrete compressive strength,
                                      negative real value (positive input is changed in sign automatically)
   ``fct`` |float|                    optional concrete tensile strength,
                                      positive real value (for concrete like materials is less than fcc),
				      :math:`0.1*abs(fcc)` =
				      :math:`4750*sqrt(abs(fcc))\text{ }if\text{ }abs(fcc)<2000`
				      because fcc is assumed in MPa (see ACI 318)
   ``E`` |float|                      optional Young modulus,
                                      :math:`57000*sqrt(abs(fcc))` if :math:`abs(fcc)>2000`
                                      because fcc is assumed in psi (see ACI 318)
   ``ni`` |float|                     optional Poisson coefficient,
                                      0.15 (from comparison with tests by Kupfer Hilsdorf Rusch 1969)
   ``Gt`` |float|                     optional tension fracture energy density,
                                      positive real value (integral of the stress-strain envelope in tension),
				      :math:`1840*fct*fct/E`
				      (from comparison with tests by Gopalaratnam and Shah 1985)
   ``Gc`` |float|                     optional compression fracture energy density,
                                      positive real value (integral of the stress-strain
                                      envelope after the peak in compression),
				      :math:6250*fcc*fcc/E`
				      (from comparison with tests by Karsan and Jirsa 1969)
   ``rho_bar`` |float|                optional parameter of plastic volume change,
                                      positive real value :math:`0=rhoBar< sqrt(2/3)`,
				      0.2 (from comparison with tests by Kupfer Hilsdorf Rusch 1969)
   ``H`` |float|                      optional linear hardening parameter for plasticity,
                                      positive real value (usually less than E),
				      :math:`0.25*E`
				      (from comparison with tests by Karsan and Jirsa 1969 and
				      Gopalaratnam and Shah 1985)
   ``theta`` |float|                  optional ratio between isotropic and kinematic hardening,
                                      positive real value :math:`0=theta=1` (with: 0 hardening kinematic
                                      only and 1 hardening isotropic only,
				      0.5 (from comparison with tests by Karsan and Jirsa 1969
				      and Gopalaratnam and Shah 1985)
   ``tangent`` |float|                optional integer to choose the computational stiffness matrix,
                                      0: computational tangent; 1: damaged secant stiffness
                                      (hint: in case of strong nonlinearities use it with
                                      Krylov-Newton algorithm)
   ================================   ===========================================================================

The material formulations for the Damage2p object are:

* ``'ThreeDimensional'``
* ``'PlaneStrain'``
* ``'Plane Stress'``
* ``'AxiSymmetric'``
* ``'PlateFiber'``

See also `here <http://opensees.berkeley.edu/wiki/index.php/Damage2p>`_
