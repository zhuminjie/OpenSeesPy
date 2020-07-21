.. include:: sub.txt

===============
 reset command
===============

.. function:: reset()

   This command is used to set the state of the domain to its original state.


.. note::

   It iterates over all components of the domain telling them to set their state back to the initial state. This is not always the same as going back to the state of the model after initial model generation, e.g. if elements have been removed.
