.. include:: sub.txt

=====================
ElasticBilin Material
=====================

.. function:: uniaxialMaterial('ElasticBilin', matTag, EP1, EP2, epsP2, EN1=EP1, EN2=EP2, epsN2=-epsP2)
   :noindex:


   This command is used to construct an elastic bilinear uniaxial material object. Unlike all other bilinear materials, the unloading curve follows the loading curve exactly.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``EP1`` |float|                       tangent in tension for stains: 0 <= strains <=    ``epsP2``
   ``EP2`` |float|                       tangent when material in tension with strains >    ``epsP2``
   ``epsP2`` |float|                     strain at which material changes tangent in tension.
   ``EN1`` |float|                       optional, default =    ``EP1``. tangent in compression for stains: 0 < strains <=    ``epsN2``
   ``EN2`` |float|                       optional, default =    ``EP2``. tangent in compression with strains <    ``epsN2``
   ``epsN2`` |float|                     optional, default = ``-epsP2``. strain at which material changes tangent in compression.
   ===================================   ===========================================================================

.. note::

   ``eps0`` can not be controlled. It is always zero.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ElasticBilin_Material>`_
