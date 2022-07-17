.. include:: sub.txt

===================
 eleLoad command
===================

.. function:: eleLoad('-ele', *eleTags, '-range', eleTag1, eleTag2, '-type', '-beamUniform', Wy, <Wz>, Wx=0.0, '-beamPoint',Py,<Pz>,xL,Px=0.0,'-beamThermal',*tempPts)

   The eleLoad command is used to construct an ElementalLoad object and add it to the enclosing LoadPattern.

   ========================   =============================================================
   ``eleTags`` |listi|        tag of PREVIOUSLY DEFINED element
   ``eleTag1`` |int|          element tag
   ``eleTag2`` |int|          element tag
   ``Wx`` |float|             mag of uniformily distributed ref load acting in direction
	                      along member length. (optional)
   ``Wy`` |float|             mag of uniformily distributed ref load acting in local y
	                      direction of element
   ``Wz`` |float|             mag of uniformily distributed ref load acting in local z
	                      direction of element. (required only for 3D)
   ``Px`` |float|             mag of ref point load acting in direction along member
	                      length. (optional)
   ``Py`` |float|             mag of ref point load acting in local y direction of element
   ``Pz`` |float|             mag of ref point load acting in local z direction of
	                      element. (required only for 3D)
   ``xL`` |float|             location of point load relative to node I,
	                      prescribed as fraction of element length
   ``tempPts`` |listf|        temperature points:
	                      ``temPts = [T1, y1, T2, y2, ..., T9, y9]``
			      Each point ``(T1, y1)`` define a temperature and
			      location. This command may accept 2,5 or 9
			      temperature points.
   ========================   =============================================================


.. note::


   #. The load values are reference load values, it is the time series that provides the load factor. The load factor times the reference values is the load that is actually applied to the element.
   #. At the moment, eleLoads do not work with 3D beam-column elements if Corotational geometric transformation is used.
