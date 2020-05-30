.. include:: sub.txt

=====================
 updateMaterialStage
=====================

.. function:: updateMaterialStage('-material',matTag,'-stage',value,'-parameter',paramTag)
   :noindex:

   This function is used in geotechnical modeling to maintain elastic nDMaterial response during the application of gravity loads. The material is then updated to allow for plastic strains during additional static loads or earthquakes.

   ========================   =============================================================
   ``matTag`` |int|           tag of nDMaterial
   ``value`` |int|            stage value
   ``paramTag`` |int|         tag of parameter (optional)
   ========================   =============================================================

