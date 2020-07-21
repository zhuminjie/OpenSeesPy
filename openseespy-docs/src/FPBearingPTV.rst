.. include:: sub.txt

============
FPBearingPTV
============

The FPBearingPTV command creates a single Friction Pendulum bearing element, which is capable of accounting for the changes in the coefficient of friction at the sliding surface with instantaneous values of the sliding velocity, axial pressure and temperature at the sliding surface. The constitutive modelling is similar to the existing singleFPBearing element, otherwise. The FPBearingPTV element has been verified and validated in accordance with the ASME guidelines, details of which are presented in Chapter 4 of Kumar et al. (2015a).



.. function:: element('FPBearingPTV', eleTag,*eleNodes,MuRef, IsPressureDependent, pRef, IsTemperatureDependent, Diffusivity, Conductivity, IsVelocityDependent, rateParameter, ReffectiveFP, Radius_Contact, kInitial, theMaterialA, theMaterialB, theMaterialC, theMaterialD, x1, x2, x3, y1, y2, y3, shearDist, doRayleigh, mass, iter, tol, unit)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``MuRef`` |float|                     Reference coefficient of friction
   ``IsPressureDependent`` |int|         1 if the coefficient of friction is a function of instantaneous axial pressure
   ``pRef`` |float|                      Reference axial pressure (the bearing pressure under static loads)
   ``IsTemperatureDependent`` |int|      1 if the coefficient of friction is a function of instantaneous temperature at the sliding surface
   ``Diffusivity`` |float|               Thermal diffusivity of steel
   ``Conductivity`` |float|              Thermal conductivity of steel
   ``IsVelocityDependent`` |int|         1 if the coefficient of friction is a function of instantaneous velocity at the sliding surface
   ``rateParameter`` |float|             The exponent that determines the shape of the coefficient of friction vs. sliding velocity curve
   ``ReffectiveFP`` |float|              Effective radius of curvature of the sliding surface of the FPbearing
   ``Radius_Contact`` |float|            Radius of contact area at the sliding surface
   ``kInitial`` |float|                  Lateral  stiffness of the sliding bearing before sliding begins
   ``theMaterialA`` |int|                Tag for the uniaxial material in the axial direction
   ``theMaterialB`` |int|                Tag for the uniaxial material in the torsional direction
   ``theMaterialC`` |int|                Tag for the uniaxial material for rocking about local Y axis
   ``theMaterialD`` |int|                Tag for the uniaxial material for rocking about local Z axis
   ``x1``  ``x2``  ``x3`` |float|        Vector components to define local X axis
   ``y1``  ``y2``  ``y3`` |float|        Vector components to define local Y axis
   ``shearDist`` |float|                 Shear distance from iNode as a fraction of the length of the element
   ``doRayleigh`` |int|                  To include Rayleigh damping from the bearing
   ``mass`` |float|                      Element mass
   ``iter`` |int|                        Maximum number of iterations to satisfy the equilibrium of element
   ``tol`` |float|                       Convergence tolerance to satisfy the equilibrium of the element
   ``unit`` |int|                        Tag to identify the unit from the list below.

                                         * ``1``: N, m, s, C
					 * ``2``: kN, m, s, C
					 * ``3``: N, mm, s, C
					 * ``4``: kN, mm, s, C
					 * ``5``: lb, in, s, C
					 * ``6``: kip, in, s, C
					 * ``7``: lb, ft, s, C
					 * ``8``: kip, ft, s, C
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/FPBearingPTV>`_
