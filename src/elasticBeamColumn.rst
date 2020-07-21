.. include:: sub.txt

.. _elasticBeamColumn:

===========================
Elastic Beam Column Element
===========================

This command is used to construct an elasticBeamColumn element object. The arguments for the construction of an elastic beam-column element depend on the dimension of the problem, (ndm)



.. function:: element('elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, Iz, transfTag, <'-mass', mass>,<'-cMass'>, <'-release', releaseCode>)
   :noindex:

   For a two-dimensional problem


.. function:: element('elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, G_mod, Jxx, Iy, Iz, transfTag, <'-mass', mass>, <'-cMass'>)
   :noindex:

   For a three-dimensional problem

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``Area`` |float|                      cross-sectional area of element
   ``E_mod`` |float|                     Young's Modulus
   ``G_mod`` |float|                     Shear Modulus
   ``Jxx`` |float|                       torsional moment of inertia of cross section
   ``Iz`` |float|                        second moment of area about the local z-axis
   ``Iy`` |float|                        second moment of area about the local y-axis
   ``transfTag`` |int|                   identifier for previously-defined coordinate-transformation (CrdTransf) object
   ``mass`` |float|                      element mass per unit length (optional, default = 0.0)
   ``'-cMass'`` |str|                    to form consistent mass matrix (optional, default = lumped mass matrix)
   ``'releaseCode'`` |int|               moment release (optional, 2d only, 0=no release (default), 1=release at I, 2=release at J, 3=release at I and J)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic_Beam_Column_Element>`_
