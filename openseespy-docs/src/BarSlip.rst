.. include:: sub.txt

===================
 BarSlip Material
===================

.. function:: uniaxialMaterial('BarSlip', matTag, fc, fy, Es, fu, Eh, db, ld, nb, depth, height, ancLratio=1.0, bsFlag, type, damage='Damage', unit='psi')
   :noindex:

   This command is used to construct a uniaxial material that simulates the bar force versus slip response of a reinforcing bar anchored in a beam-column joint. The model exhibits degradation under cyclic loading. Cyclic degradation of strength and stiffness occurs in three ways: unloading stiffness degradation, reloading stiffness degradation, strength degradation.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fc`` |float|                        positive floating point value defining the compressive strength of the concrete in which the reinforcing bar is anchored
   ``fy`` |float|                        positive floating point value defining the yield strength of the reinforcing steel
   ``Es`` |float|                        floating point value defining the modulus of elasticity of the reinforcing steel
   ``fu`` |float|                        positive floating point value defining the ultimate strength of the reinforcing steel
   ``Eh`` |float|                        floating point value defining the hardening modulus of the reinforcing steel
   ``ld`` |float|                        floating point value defining the development length of the reinforcing steel
   ``db`` |float|                        point value defining the diameter of reinforcing steel
   ``nb`` |int|                          an integer defining the number of anchored bars
   ``depth`` |float|                     floating point value defining the dimension of the member (beam or column) perpendicular to the dimension of the plane of the paper
   ``height`` |float|                    floating point value defining the height of the flexural member, perpendicular to direction in which the reinforcing steel is placed, but in the plane of the paper
   ``ancLratio`` |float|                 floating point value defining the ratio of anchorage length used for the reinforcing bar to the dimension of the joint in the direction of the reinforcing bar (optional, default: 1.0)
   ``bsFlag`` |str|                      string indicating relative bond strength for the anchored reinforcing bar (options: ``'Strong'`` or ``'Weak'``)
   ``type`` |str|                        string indicating where the reinforcing bar is placed. (options: ``'beamtop'``, ``'beambot'`` or ``'column'``)
   ``damage`` |str|                      string indicating type of damage:whether there is full damage in the material or no damage (optional, options: ``'Damage'``, ``'NoDamage'`` ; default: ``'Damage'``)
   ``unit`` |str|                        string indicating the type of unit system used (optional, options: ``'psi'``, ``'MPa'``, ``'Pa'``, ``'psf'``, ``'ksi'``, ``'ksf'``) (default: ``'psi'`` / ``'MPa'``)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/BARSLIP_Material>`_
