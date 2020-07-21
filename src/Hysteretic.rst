.. include:: sub.txt

============
 Hysteretic
============

.. function:: uniaxialMaterial('Hysteretic', matTag, *p1, *p2, *p3=p2, *n1, *n2, *n3=n2, pinchX, pinchY, damage1, damage2, beta=0.0)
   :noindex:

   This command is used to construct a uniaxial bilinear hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``p1`` |listf|                        ``p1=[s1p, e1p]``, stress and strain (or force
                                         & deformation) at first point of the envelope
					 in the positive direction
   ``p2`` |listf|                        ``p2=[s2p, e2p]``, stress and strain (or force
                                         & deformation) at second point of the envelope
					 in the positive direction
   ``p3`` |listf|                        ``p3=[s3p, e3p]``, stress and strain (or force
                                         & deformation) at third point of the envelope
					 in the positive direction
   ``n1`` |listf|                        ``n1=[s1n, e1n]``, stress and strain (or force
                                         & deformation) at first point of the envelope
					 in the negative direction
   ``n2`` |listf|                        ``n2=[s2n, e2n]``, stress and strain (or force
                                         & deformation) at second point of the envelope
					 in the negative direction
   ``n3`` |listf|                        ``n3=[s3n, e3n]``, stress and strain (or force
                                         & deformation) at third point of the envelope
					 in the negative direction
   ``pinchX`` |float|                    pinching factor for strain (or deformation) during reloading
   ``pinchY`` |float|                    pinching factor for stress (or force) during reloading
   ``damage1`` |float|                   damage due to ductility: D1(mu-1)
   ``damage2`` |float|                   damage due to energy: D2(Eii/Eult)
   ``beta`` |float|                      power used to determine the degraded unloading
                                         stiffness based on ductility, mu-beta (optional, default=0.0)

   ===================================   ===========================================================================

.. seealso::


   `Steel4 <http://opensees.berkeley.edu/wiki/index.php/Hysteretic_Material>`_
