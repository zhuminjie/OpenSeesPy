.. include:: sub.txt

==========================================
 setElementRayleighDampingFactors command
==========================================

.. function:: setElementRayleighDampingFactors(eleTag,alphaM,betaK,betaK0,betaKc)

   Set the :func:`rayleigh` damping for an element.

   ========================   ===========================================================================
   ``eleTag`` |int|           element tag
   ``alphaM`` |float|         factor applied to elements or nodes mass matrix
   ``betaK`` |float|          factor applied to elements current stiffness matrix.
   ``betaK0`` |float|         factor applied to elements initial stiffness matrix.
   ``betaKc`` |float|         factor applied to elements committed stiffness matrix.
   ========================   ===========================================================================
