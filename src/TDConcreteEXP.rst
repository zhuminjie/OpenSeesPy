.. include:: sub.txt

==================
 TDConcreteEXP
==================

.. function:: uniaxialMaterial('TDConcreteEXP', matTag, fc, fct, Ec, beta, tD, epsshu, psish, Tcr, epscru, sigCr, psicr1, psicr2, tcast)
   :noindex:

   This command is used to construct a uniaxial time-dependent concrete material object with linear behavior in compression, nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage according to ACI 209R-92.

   ===================================   =====================================================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fc`` |float|                        concrete compressive strength (compression is negative)
   ``fct`` |float|                       concrete tensile strength (tension is positive)
   ``Ec`` |float|                        concrete modulus of elasticity
   ``beta`` |float|                      tension softening parameter (tension softening exponent)
   ``tD`` |float|						 analysis time at initiation of drying (in days)
   ``epsshu`` |float|                    ultimate shrinkage strain as per ACI 209R-92 (shrinkage is negative)
   ``psish`` |float|                     fitting parameter of the shrinkage time evolution function as per ACI 209R-92
   ``Tcr`` |float|                       creep model age (in days)
   ``epscru`` |float|                    ultimate creep strain (e.g., taken from experimental measurements)
   ``sigCr`` |float|                     concrete compressive stress (input as negative) associated with $epscru (e.g., experimentally applied)
   ``psicr1`` |float|                    fitting parameter of the creep time evolution function as per ACI 209R-92
   ``psicr2`` |float|                    fitting parameter of the creep time evolution function as per ACI 209R-92
   ``tcast`` |float|                     analysis time corresponding to concrete casting (in days; minimum value 2.0)
   ===================================   =====================================================================================================

.. note::

   #. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
   #. Shrinkage concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).


.. seealso::


   `Detailed descriptions of the model and its implementation can be found in the following:`
   `(1) Knaack, A.M., Kurama, Y.C. 2018. Modeling Time-Dependent Deformations: Application for Reinforced Concrete Beams with Recycled Concrete Aggregates. ACI Structural J. 115, 175-190. doi:10.14359/51701153`
   `(2) Knaack, A.M., 2013. Sustainable concrete structures using recycled concrete aggregate: short-term and long-term behavior considering material variability. PhD Dissertation, Civil and Environmental Engineering and Earth Sciences, University of Notre Dame, Notre Dame, Indiana, USA, 680 pp`
   `A manual describing the use of the model and sample files can be found at:`  
   `<https://data.mendeley.com/datasets/z4gxnhchky/1>`_
