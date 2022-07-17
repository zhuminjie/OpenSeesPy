.. include:: sub.txt

====================
zeroLengthND Element
====================

.. function:: element('zeroLengthND', eleTag,*eleNodes,matTag, <uniTag>, <'-orient', *vecx, vecyp>)
   :noindex:

   This command is used to construct a zeroLengthND element object, which is defined by two nodes at the same location. The nodes are connected by a single NDMaterial object to represent the force-deformation relationship for the element.



   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``matTag`` |int|                      tag associated with previously-defined ndMaterial object
   ``uniTag`` |int|                      tag associated with previously-defined UniaxialMaterial object which may be used to represent uncoupled behavior orthogonal to the plane of the NDmaterial response. SEE NOTES 2 and 3.
   ``vecx`` |listf|                      a list of vector components in global coordinates defining local x-axis (optional)
   ``vecyp`` |listf|                     a list of vector components in global coordinates defining vector yp which lies in the local x-y plane for the element. (optional)
   ===================================   ===========================================================================


.. note::

   #. The zeroLengthND element only represents translational response between its nodes
   #. If the NDMaterial object is of order two, the response lies in the element local x-y plane and the UniaxialMaterial object may be used to represent the uncoupled behavior orthogonal to this plane, i.e. along the local z-axis.
   #. If the NDMaterial object is of order three, the response is along each of the element local exes.
   #. If the optional orientation vectors are not specified, the local element axes coincide with the global axes. Otherwise the local z-axis is defined by the cross product between the vectors x and yp vectors specified on the command line.
   #. The valid queries to a zero-length element when creating an ElementRecorder object are 'force', 'deformation', and 'material matArg1 matArg2 ...'

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthND_Element>`_
