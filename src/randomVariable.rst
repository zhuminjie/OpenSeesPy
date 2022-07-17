.. include:: sub.txt

========================
 randomVariable command
========================

.. function:: randomVariable(tag, dist, '-mean', mean, '-stdv', stdv, '-startPoint', startPoint, '-parameters', *params)

   Create a random variable with user specified distribution

   ========================   ===========================================================================
   ``tag`` |int|              random variable tag
   ``dist`` |str|             random variable distribution

	                      * ``'normal'``
			      * ``'lognormal'``
			      * ``'gamma'``
			      * ``'shiftedExponential'``
			      * ``'shiftedRayleigh'``
			      * ``'exponential'``
			      * ``'rayleigh'``
			      * ``'uniform'``
			      * ``'beta'``
			      * ``'type1LargestValue'``
			      * ``'type1SmallestValue'``
			      * ``'type2LargestValue'``
			      * ``'type3SmallestValue'``
			      * ``'chiSquare'``
			      * ``'gumbel'``
			      * ``'weibull'``
			      * ``'laplace'``
			      * ``'pareto'``
			      
   ``mean`` |float|           mean value
   ``stdv`` |float|           standard deviation
   ``startPoint`` |float|     starting point of the distribution
   ``params`` |listi|         a list of parameter tags
   ========================   ===========================================================================
