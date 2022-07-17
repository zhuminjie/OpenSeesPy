.. include:: sub.txt

==========================
 Portal Frame 2d Analysis
==========================


#. The source code is shown below, which can be downloaded :download:`here </pyExamples/PortalFrame2d.py>`.
#. Run the source code in your favorite Python program and should see results below

::

   Period Comparisons:
    Period       OpenSees        SAP2000   SeismoStruct
         1        1.27321         1.2732         1.2732
         2        0.43128         0.4313         0.4313
         3        0.24204         0.2420         0.2420
         4        0.16018         0.1602         0.1602
         5        0.11899         0.1190         0.1190
         6        0.09506         0.0951         0.0951
         7        0.07951         0.0795         0.0795


    tSatic Analysis Result Comparisons:
                     Parameter       OpenSees        SAP2000   SeismoStruct
                      Disp Top          1.451           1.45           1.45
       Axial Force Bottom Left         69.987          69.99          70.01
            Moment Bottom Left       2324.677        2324.68        2324.71
    PASSED Verification Test PortalFrame2d.py 

.. literalinclude:: /pyExamples/PortalFrame2d.py
   :linenos:
