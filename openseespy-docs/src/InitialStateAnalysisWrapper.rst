.. include:: sub.txt

=============================
 InitialStateAnalysisWrapper
=============================

.. function:: nDMaterial('InitialStateAnalysisWrapper', matTag, nDMatTag, nDim)
   :noindex:

   The InitialStateAnalysisWrapper nDMaterial allows for the use of the InitialStateAnalysis command for setting initial conditions. The InitialStateAnalysisWrapper can be used with any nDMaterial. This material wrapper allows for the development of an initial stress field while maintaining the original geometry of the problem. An example analysis is provided below to demonstrate the use of this material wrapper object.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``nDMatTag`` |int|                 the tag of the associated nDMaterial object
   ``nDim`` |int|                     number of dimensions (2 for 2D, 3 for 3D)
   ================================   ===========================================================================


.. note::

   #. There are no valid recorder queries for the InitialStateAnalysisWrapper.
   #. The InitialStateAnalysis off command removes all previously defined recorders. Two sets of recorders are needed if the results before and after this command are desired. See the example below for more.
   #. The InitialStateAnalysisWrapper material is somewhat tricky to use in dynamic analysis. Sometimes setting the displacement to zero appears to be interpreted as an initial displacement in subsequent steps, resulting in undesirable vibrations.
