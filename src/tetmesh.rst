.. include:: sub.txt

.. _TetMesh:
   
==================
 tetrahedron mesh
==================

.. function:: mesh('tet',tag,nummesh,*mtags,id,ndf,meshsize,eleType='',*eleArgs=[])
   :noindex:

   Create a 3D tetrahedron mesh object.


   ========================   ===========================================================================
   ``tag`` |int|              mesh tag.
   ``nummesh`` |int|          number of 2D mesh for defining a 3D body.
   ``mtags`` |listi|          the mesh tags
   ``id`` |int|               mesh id. Meshes with same id are considered as same structure
                              of fluid identity.

                              * ``id`` = 0 : not in FSI
			      * ``id`` > 0 : structure
			      * ``id`` < 0 : fluid
   ``ndf`` |int|              ndf for nodes to be created.
   ``meshsize`` |float|       mesh size.
   ``eleType`` |str|          the element type, (optional)

                              * :doc:`FourNodeTetrahedron`

			      if no type is given, only nodes are created.

			      
   ``eleArgs`` |list|         a list of element arguments. The arguments
                              are same as in the element commands, but without
			      element tag, and node tags. (optional)

   ========================   ===========================================================================

