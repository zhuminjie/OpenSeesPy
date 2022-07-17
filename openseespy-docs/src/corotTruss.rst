.. include:: sub.txt

==========================
Corotational Truss Element
==========================

This command is used to construct a corotational truss element object. There are two ways to construct a corotational truss element object:

.. function:: element('corotTruss', eleTag,*eleNodes,A, matTag, <'-rho', rho>,<'-cMass', cFlag>,<'-doRayleigh', rFlag>)
   :noindex:

   One way is to specify an area and a UniaxialMaterial identifier:


.. function:: element('corotTrussSection', eleTag,*eleNodes, secTag, <'-rho', rho>,<'-cMass', cFlag>,<'-doRayleigh', rFlag>)
   :noindex:

   the other is to specify a Section identifier:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``A`` |float|                         cross-sectional area of element
   ``matTag`` |int|                      tag associated with previously-defined UniaxialMaterial
   ``secTag`` |int|                      tag associated with previously-defined Section
   ``rho`` |float|                       mass per unit length, optional, default = 0.0
   ``cFlag`` |float|                     consistent mass flag, optional, default = 0

                                         * ``cFlag`` = 0 lumped mass matrix (default)
					 * ``cFlag`` = 1 consistent mass matrix
   ``rFlag`` |float|                     Rayleigh damping flag, optional, default = 0

                                         * ``rFlag`` = 0 NO RAYLEIGH DAMPING (default)
					 * ``rFlag`` = 1 include Rayleigh damping
   ===================================   ===========================================================================


.. note::

   #. When constructed with a UniaxialMaterial object, the corotational truss element considers strain-rate effects, and is thus suitable for use as a damping element.
   #. The valid queries to a truss element when creating an ElementRecorder object are 'axialForce,' 'stiff,' deformations,' 'material matArg1 matArg2...,' 'section sectArg1 sectArg2...' There will be more queries after the interface for the methods involved have been developed further.
   #. CorotTruss DOES NOT include Rayleigh damping by default.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Corotational_Truss_Element>`_
