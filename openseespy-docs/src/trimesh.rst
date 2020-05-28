.. include:: sub.txt

.. _TriMesh:
   
=================
 triangular mesh
=================

.. function:: mesh('tri',tag,numlines,*ltags,id,ndf,meshsize,eleType='',*eleArgs=[])
   :noindex:

   Create a triangular mesh object.


   ========================   ===========================================================================
   ``tag`` |int|              mesh tag.
   ``numlines`` |int|         number of lines (:ref:`LineMesh`) for defining a polygon.
   ``ltags`` |listi|          the :ref:`LineMesh` tags
   ``id`` |int|               mesh id. Meshes with same id are considered as same structure
                              of fluid identity.

                              * ``id`` = 0 : not in FSI
			      * ``id`` > 0 : structure
			      * ``id`` < 0 : fluid
   ``ndf`` |int|              ndf for nodes to be created.
   ``meshsize`` |float|       mesh size.
   ``eleType`` |str|          the element type, (optional)

                              * :doc:`PFEMElementBubble`
			      * :doc:`PFEMElementCompressible`
			      * :doc:`tri31`
			      * :doc:`elasticBeamColumn`
			      * :doc:`ForceBeamColumn`
			      * :doc:`dispBeamColumn`

			      if no type is given, only nodes are created.
			      if beam elements are given, beams are created
			      instead of triangular elements.
			      
   ``eleArgs`` |list|         a list of element arguments. The arguments
                              are same as in the element commands, but without
			      element tag, and node tags. (optional)

			      For example,

			      ``eleArgs = ['PFEMElementBubble', rho, mu, b1, b2, thickness, kappa]``
   ========================   ===========================================================================

