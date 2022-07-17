.. include:: sub.txt

=======================
Hyperbolic Gap Material
=======================

.. function:: uniaxialMaterial('HyperbolicGapMaterial', matTag, Kmax, Kur, Rf, Fult, gap)
   :noindex:

   This command is used to construct a hyperbolic gap material object.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``Kmax`` |float|                      initial stiffness
   ``Kur`` |float|                       unloading/reloading stiffness
   ``Rf`` |float|                        failure ratio
   ``Fult`` |float|                      ultimate (maximum) passive resistance
   ``gap`` |float|                       initial gap
   ===================================   ===========================================================================

.. note::

   #. This material is implemented as a compression-only gap material. ``Fult`` and ``gap`` should be input as negative values.
   #. Recomended Values:

      * ``Kmax``	= 20300 kN/m of abutment width
      * ``Kcur``	= ``Kmax``
      * ``Rf``	= 0.7
      * ``Fult``	= -326 kN per meter of abutment width
      * ``gap``	= -2.54 cm

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Hyperbolic_Gap_Material>`_
