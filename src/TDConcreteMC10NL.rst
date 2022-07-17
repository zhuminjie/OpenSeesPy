.. include:: sub.txt

==================
 TDConcreteMC10NL
==================

.. function:: uniaxialMaterial('TDConcreteMC10NL', matTag, fc, fcu, epscu, fct, Ec, Ecm, beta, tD, epsba, epsbb, epsda, epsdb, phiba, phibb, phida, phidb, tcast, cem)
   :noindex:

   This command is used to construct a uniaxial time-dependent concrete material object with non-linear behavior in compression (REF: Concrete02), nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage according to fib Model Code 2010.

   ===================================   =============================================================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fc`` |float|                        concrete compressive strength (compression is negative)
   ``fcu`` |float|                       concrete crushing strength (compression is negative)
   ``epscu`` |float|                     concrete strain at crushing strength (input as negative)
   ``fct`` |float|                       concrete tensile strength (tension is positive)
   ``Ec`` |float|                        concrete modulus of elasticity at loading age
   ``Ecm`` |float|                       concrete modulus of elasticity at 28 days
   ``beta`` |float|                      tension softening parameter (tension softening exponent)
   ``tD`` |float|			 analysis time at initiation of drying (in days)
   ``epsba`` |float|                     ultimate basic shrinkage strain (input as negative) as per fib Model Code 2010
   ``epsbb`` |float|                     fitting parameter of the basic shrinkage time evolution function as per fib Model Code 2010
   ``epsda`` |float|                     product of ultimate drying shrinkage strain and relative humidity function as per fib Model Code 2010
   ``epsdb`` |float|                     fitting parameter of the basic shrinkage time evolution function as per fib Model Code 2010
   ``phiba`` |float|                     parameter for the effect of compressive strength on basic creep as per fib Model Code 2010
   ``phibb`` |float|                     fitting parameter of the basic creep time evolution function as per fib Model Code 2010
   ``phida`` |float|                     product of the effect of compressive strength and relative humidity on drying creep as per fib Model Code 2010
   ``phidb`` |float|                     fitting parameter of the drying creep time evolution function as per fib Model Code 2010
   ``tcast`` |float|                     analysis time corresponding to concrete casting (in days; minimum value 2.0)
   ``cem`` |float|                       coefficient dependent on the type of cement as per fib Model Code 2010
   ===================================   =============================================================================================================

.. note::

   #. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
   #. Shrinkage concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).


.. seealso::


   `Detailed descriptions of the model and its implementation can be found in the following:`
   `(1) Knaack, A.M., Kurama, Y.C. 2018. Modeling Time-Dependent Deformations: Application for Reinforced Concrete Beams with Recycled Concrete Aggregates. ACI Structural J. 115, 175-190. doi:10.14359/51701153`
   `(2) Knaack, A.M., 2013. Sustainable concrete structures using recycled concrete aggregate: short-term and long-term behavior considering material variability. PhD Dissertation, Civil and Environmental Engineering and Earth Sciences, University of Notre Dame, Notre Dame, Indiana, USA, 680 pp`
   `A manual describing the use of the model and sample files can be found at:`  
   `<https://data.mendeley.com/datasets/z4gxnhchky/1>`_
