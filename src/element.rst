.. include:: sub.txt

==================
 element commands
==================

.. function:: element(eleType, eleTag, *eleNodes, *eleArgs)

   Create a OpenSees element.

   ================================   ===========================================================================
   ``eleType`` |str|                  element type
   ``eleTag`` |int|                   element tag.
   ``eleNodes`` |listi|               a list of element nodes, must be preceded with ``*``.
   ``eleArgs`` |list|                 a list of element arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example,

.. code-block:: python

   eleType = 'truss'
   eleTag = 1
   eleNodes = [iNode, jNode]
   eleArgs = [A, matTag]
   element(eleType, eleTag, *eleNodes, *eleArgs)



The following contain information about available ``eleType``:

Zero-Length Element
--------------------

#. :doc:`ZeroLength`
#. :doc:`zeroLengthND`
#. :doc:`zeroLengthSection`
#. :doc:`CoupledZeroLength`
#. :doc:`zeroLengthContact2D`
#. :doc:`zeroLengthContactNTS2D`
#. :doc:`zeroLengthInterface2D`
#. :doc:`zeroLengthImpact3D`


.. toctree::
   :maxdepth: 2
   :hidden:

   ZeroLength
   zeroLengthND
   zeroLengthSection
   CoupledZeroLength
   zeroLengthContact2D
   zeroLengthContactNTS2D
   zeroLengthInterface2D
   zeroLengthImpact3D


Truss Elements
--------------

#. :doc:`trussEle`
#. :doc:`corotTruss`

.. toctree::
   :maxdepth: 2
   :hidden:

   trussEle
   corotTruss


Beam-Column Elements
--------------------

#. :doc:`elasticBeamColumn`
#. :doc:`ModElasticBeam2d`
#. :doc:`ElasticTimoshenkoBeam`
#. :doc:`beamWithHinges`
#. :doc:`dispBeamColumn`
#. :doc:`ForceBeamColumn`
#. :doc:`nonlinearBeamColumn`
#. :doc:`dispBeamColumnInt`
#. :doc:`MVLEM`
#. :doc:`SFI_MVLEM`

      
.. toctree::
   :maxdepth: 2
   :hidden:

   elasticBeamColumn
   ModElasticBeam2d
   ElasticTimoshenkoBeam
   beamWithHinges
   dispBeamColumn
   ForceBeamColumn
   nonlinearBeamColumn
   dispBeamColumnInt
   MVLEM
   SFI_MVLEM


Joint Elements
--------------

#. :doc:`beamColumnJoint`
#. :doc:`ElasticTubularJoint`
#. :doc:`Joint2D`


.. toctree::
   :maxdepth: 2
   :hidden:

   beamColumnJoint
   ElasticTubularJoint
   Joint2D

Link Elements
-------------

#. :doc:`twoNodeLink`

      
.. toctree::
   :maxdepth: 2
   :hidden:

   twoNodeLink



Bearing Elements
----------------

#. :doc:`elastomericBearingPlasticity`
#. :doc:`elastomericBearingBoucWen`
#. :doc:`flatSliderBearing`
#. :doc:`singleFPBearing`
#. :doc:`TFP`
#. :doc:`TripleFrictionPendulum`
#. :doc:`multipleShearSpring`
#. :doc:`KikuchiBearing`
#. :doc:`YamamotoBiaxialHDR`
#. :doc:`ElastomericX`
#. :doc:`LeadRubberX`
#. :doc:`HDR`
#. :doc:`RJWatsonEqsBearing`
#. :doc:`FPBearingPTV`

      
.. toctree::
   :maxdepth: 2
   :hidden:

   elastomericBearingPlasticity
   elastomericBearingBoucWen
   flatSliderBearing
   singleFPBearing
   TFP
   TripleFrictionPendulum
   multipleShearSpring
   KikuchiBearing
   YamamotoBiaxialHDR
   ElastomericX
   LeadRubberX
   HDR
   RJWatsonEqsBearing
   FPBearingPTV

Quadrilateral Elements
----------------------


#. :doc:`quad`
#. :doc:`ShellMITC4`
#. :doc:`ShellDKGQ`
#. :doc:`ShellDKGT`
#. :doc:`ShellNLDKGQ`
#. :doc:`ShellNLDKGT`
#. :doc:`ShellNL`
#. :doc:`bbarQuad`
#. :doc:`enhancedQuad`
#. :doc:`SSPquad`
#. :doc:`MVLEM_3D`
#. :doc:`SFI_MVLEM_3D`

.. toctree::
   :maxdepth: 2
   :hidden:

   quad
   ShellMITC4
   ShellDKGQ
   ShellDKGT
   ShellNLDKGQ
   ShellNLDKGT
   ShellNL
   bbarQuad
   enhancedQuad
   SSPquad
   MVLEM_3D
   SFI_MVLEM_3D


Triangular Elements
-------------------

#. :doc:`tri31`

.. toctree::
   :maxdepth: 2
   :hidden:

   tri31


Brick Elements
--------------

#. :doc:`stdBrick`
#. :doc:`bbarBrick`
#. :doc:`20NodeBrick`
#. :doc:`SSPbrick`


.. toctree::
   :maxdepth: 2
   :hidden:

   stdBrick
   bbarBrick
   20NodeBrick
   SSPbrick


Tetrahedron Elements
--------------------

#. :doc:`FourNodeTetrahedron`

      
.. toctree::
   :maxdepth: 2
   :hidden:

   FourNodeTetrahedron


UC San Diego u-p element (saturated soil)
-----------------------------------------

#. :doc:`quadUP`
#. :doc:`brickUP`
#. :doc:`bbarQuadUP`
#. :doc:`bbarBrickUP`
#. :doc:`NineFourNodeQuadUP`
#. :doc:`TwentyEightNodeBrickUP`


      
.. toctree::
   :maxdepth: 2
   :hidden:

   quadUP
   brickUP
   bbarQuadUP
   bbarBrickUP
   NineFourNodeQuadUP
   TwentyEightNodeBrickUP

Other u-p elements
------------------

#. :doc:`SSPquadUP`
#. :doc:`SSPbrickUP`

      
.. toctree::
   :maxdepth: 2
   :hidden:

   SSPquadUP
   SSPbrickUP

Contact Elements
----------------

#. :doc:`SimpleContact2D`
#. :doc:`SimpleContact3D`
#. :doc:`BeamContact2D`
#. :doc:`BeamContact3D`
#. :doc:`BeamEndContact3D`


.. toctree::
   :maxdepth: 2
   :hidden:

   SimpleContact2D
   SimpleContact3D
   BeamContact2D
   BeamContact3D
   BeamEndContact3D


Cable Elements
--------------

#. :doc:`CatenaryCable`

.. toctree::
   :maxdepth: 2
   :hidden:

   CatenaryCable


PFEM Elements
--------------

#. :doc:`PFEMElementBubble`
#. :doc:`PFEMElementCompressible`

.. toctree::
   :maxdepth: 2
   :hidden:

   PFEMElementBubble
   PFEMElementCompressible
      
Misc.
-----

#. :doc:`SurfaceLoad`
#. :doc:`VS3D4`
#. :doc:`AC3D8`
#. :doc:`ASI3D8`
#. :doc:`AV3D4`


.. toctree::
   :maxdepth: 2
   :hidden:

   SurfaceLoad
   VS3D4
   AC3D8
   ASI3D8
   AV3D4
