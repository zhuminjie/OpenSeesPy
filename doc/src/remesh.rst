.. include:: sub.txt

.. _ReMesh:

================
 remesh command
================

.. function:: remesh(alpha=-1.0)

   * :math:`\alpha \ge 0` for updating moving mesh.
   * :math:`\alpha < 0` for updating background mesh.

   If there are nodes shared by different mesh in the domain,
   the principles to decide what element should be used for
   a triangle:

   #. If all 3 nodes share the same mesh, use that mesh for the triangle.
   #. If all 3 nodes share more than one mesh, use the mesh with ``eleArgs`` defined
      and lowest ``id``.
   #. If all 3 nodes are in different mesh, use the mesh with lowest ``id``.
   #. If the selected mesh ``id`` >= 0, skip the triangle.
   #. If the selected mesh has no ``eleArgs``, skip the triangle.




   ========================   ===========================================================================
   ``alpha`` |float|          Parameter for the :math:`\alpha` method to construct a mesh
	                      from the node cloud of moving meshes. (optional)

			      * :math:`\alpha = 0` : no elements are created
			      * large :math:`\alpha` : all elements in the convex hull are created
			      * :math:`1.0 < \alpha < 2.0` : usually gives a good shape
   ========================   ===========================================================================
