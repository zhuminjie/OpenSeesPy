.. include:: sub.txt

=================
 Elastic Section
=================

.. function:: section('Elastic', secTag, E_mod, A, Iz, G_mod=None, alphaY=None)
   :noindex:

.. function:: section('Elastic', secTag, E_mod, A, Iz, Iy, G_mod, Jxx, alphaY=None, alphaZ=None)
   :noindex:

   This command allows the user to construct an ElasticSection. The inclusion of shear deformations is optional. The dofs for 2D elastic section are ``[P, Mz]``,
   for 3D are ``[P,Mz,My,T]``.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``E_mod`` |float|                  Young's Modulus
   ``A`` |float|                      cross-sectional area of section
   ``Iz`` |float|                     second moment of area about the local z-axis
   ``Iy`` |float|                     second moment of area about the local y-axis
                                      (required for 3D analysis)
   ``G_mod`` |float|                  Shear Modulus (optional for 2D analysis,
                                      required for 3D analysis)
   ``Jxx`` |float|                    torsional moment of inertia of section
                                      (required for 3D analysis)
   ``alphaY`` |float|                 shear shape factor along the local y-axis (optional)
   ``alphaZ`` |float|                 shear shape factor along the local z-axis (optional)
   ================================   ===========================================================================


.. note::

   The elastic section can be used in the nonlinear beam column elements, which is useful in the initial stages of developing a complex model.
