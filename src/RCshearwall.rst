.. include:: sub.txt

===============================================================
 Reinforced Concrete Shear Wall with Special Boundary Elements
===============================================================

#. The original code was written for OpenSees Tcl by `Lu X.Z. et al. (2015) <http://www.luxinzheng.net/download/OpenSEES/Examples_of_NLDKGQ_element.htm>`. 
#. The source code is converted to OpenSeesPy by `Anurag Upadhyay <https://github.com/anurag-upadhay>`_ from University of Utah.
#. Four node shell elements with LayeredShell sections are used to model the shear wall.
#. The source code is shown below, which can be downloaded :download:`here </pyExamples/RCshearwall.py>`.
#. Download the cyclic test load input and output files, :download:`RCshearwall_Load_input </pyExamples/RCshearwall_Load_input.txt>`, :download:`RCshearwall_TestOutput </pyExamples/RCshearwall_TestOutput.txt>`.
#. The details of the shear wall specimen are shown in the figure below, along with the finite element mesh.
#. Run the source code and you should see the cyclic test plot overlaid by a pushover curve, shown at the end.

.. image:: /_static/RCshearwall_Specimen-Mesh.png

.. literalinclude:: /pyExamples/RCshearwall.py
   :linenos:

.. image:: /_static/RCshearwall_PushoverCurve.png
