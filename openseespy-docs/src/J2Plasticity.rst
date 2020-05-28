.. include:: sub.txt

==================
 J2Plasticity
==================

.. function:: nDMaterial('J2Plasticity', matTag, K, G, sig0, sigInf, delta, H)
   :noindex:

   This command is used to construct an multi dimensional material object that has a von Mises (J2) yield criterium and isotropic hardening.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``K`` |float|                      bulk modulus
   ``G`` |float|                      shear modulus
   ``sig0`` |float|                   initial yield stress
   ``sigInf`` |float|                 final saturation yield stress
   ``delta`` |float|                  exponential hardening parameter
   ``H`` |float|                      linear hardening parameter
   ================================   ===========================================================================

The material formulations for the J2Plasticity object are:

* ``'ThreeDimensional'``
* ``'PlaneStrain'``
* ``'Plane Stress'``
* ``'AxiSymmetric'``
* ``'PlateFiber'``

J2 isotropic hardening material class

Elastic Model

.. math::

   \sigma = K * trace(\epsilon_e) + (2 * G) * dev(\epsilon_e)

Yield Function

.. math::

   \phi(\sigma,q) = || dev(\sigma) ||  - \sqrt(\tfrac{2}{3}*q(x_i))

Saturation Isotropic Hardening with linear term

.. math::

 q(x_i) = \sigma_0 + (\sigma_\infty - \sigma_0)*exp(-delta*\xi) + H*\xi

Flow Rules

.. math::

 \dot {\epsilon_p} =  \gamma * \frac{\partial \phi}{\partial \sigma}

 \dot \xi  = -\gamma * \frac{\partial \phi}{\partial q}

Linear Viscosity

.. math::
   \gamma = \frac{\phi}{\eta}  ( if   \phi > 0 )

Backward Euler Integration Routine Yield condition enforced at time n+1

set :math:`\eta` = 0 for rate independent case
