.. include:: sub.txt

.. _BgMesh:

=================
 background mesh
=================

.. function:: mesh('bg',basicsize,*lower,*upper,'-tol',tol,'-meshtol',meshtol,'-wave',wavefilename,numl,*locations,'-numsub',numsub,'-structure',id,numnodes,*snodes,'-largeSize',level,*llower,*lupper)
   :noindex:

   Create a background mesh. 


   ========================   ===========================================================================
   ``basicsize`` |float|      basic mesh size
   ``lower`` |listf|          a list of coordinates of the lower point of the background region.
   ``upper`` |listf|          a list of coordinates of the uuper point of the background region.
   ``tol`` |float|            tolerance for intri check. (optional, default 1e-10)
   ``meshtol`` |float|        tolerance for cell boundary check. (optional, default 0.1)
   ``wavefilename`` |str|     a filename to record wave heights and velocities (optional)
   ``numl`` |int|             number of locations to record wave (optional)
   ``locations`` |listf|      coordinates of the locations (optional)
   ``id`` |int|               structural id > 0, same meaning as :doc:`trimesh` (optional)
   ``numsnodes`` |int|        number of structural nodes (optional)
   ``sNodes`` |listi|         a list of structural nodes (optional)
   ``level`` |int|            some regions can have larger mesh size with larger ``level``.
                              ``level = 1`` means same as basic mesh size.
   ``llower`` |listf|         a list of coordinates of the lower point of the region with
                              larger mesh size (optional)
   ``lupper`` |listf|         a list of coordinates of the upper point of the region with
                              larger mesh size(optional)
   ========================   ===========================================================================
