.. include:: sub.txt

=================
 block3D command
=================

.. function:: block3D(numX, numY, numZ, startNode, startEle, eleType, *eleArgs, *crds)

   Create mesh of quadrilateral elements

   ========================   ===========================================================================
   ``numX`` |int|             number of elements in local x directions of the block.
   ``numY`` |int|             number of elements in local y directions of the block.
   ``numZ`` |int|             number of elements in local z directions of the block.
   ``startNode`` |int|        node from which the mesh generation will start.
   ``startEle`` |int|         element from which the mesh generation will start.
   ``eleType`` |str|          element type (``'stdBrick'``, ``'bbarBrick'``, ``'Brick20N'``)
   ``eleArgs`` |list|         a list of element parameters.
   ``crds`` |list|            coordinates of the block elements with the format:
	      
	                      [1, x1, y1, z1,
   
			      2, x2, y2, z2,
			      
			      3, x3, y3, z3,
			      
			      4, x4, y4, z4,
   
			      5, x5, y5, z5,
   
			      6, x6, y6, z6,
   
			      7, x7, y7, z7,
   
			      8, x8, y8, z8,
   
			      9, x9, y9, z9,
   
			      <10>, <x10>, <y10>, <z10>,
   
			      <11>, <x11>, <y11>, <z11>,
   
			      <12>, <x12>, <y12>, <z12>,
   
			      <13>, <x13>, <y13>, <z13>,
   
			      <14>, <x14>, <y14>, <z14>,
   
			      <15>, <x15>, <y15>, <z15>,
   
			      <16>, <x16>, <y16>, <z16>,
   
			      <17>, <x17>, <y17>, <z17>,
   
			      <18>, <x18>, <y18>, <z18>,
   
			      <19>, <x19>, <y19>, <z19>,
   
			      <20>, <x20>, <y20>, <z20>,
   
			      <21>, <x21>, <y21>, <z21>,
   
			      <22>, <x22>, <y22>, <z22>,
   
			      <23>, <x23>, <y23>, <z23>,
   
			      <24>, <x24>, <y24>, <z24>,
   
			      <25>, <x25>, <y25>, <z25>,
   
			      <26>, <x26>, <y26>, <z26>,
   
			      <27>, <x27>, <y27>, <z27>]

			      <> means optional
   ========================   ===========================================================================

