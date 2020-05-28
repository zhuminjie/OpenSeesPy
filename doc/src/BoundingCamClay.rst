.. include:: sub.txt

==================
 BoundingCamClay
==================

.. function:: nDMaterial('BoundingCamClay', matTag, massDensity, C, bulkMod, OCR, mu_o, alpha, lambda, h, m)
   :noindex:

   This command is used to construct a multi-dimensional bounding surface Cam Clay material object after Borja et al. (2001).

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``massDensity`` |float|            mass density
   ``C`` |float|                      ellipsoidal axis ratio (defines shape of ellipsoidal
                                      loading/bounding surfaces)
   ``bulkMod`` |float|                initial bulk modulus
   ``OCR`` |float|                    overconsolidation ratio
   ``mu_o`` |float|                   initial shear modulus
   ``alpha`` |float|                  pressure-dependency parameter for modulii (greater than or equal to zero)
   ``lambda`` |float|                 soil compressibility index for virgin loading
   ``h`` |float|                      hardening parameter for plastic response inside of bounding
                                      surface (if h = 0, no hardening)
   ``m`` |float|                      hardening parameter (exponent) for plastic response inside
                                      of bounding surface (if m = 0, only linear hardening)
   ================================   ===========================================================================

The material formulations for the BoundingCamClay object are:

* ``'ThreeDimensional'``
* ``'PlaneStrain'``

See also for `information <http://opensees.berkeley.edu/wiki/index.php/Bounding_Cam_Clay>`_
