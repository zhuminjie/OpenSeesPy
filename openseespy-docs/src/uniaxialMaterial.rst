.. include:: sub.txt

===========================
 uniaxialMaterial commands
===========================

.. function:: uniaxialMaterial(matType, matTag, *matArgs)

   This command is used to construct a UniaxialMaterial object which represents uniaxial stress-strain (or force-deformation) relationships.

   ================================   ===========================================================================
   ``matType`` |str|                  material type
   ``matTag`` |int|                   material tag.
   ``matArgs`` |list|                 a list of material arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example,

.. code-block:: python

   matType = 'Steel01'
   matTag = 1
   matArgs = [Fy, E0, b]
   uniaxialMaterial(matType, matTag, *matArgs)



The following contain information about available ``matType``:

Steel & Reinforcing-Steel Materials
-----------------------------------


#. :doc:`steel01`
#. :doc:`steel02`
#. :doc:`steel4`
#. :doc:`Hysteretic`
#. :doc:`ReinforcingSteel`
#. :doc:`Dodd_Restrepo`
#. :doc:`RambergOsgoodSteel`
#. :doc:`SteelMPF`
#. :doc:`steel01thermal`


.. toctree::
   :maxdepth: 2
   :hidden:

   steel01
   steel02
   steel4
   Hysteretic
   ReinforcingSteel
   Dodd_Restrepo
   RambergOsgoodSteel
   SteelMPF
   steel01thermal



Concrete Materials
------------------


#. :doc:`Concrete01`
#. :doc:`Concrete02`
#. :doc:`Concrete04`
#. :doc:`Concrete06`
#. :doc:`Concrete07`
#. :doc:`Concrete01WithSITC`
#. :doc:`ConfinedConcrete01`
#. :doc:`ConcreteD`
#. :doc:`FRPConfinedConcrete`
#. :doc:`FRPConfinedConcrete02`
#. :doc:`ConcreteCM`
#. :doc:`TDConcrete`
#. :doc:`TDConcreteEXP`
#. :doc:`TDConcreteMC10`
#. :doc:`TDConcreteMC10NL`

      
.. toctree::
   :maxdepth: 2
   :hidden:

   Concrete01
   Concrete02
   Concrete04
   Concrete06
   Concrete07
   Concrete01WithSITC
   ConfinedConcrete01
   ConcreteD
   FRPConfinedConcrete
   FRPConfinedConcrete02
   ConcreteCM
   TDConcrete
   TDConcreteEXP
   TDConcreteMC10
   TDConcreteMC10NL


Standard Uniaxial Materials
---------------------------


#. :doc:`ElasticUni`
#. :doc:`ElasticPP`
#. :doc:`ElasticPPGap`
#. :doc:`ENT`
#. :doc:`ParallelUni`
#. :doc:`SeriesUni`


.. toctree::
   :maxdepth: 2
   :hidden:

   ElasticUni
   ElasticPP
   ElasticPPGap
   ENT
   ParallelUni
   SeriesUni


PyTzQz uniaxial materials for p-y, t-z and q-z elements for modeling soil-structure interaction through the piles in a structural foundation
--------------------------------------------------------------------------------------------------------------------------------------------

#. :doc:`PySimple1`
#. :doc:`TzSimple1`
#. :doc:`QzSimple1`
#. :doc:`PyLiq1`
#. :doc:`TzLiq1`


.. toctree::
   :maxdepth: 2
   :hidden:

   PySimple1
   TzSimple1
   QzSimple1
   PyLiq1
   TzLiq1


Other Uniaxial Materials
------------------------


#. :doc:`Hardening`
#. :doc:`Cast`
#. :doc:`ViscousDamper`
#. :doc:`BilinearOilDamper`
#. :doc:`Bilin`
#. :doc:`ModIMKPeakOriented`
#. :doc:`ModIMKPinching`
#. :doc:`SAWS`
#. :doc:`BarSlip`
#. :doc:`Bond_SP01`
#. :doc:`Fatigue`
#. :doc:`ImpactMaterial`
#. :doc:`HyperbolicGapMaterial`
#. :doc:`LimitState`
#. :doc:`MinMax`
#. :doc:`ElasticBilin`
#. :doc:`ElasticMultiLinear`
#. :doc:`MultiLinear`
#. :doc:`InitStrainMaterial`
#. :doc:`InitStressMaterial`
#. :doc:`PathIndependent`
#. :doc:`Pinching4`
#. :doc:`ECC01`
#. :doc:`SelfCentering`
#. :doc:`Viscous`
#. :doc:`BoucWen`
#. :doc:`BWBN`
#. :doc:`KikuchiAikenHDR`
#. :doc:`KikuchiAikenLRB`
#. :doc:`AxialSp`
#. :doc:`AxialSpHD`
#. :doc:`PinchingLimitStateMaterial`
#. :doc:`CFSWSWP`
#. :doc:`CFSSSWP`


.. toctree::
   :maxdepth: 2
   :hidden:

   Hardening
   Cast
   ViscousDamper
   BilinearOilDamper
   Bilin
   ModIMKPeakOriented
   ModIMKPinching
   SAWS
   BarSlip
   Bond_SP01
   Fatigue
   ImpactMaterial
   HyperbolicGapMaterial
   LimitState
   MinMax
   ElasticBilin
   ElasticMultiLinear
   MultiLinear
   InitStrainMaterial
   InitStressMaterial
   PathIndependent
   Pinching4
   ECC01
   SelfCentering
   Viscous
   BoucWen
   BWBN
   KikuchiAikenHDR
   KikuchiAikenLRB
   AxialSp
   AxialSpHD
   PinchingLimitStateMaterial
   CFSWSWP
   CFSSSWP
