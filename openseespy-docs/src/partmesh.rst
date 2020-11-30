.. include:: sub.txt

===============
 particle mesh
===============

.. function:: mesh('part',tag,type,*pArgs,eleType='',*eleArgs=[], '-vel', *vel0, '-pressure', p0)
   :noindex:

   Create or return a group of particles which will be used for background mesh.


   ========================     ==========================================================================================
   ``tag`` |int|                mesh tag.
   ``type`` |str|               type of the mesh
   ``pArgs`` |listf|            coordinates of points defining the mesh region
				``nx``, ``ny``, ``nz`` are number of particles in x, y,
				and z directions
		

				* ``'quad'`` : [x1, y1, x2, y2, x3, y3, x4, y4, nx, ny]
					
				  Coordinates of four corners in counter-clock wise order.
					
				* ``'cube'`` : [x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4,
						z4, x5, y5, z5, x6, y6, z6, x7, y7, z7, x8,
						y8, z8, nx, ny, nz]
					
				  Coordinates of four corners at bottom and at top in
				  counter-clock wise order
				
				* ``'tri'`` : [x1, y1, x2, y2, x3, y3, nx, ny]
					
				  Coordinates of three corners in counter-clock wise order

				* ``'line'`` : [x1, y1, x2, y2, nx]
			      
				  Coordinates of two ends in counter-clock wise order
				
                                * ``'pointlist'`` : [x1, y1, <z1>, vx1, vy1, <vz1>,
				                     ax1, ay1, <az1>, p1, 
						     x2, y2, <z2>, vx2, vy2, <vz2>,
						     ax2, ay2, <az2>, p2, ..]
			      
				  input particles' data in a list, in the order of coordinates
				  of last time step, current coordinates, velocity, acceleration,
				  and pressure.

				* ``'pointlist'`` without list

				  return a list of current particles' data in this mesh

				  [tag1, x1, y1, <z1>, vx1, vy1, <vz1>,
				  ax1, ay1, <az1>, p1,
				  tag2, x2, y2, <z2>, vx2, vy2, <vz2>,
				  ax2, ay2, <az2>, p2,
				  ..]

				  The format is similar to the input list, but with an
				  additional tag for each particle.

			      
   ``eleType`` |str|            the element type, (optional)

                                * :doc:`PFEMElementBubble`
				* :doc:`PFEMElementCompressible`
				* :doc:`tri31`

				  if no type is given, only nodes are created
			      
   ``eleArgs`` |list|           a list of element arguments.
                                (optional, see :doc:`linemesh` and :doc:`trimesh`)
   ``vel0`` |listf|             a list of initial velocities. (optional)
   ``p0`` |float|               initial pressure. (optional)
   ========================     ==========================================================================================

