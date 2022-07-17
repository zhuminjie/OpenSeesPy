.. include:: sub.txt

===================
 Parallel Material
===================

.. function:: uniaxialMaterial('Parallel', matTag, *MatTags, '-factors', *factorArgs)
   :noindex:

   This command is used to construct a parallel material object made up of an arbitrary number of previously-constructed UniaxialMaterial objects.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``MatTags`` |listi|                   identification tags of materials making up the material model
   ``factorArgs`` |listf|                factors to create a linear combination of the
                                         specified materials. Factors can be negative to
					 subtract one material from an other. (optional, default = 1.0)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Parallel_Material>`_
