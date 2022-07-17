.. include:: sub.txt

==================
 Dodd_Restrepo
==================

.. function:: uniaxialMaterial('Dodd_Restrepo', matTag, Fy, Fsu, ESH, ESU, Youngs, ESHI, FSHI, OmegaFac=1.0)
   :noindex:

   This command is used to construct a Dodd-Restrepo steel material

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``Fy`` |float|                        Yield strength
   ``Fsu`` |float|                       Ultimate tensile strength (UTS)
   ``ESH`` |float|                       Tensile strain at initiation of strain hardening
   ``ESU`` |float|                       Tensile strain at the UTS
   ``Youngs`` |float|                    Modulus of elasticity
   ``ESHI`` |float|                      Tensile strain for a point on strain hardening
                                         curve, recommended range of values for ESHI: [ (ESU + 5*ESH)/6, (ESU + 3*ESH)/4]
   ``FSHI`` |float|                      Tensile stress at point on strain hardening curve corresponding to ESHI
   ``OmegaFac`` |float|                  Roundedness factor for Bauschinger curve in cycle reversals from the strain hardening curve.
                                         Range: [0.75, 1.15]. Largest value tends to near a bilinear Bauschinger curve. Default = 1.0.
   ===================================   ===========================================================================



.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/DoddRestrepo>`_
