.. include:: sub.txt

===============
 Fiber Command
===============

.. function:: fiber(yloc, zloc, A, matTag)

   This command allows the user to construct a single fiber and add it to the enclosing FiberSection or NDFiberSection.

   ================================   ===========================================================================
   ``yloc`` |float|                   y coordinate of the fiber in the section (local coordinate system)
   ``zloc`` |float|                   z coordinate of the fiber in the section (local coordinate system)
   ``A`` |float|                      cross-sectional area of fiber
   ``matTag`` |int|                   material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection).
   ================================   ===========================================================================
