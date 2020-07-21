.. include:: sub.txt

================
AxialSp Material
================

.. function:: uniaxialMaterial('AxialSp', matTag,sce, fty, fcy, <bte, bty, bcy, fcr>)
   :noindex:

   This command is used to construct a uniaxial AxialSp material object. This material model produces axial stress-strain curve of elastomeric bearings.



   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``sce`` |float|                       compressive modulus
   ``fty``    ``fcy`` |float|            yield stress under tension (   ``fty``) and compression (   ``fcy``) (see note 1)
   ``bte``  ``bty``  ``bcy`` |float|     reduction rate for tensile elastic range (   ``bte``), tensile yielding (   ``bty``) and compressive yielding (   ``bcy``) (see note 1)
   ``fcr`` |float|                       target point stress (see note 1)
   ===================================   ===========================================================================

.. note::

   #. Input parameters are required to satisfy followings.

      ``fcy`` < 0.0 <    ``fty``

      0.0 <=    ``bty`` <    ``bte`` <= 1.0

      0.0 <=    ``bcy`` <= 1.0

      ``fcy`` <=    ``fcr`` <= 0.0


.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/AxialSp_Material>`_
