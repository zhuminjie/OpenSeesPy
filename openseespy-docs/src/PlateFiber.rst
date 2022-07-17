.. include:: sub.txt

==================
 PlateFiber
==================

.. function:: nDMaterial('PlateFiber', matTag, threeDTag)
   :noindex:

   This command is used to construct a plate-fiber material wrapper which converts any three-dimensional material into a plate fiber material (by static condensation) appropriate for shell analysis.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``threeDTag`` |float|              material tag for a previously-defined three-dimensional material
   ================================   ===========================================================================
