.. include:: sub.txt

=====
VS3D4
=====

This command is used to construct a four-node 3D viscous-spring boundary quad element object based on a bilinear isoparametric formulation.



.. function:: element('VS3D4', eleTag,*eleNodes,E, G, rho, R, alphaN, alphaT)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  4 end nodes
   ``E`` |float|                         Young's Modulus of element material
   ``G`` |float|                         Shear Modulus of element material
   ``rho`` |float|                       Mass Density of element material
   ``R`` |float|                         distance from the scattered wave source to the boundary
   ``alphaN`` |float|                    correction parameter in the normal direction
   ``alphaT`` |float|                    correction parameter in the tangential direction
   ===================================   ===========================================================================

.. note::

   Reference: Liu J, Du Y, Du X, et al. 3D viscous-spring artificial boundary in time domain. Earthquake Engineering and Engineering Vibration, 2006, 5(1):93-102



.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/VS3D4>`_
