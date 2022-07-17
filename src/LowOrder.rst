.. include:: sub.txt

==========
 LowOrder
==========

.. function:: beamIntegration('LowOrder',tag,N,*secTags,*locs,*wts)
   :noindex:

   Create a LowOrder beamIntegration object.
   This option is a generalization of the :ref:`FixedLocation-BeamIntegration` and :ref:`UserDefined-BeamIntegration` integration approaches and is useful for moving load analysis (`Kidarsa, Scott and Higgins 2008`_). The locations of the integration points are user defined,
   while a selected number of weights are specified and the remaining weights are
   computed by the method of undetermined coefficients.

   .. math::

      \sum_{i=1}^{N_f}x_{fi}^{j-1}w_{fi}=\frac{1}{j}-\sum_{i=1}^{N_c}x_{ci}^{j-1}w_{ci}

   Note that :ref:`FixedLocation-BeamIntegration` integration is recovered when ``Nc`` is zero.

   ========================   =============================================================
   ``tag`` |int|              tag of the beam integration
   ``N`` |int|                number of integration points along the element.
   ``secTags`` |listi|        A list previous-defined section objects.
   ``locs`` |listf|           Locations of integration points along the element.
   ``wts`` |listf|            weights of integration points.
   ========================   =============================================================



   ::

      locs = [0.0, 0.2, 0.5, 0.8, 1.0]
      wts = [0.2, 0.2]
      secs = [1, 2, 2, 2, 1]
      beamIntegration('LowOrder',1,len(secs),*secs,*locs,*wts)

   Places ``N`` integration points along the element, which are defined in ``locs``.
   on the natural domain [0, 1]. The force-deformation response at each integration point is
   defined by the ``secs``. Both the ``locs`` and ``secs``
   should be of length ``N``. The ``wts`` at user-selected integration
   points are specified on [0, 1],
   which can be of length ``Nc`` equals ``0`` up to ``N``. These specified weights
   are assigned to the first ``Nc`` entries in the ``locs`` and ``secs``, respectively. The
   order of accuracy for Low Order integration is N-Nc-1.

   .. note::

      ``Nc`` is determined from the length of the ``wts`` list. Accordingly,
      :ref:`FixedLocation-BeamIntegration`
      integration is recovered when ``wts`` is an empty list and
      :ref:`UserDefined-BeamIntegration` integration is
      recovered when the ``wts`` and ``locs`` lists are of equal length.




