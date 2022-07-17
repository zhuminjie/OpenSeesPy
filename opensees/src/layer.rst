.. include:: sub.txt

===============
 Layer Command
===============

.. function:: layer(type, *args)

   The layer command is used to generate a number of fibers along a line or a circular arc.

.. function:: layer('straight', matTag,numFiber,areaFiber,*start,*end)
   :noindex:

   This command is used to construct a straight line of fibers

   ================================   ===========================================================================
   ``matTag`` |int|                   material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection).
   ``numFiber`` |int|                 number of fibers along line
   ``areaFiber`` |float|              area of each fiber
   ``start`` |listf|                  y & z-coordinates of first fiber in line (local coordinate system)
   ``end`` |listf|                    y & z-coordinates of last fiber in line (local coordinate system)
   ================================   ===========================================================================


.. function:: layer('circ', matTag,numFiber,areaFiber,*center,radius,*ang=[0.0,360.0-360/numFiber])
   :noindex:

   This command is used to construct a line of fibers along a circular arc

   ================================   ===========================================================================
   ``matTag`` |int|                   material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection).
   ``numFiber`` |int|                 number of fibers along line
   ``areaFiber`` |float|              area of each fiber
   ``center`` |listf|                 y & z-coordinates of center of circular arc
   ``radius`` |float|                 radius of circlular arc
   ``ang`` |listf|                    starting and ending angle (optional)
   ================================   ===========================================================================
