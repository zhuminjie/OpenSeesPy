.. include:: sub.txt

===============
 Patch Command
===============

.. function:: patch(type, *args)

   The patch command is used to generate a number of fibers over a cross-sectional area. Currently there are three types of cross-section that fibers can be generated: quadrilateral, rectangular and circular.




.. function:: patch('quad', matTag,numSubdivIJ,numSubdivJK,*crdsI,*crdsJ,*crdsK,*crdsL)
   :noindex:

   This is the command to generate a quadrilateral shaped patch (the geometry of the patch is defined by four vertices: I J K L. The coordinates of each of the four vertices is specified in COUNTER CLOCKWISE sequence)

   ================================   ===========================================================================
   ``matTag`` |int|                   material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection).
   ``numSubdivIJ`` |int|              number of subdivisions (fibers) in the IJ direction.
   ``numSubdivJK`` |int|              number of subdivisions (fibers) in the JK direction.
   ``crdsI`` |listf|                  y & z-coordinates of vertex I (local coordinate system)
   ``crdsJ`` |listf|                  y & z-coordinates of vertex J (local coordinate system)
   ``crdsK`` |listf|                  y & z-coordinates of vertex K (local coordinate system)
   ``crdsL`` |listf|                  y & z-coordinates of vertex L (local coordinate system)
   ================================   ===========================================================================


.. function:: patch('rect', matTag,numSubdivY,numSubdivZ,*crdsI,*crdsJ)
   :noindex:

   This is the command to generate a rectangular patch. The geometry of the patch is defined by coordinates of vertices: I and J. The first vertex, I, is the bottom-left point and the second vertex, J, is the top-right point, having as a reference the local y-z plane.

   ================================   ===========================================================================
   ``matTag`` |int|                   material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection).
   ``numSubdivY`` |int|               number of subdivisions (fibers) in local y direction.
   ``numSubdivZ`` |int|               number of subdivisions (fibers) in local z direction.
   ``crdsI`` |listf|                  y & z-coordinates of vertex I (local coordinate system)
   ``crdsJ`` |listf|                  y & z-coordinates of vertex J (local coordinate system)
   ================================   ===========================================================================


.. function:: patch('circ', matTag,numSubdivCirc,numSubdivRad,*center,*rad,*ang)
   :noindex:

   This is the command to generate a circular shaped patch

   ================================   ===========================================================================
   ``matTag`` |int|                   material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection).
   ``numSubdivCirc`` |int|            number of subdivisions (fibers) in the circumferential direction (number of wedges)
   ``numSubdivRad`` |int|             number of subdivisions (fibers) in the radial direction (number of rings)
   ``center`` |listf|                 y & z-coordinates of the center of the circle
   ``rad`` |listf|                    internal & external radius
   ``ang`` |listf|                    starting & ending-coordinates angles (degrees)
   ================================   ===========================================================================
