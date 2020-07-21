.. include:: sub.txt

=============================
Pinching4 Material
=============================

.. function:: uniaxialMaterial('Pinching4', matTag,ePf1, ePd1, ePf2, ePd2, ePf3, ePd3, ePf4, ePd4, <eNf1, eNd1, eNf2, eNd2, eNf3, eNd3, eNf4, eNd4>, rDispP, rForceP, uForceP, <rDispN, rForceN, uForceN>, gK1, gK2, gK3, gK4, gKLim, gD1, gD2, gD3, gD4, gDLim, gF1, gF2, gF3, gF4, gFLim, gE, dmgType)
   :noindex:

   This command is used to construct a uniaxial material that represents a 'pinched' load-deformation response and exhibits degradation under cyclic loading. Cyclic degradation of strength and stiffness occurs in three ways: unloading stiffness degradation, reloading stiffness degradation, strength degradation.

   ==========================================================   ===========================================================================
   ``matTag`` |int|                                             integer tag identifying material
   ``ePf1``    ``ePf2``    ``ePf3``    ``ePf4`` |float|         floating point values defining force points on the positive response envelope
   ``ePd1``    ``ePd2``    ``ePd3``    ``ePd4`` |float|         floating point values defining deformation points on the positive response envelope
   ``eNf1``    ``eNf2``    ``eNf3``    ``eNf4`` |float|         floating point values defining force points on the negative response envelope
   ``eNd1``    ``eNd2``    ``eNd3``    ``eNd4`` |float|         floating point values defining deformation points on the negative response envelope
   ``rDispP`` |float|                                           floating point value defining the ratio of the deformation at which reloading occurs to the maximum historic deformation demand
   ``fFoceP`` |float|                                           floating point value defining the ratio of the force at which reloading begins to force corresponding to the maximum historic deformation demand
   ``uForceP`` |float|                                          floating point value defining the ratio of strength developed upon unloading from negative load to the maximum strength developed under monotonic loading
   ``rDispN`` |float|                                           floating point value defining the ratio of the deformation at which reloading occurs to the minimum historic deformation demand
   ``fFoceN`` |float|                                           floating point value defining the ratio of the force at which reloading begins to force corresponding to the minimum historic deformation demand
   ``uForceN`` |float|                                          floating point value defining the ratio of strength developed upon unloading from negative load to the minimum strength developed under monotonic loading
   ``gK1``  ``gK2``  ``gK3``  ``gK4``  ``gKLim`` |float|        floating point values controlling cyclic degradation model for unloading stiffness degradation
   ``gD1``  ``gD2``  ``gD3``  ``gD4``  ``gDLim`` |float|        floating point values controlling cyclic degradation model for reloading stiffness degradation
   ``gF1``  ``gF2``  ``gF3``  ``gF4``  ``gFLim`` |float|        floating point values controlling cyclic degradation model for strength degradation
   ``gE`` |float|                                               floating point value used to define maximum energy dissipation under cyclic loading. Total energy dissipation capacity is defined as this factor multiplied by the energy dissipated under monotonic loading.
   ``dmgType`` |str|                                            string to indicate type of damage (option: ``'cycle'``, ``'energy'``)
   ==========================================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Pinching4_Material>`_
