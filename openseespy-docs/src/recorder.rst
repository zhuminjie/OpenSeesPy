.. include:: sub.txt

================
recorder command
================

.. function:: recorder(recorderType, *recorderArgs)

   This command is used to generate a recorder object which is to monitor what is happening during the analysis and generate output for the user.
   
   Return:

   * >0 an integer tag that can be used as a handle on the recorder for the remove recorder commmand.
   * -1 recorder command failed if integer -1 returned.

   ================================   ===========================================================================
   ``recorderType`` |str|             recorder type
   ``recorderArgs`` |list|            a list of recorder arguments
   ================================   ===========================================================================

The following contain information about available ``recorderType``:

.. toctree::
   :maxdepth: 2

   nodeRecorder
   nodeEnRecorder
   elementRecorder
   elementEnRecorder
   pvdRecorder
   bgpvdRecorder
   CollapseRecorder
