.. include:: sub.txt

=========================
 Preprocessing Commands
=========================

The :doc:`mesh` and :doc:`remesh` should be 
called as

::

    import openseespy.opensees as ops
    ops.mesh()
    ops.remesh()

The :doc:`DiscretizeMember` should be called as 

::

    import openseespy.preprocessing.DiscretizeMember as opsdm

    opsdm.DiscretizeMember()

#. :doc:`mesh`
#. :doc:`remesh`
#. :doc:`DiscretizeMember`

.. toctree::
    :maxdepth: 1
    :hidden:

    DiscretizeMember



