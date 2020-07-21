.. include:: sub.txt

==================
AxialSpHD Material
==================

.. function:: uniaxialMaterial('AxialSpHD', matTag,sce, fty, fcy, <bte, bty, bth, bcy, fcr, ath>)
   :noindex:

   This command is used to construct a uniaxial AxialSpHD material object. This material model produces axial stress-strain curve of elastomeric bearings including hardening behavior.


   ===========================================   ===========================================================================
   ``matTag`` |int|                              integer tag identifying material
   ``sce`` |float|                               compressive modulus
   ``fty``    ``fcy`` |float|                    yield stress under tension (``fty``) and compression (``fcy``) (see note 1)
   ``bte``  ``bty``  ``bth``  ``bcy`` |float|    reduction rate for tensile elastic range (``bte``), tensile yielding (``bty``), tensile hardening (   ``bth``) and compressive yielding (``bcy``) (see note 1)
   ``fcr`` |float|                               target point stress (see note 1)
   ``ath`` |float|                               hardening strain ratio to yield strain
   ===========================================   ===========================================================================

.. note::

    #. Input parameters are required to satisfy followings.

       ``fcy`` < 0.0 <    ``fty``

       0.0 <=    ``bty`` <    ``bth`` <    ``bte`` <= 1.0

       0.0 <=    ``bcy`` <= 1.0

       ``fcy`` <=    ``fcr`` <= 0.0

       1.0 <=    ``ath``

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/AxialSpHD_Material>`_
