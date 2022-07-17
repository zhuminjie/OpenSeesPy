.. include:: sub.txt

.. _QuadMesh:
   
===========
 quad mesh
===========

.. function:: mesh('quad',tag,numlines,*ltags,id,ndf,meshsize,eleType='',*eleArgs=[])
   :noindex:

   Create a quad mesh object. The number of lines must be 4. These lines are continuous
   to form a loop.


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
			      * :doc:`ShellMITC4`

			      if no type is given, only nodes are created.
			      If beam elements are given, beams are created
			      instead of quad elements.
			      If triangular elements are given, they are created
			      by dividing one quad to two triangles.
			      
   ``eleArgs`` |list|         a list of element arguments. The arguments
                              are same as in the element commands, but without
			      element tag, and node tags. (optional)

			      For example,

			      ``eleArgs = ['PFEMElementBubble', rho, mu, b1, b2, thickness, kappa]``
   ========================   ===========================================================================

