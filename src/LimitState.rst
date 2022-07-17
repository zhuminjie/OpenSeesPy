.. include:: sub.txt

====================
Limit State Material
====================

.. function:: uniaxialMaterial('LimitState', matTag, s1p, e1p, s2p, e2p, s3p, e3p, s1n, e1n, s2n, e2n, s3n, e3n, pinchX, pinchY, damage1, damage2, beta, curveTag, curveType)
   :noindex:

   This command is used to construct a uniaxial hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility. Failure of the material is defined by the associated Limit Curve.


   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``s1p``  ``e1p`` |float|              stress and strain (or force & deformation) at first point of the envelope in the positive direction
   ``s2p``  ``e2p`` |float|              stress and strain (or force & deformation) at second point of the envelope in the positive direction
   ``s3p``  ``e3p`` |float|              stress and strain (or force & deformation) at third point of the envelope in the positive direction
   ``s1n``  ``e1n`` |float|              stress and strain (or force & deformation) at first point of the envelope in the negative direction
   ``s2n``  ``e2n`` |float|              stress and strain (or force & deformation) at second point of the envelope in the negative direction
   ``s3n``  ``e3n`` |float|              stress and strain (or force & deformation) at third point of the envelope in the negative direction
   ``pinchX`` |float|                    pinching factor for strain (or deformation) during reloading
   ``pinchY`` |float|                    pinching factor for stress (or force) during reloading
   ``damage1`` |float|                   damage due to ductility: D1(m-1)
   ``damage2`` |float|                   damage due to energy: D2(Ei/Eult)
   ``beta`` |float|                      power used to determine the degraded unloading stiffness based on ductility, m-b (optional, default=0.0)
   ``curveTag`` |int|                    an integer tag for the Limit Curve defining the limit surface
   ``curveType`` |int|                   an integer defining the type of LimitCurve (0 = no curve, 1 = axial curve, all other curves can be any other integer)
   ===================================   ===========================================================================

.. note::

   * negative backbone points should be entered as negative numeric values

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Limit_State_Material>`_
