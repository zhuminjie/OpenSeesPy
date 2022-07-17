.. include:: sub.txt

===================
 plot_line command
===================

.. function:: plot_line(x, y, label='', color='rgb(0,0,255)', bgColor='white', lineWidth=2, lineStyle='solid', fill=False, pointStyle='circle', pointSize=5, pointColor='', pointBgColor='white', lineTension=0.0)

   This command is used to add a line in the :doc:`PlotModule`.

   ========================   ===================================================================================
   ``x`` |listf|              a list of x values
   ``y`` |listf|              a list of y values
   ``label`` |str|            the label name for the line in the legend
   ``color`` |str|            the color for the line, the value could be:

	                      - rgb values as ``'rgb(r,g,b)'`` betwen ``[0, 255]``.
			      - a color name such as ``'white'``, ``'black'``, ``'blue'``, etc.
   ``bgColor`` |str|          the color for filling the area below the line, if ``fill`` is set to ``True``.
   ``lineWidth`` |int|        the line width
   ``lineStyle`` |str|        the line style, valid values include:

	                      - ``'solid'``
			      - ``'dotted'``
			      - ``'dashed'``
			      - ``'long-dashed'``
			      - ``'dashed-dotted'``
			      - ``'dashed-dotted-dotted'``
			      - ``'dotted-dashed-dotted'``
   ``fill`` |bool|            whether to fill the area below the line
   ``pointStyle`` |str|       the point style, valid values include:

	                      - ``'circle'``
			      - ``'cross'``
			      - ``'crossRot'``
			      - ``'dash'``
			      - ``'line'``
			      - ``'rect'``
			      - ``'rectRounded'``
			      - ``'rectRot'``
			      - ``'star'``
			      - ``'triangle'``
   ``pointSize`` |int|        the point size
   ``pointColor`` |str|       the point border color, if = ``''``, the line color is used
   ``pointBgColor`` |str|     the point fill color
   ``lineTension`` |float|    if ``0.0``, straight lines are drawn, otherwise, Bezier curves are drawn.
   ========================   ===================================================================================

