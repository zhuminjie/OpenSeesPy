# OpenSeesPy visualization module

# Copyright (C) 2020 Seweryn Kokot
# Faculty of Civil Engineering and Architecture
# Opole University of Technology, Poland
# ver. 0.95, 2020 September
# License: GNU GPL version 3

# plot_fiber_section is inspired by plotSection matlab function
# written by D. Vamvatsikos available at
# http://users.ntua.gr/divamva/software.html (plotSection.zip)

# Notes:

# 1. matplotlib's plt.axis('equal') does not work for 3d plots
#    therefore right angles are not guaranteed to be 90 degrees on the
#    plots

import openseespy.opensees as ops  # installed from pip
# import opensees as ops  # local compilation
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import Circle, Polygon, Wedge
from matplotlib.animation import FuncAnimation
import matplotlib.tri as tri

# default settings

# fmt: format string setting color, marker and linestyle
# check documentation on matplotlib's plot

# continuous interpolated shape line
fmt_interp = 'b-'  # blue solid line, no markers

# element end nodes
fmt_nodes = 'rs'  # red square markers, no line

# deformed model
fmt_defo = 'b-'  # green dashed line, no markers

# undeformed model
fmt_undefo = 'g:'  # green dotted line, no markers

# section forces
fmt_secforce = 'b-'  # blue solid line

# figure left right bottom top offsets
fig_lbrt = (.04, .04, .96, .96)

# azimuth and elevation in degrees
az_el = (-60., 30.)

# figure width and height in centimeters
fig_wi_he = (16., 10.)


def _plot_model_2d(node_labels, element_labels, offset_nd_label, axis_off,
                   fig_wi_he, fig_lbrt):

    fig_wi, fig_he = fig_wi_he
    fleft, fbottom, fright, ftop = fig_lbrt

    fig = plt.figure(figsize=(fig_wi/2.54, fig_he/2.54))
    fig.subplots_adjust(left=.08, bottom=.08, right=.985, top=.94)

    max_x_crd, max_y_crd, max_crd = -np.inf, -np.inf, -np.inf

    node_tags = ops.getNodeTags()
    ele_tags = ops.getEleTags()

    nen = np.shape(ops.eleNodes(ele_tags[0]))[0]

    # truss and beam/frame elements plot_model
    if nen == 2:

        for node_tag in node_tags:
            x_crd = ops.nodeCoord(node_tag)[0]
            y_crd = ops.nodeCoord(node_tag)[1]
            if x_crd > max_x_crd:
                max_x_crd = x_crd
            if y_crd > max_y_crd:
                max_y_crd = y_crd

        max_crd = np.amax([max_x_crd, max_y_crd])
        _offset = 0.005 * max_crd

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2 = ops.eleNodes(ele_tag)

            # element node1-node2, x,  y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0], ops.nodeCoord(nd2)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1], ops.nodeCoord(nd2)[1]])

            # location of label
            xt = sum(ex)/nen
            yt = sum(ey)/nen

            plt.plot(ex, ey, 'bo-')

            if element_labels:
                if ex[1]-ex[0] == 0:
                    va = 'center'
                    ha = 'left'
                    offset_x, offset_y = _offset, 0.0
                elif ey[1]-ey[0] == 0:
                    va = 'bottom'
                    ha = 'center'
                    offset_x, offset_y = 0.0, _offset
                else:
                    va = 'bottom'
                    ha = 'left'
                    offset_x, offset_y = 0.03, 0.03

                plt.text(xt+offset_x, yt+offset_y, f'{ele_tag}', va=va, ha=ha,
                         color='red')

        if node_labels:
            for node_tag in node_tags:
                if not offset_nd_label == 'above':
                    offset_nd_label_x, offset_nd_label_y = _offset, _offset
                    va = 'bottom'
                    ha = 'left'
                else:
                    offset_nd_label_x, offset_nd_label_y = 0.0, _offset
                    va = 'bottom'
                    ha = 'center'

                plt.text(ops.nodeCoord(node_tag)[0]+offset_nd_label_x,
                         ops.nodeCoord(node_tag)[1]+offset_nd_label_y,
                         f'{node_tag}', va=va, ha=ha, color='blue')

        # plt.axis('equal')

    # 2d triangular (tri31) elements plot_model
    elif nen == 3:

        for node_tag in node_tags:
            x_crd = ops.nodeCoord(node_tag)[0]
            y_crd = ops.nodeCoord(node_tag)[1]
            if x_crd > max_x_crd:
                max_x_crd = x_crd
            if y_crd > max_y_crd:
                max_y_crd = y_crd

        max_crd = np.amax([max_x_crd, max_y_crd])
        _offset = 0.005 * max_crd
        _offnl = 0.003 * max_crd

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1]])

            # location of label
            xt = sum(ex)/nen
            yt = sum(ey)/nen

            plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]), 'bo-', ms=2)

            if element_labels:
                va = 'center'
                ha = 'center'
                plt.text(xt, yt, f'{ele_tag}', va=va, ha=ha, color='red')

        if node_labels:
            for node_tag in node_tags:
                if not offset_nd_label == 'above':
                    offset_nd_label_x, offset_nd_label_y = _offnl, _offnl
                    va = 'bottom'
                    # va = 'center'
                    ha = 'left'
                else:
                    offset_nd_label_x, offset_nd_label_y = 0.0, _offnl
                    va = 'bottom'
                    ha = 'center'

                plt.text(ops.nodeCoord(node_tag)[0]+offset_nd_label_x,
                         ops.nodeCoord(node_tag)[1]+offset_nd_label_y,
                         f'{node_tag}', va=va, ha=ha, color='blue')

    # 2d quadrilateral (quad) elements plot_model
    elif nen == 4:

        for node_tag in node_tags:
            x_crd = ops.nodeCoord(node_tag)[0]
            y_crd = ops.nodeCoord(node_tag)[1]
            if x_crd > max_x_crd:
                max_x_crd = x_crd
            if y_crd > max_y_crd:
                max_y_crd = y_crd

        max_crd = np.amax([max_x_crd, max_y_crd])
        _offset = 0.005 * max_crd
        _offnl = 0.003 * max_crd

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1]])

            # location of label
            xt = sum(ex)/nen
            yt = sum(ey)/nen

            # plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]), 'bo-')
            plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]), 'b-', lw=0.4,
                     ms=2)

            if element_labels:
                va = 'center'
                ha = 'center'
                plt.text(xt, yt, f'{ele_tag}', va=va, ha=ha, color='red')

        if node_labels:
            for node_tag in node_tags:
                if not offset_nd_label == 'above':
                    offset_nd_label_x, offset_nd_label_y = _offnl, _offnl
                    va = 'bottom'
                    # va = 'center'
                    ha = 'left'
                else:
                    offset_nd_label_x, offset_nd_label_y = 0.0, _offnl
                    va = 'bottom'
                    ha = 'center'

                plt.text(ops.nodeCoord(node_tag)[0]+offset_nd_label_x,
                         ops.nodeCoord(node_tag)[1]+offset_nd_label_y,
                         f'{node_tag}', va=va, ha=ha, color='blue')

        plt.axis('equal')

    # 2d quadrilateral (quad8n) elements plot_model
    elif nen == 8:

        for node_tag in node_tags:
            x_crd = ops.nodeCoord(node_tag)[0]
            y_crd = ops.nodeCoord(node_tag)[1]
            if x_crd > max_x_crd:
                max_x_crd = x_crd
            if y_crd > max_y_crd:
                max_y_crd = y_crd

        max_crd = np.amax([max_x_crd, max_y_crd])
        _offset = 0.005 * max_crd
        _offnl = 0.003 * max_crd

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6, nd7, nd8 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0],
                           ops.nodeCoord(nd5)[0],
                           ops.nodeCoord(nd6)[0],
                           ops.nodeCoord(nd7)[0],
                           ops.nodeCoord(nd8)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1],
                           ops.nodeCoord(nd5)[1],
                           ops.nodeCoord(nd6)[1],
                           ops.nodeCoord(nd7)[1],
                           ops.nodeCoord(nd8)[1]])

            # location of label
            xt = sum(ex)/nen
            yt = sum(ey)/nen

            # plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]), 'bo-')
            plt.plot(np.append(ex[:4], ex[0]), np.append(ey[:4], ey[0]), 'b-',
                     lw=0.4, ms=2)

            if element_labels:
                va = 'center'
                ha = 'center'
                plt.text(xt, yt, f'{ele_tag}', va=va, ha=ha, color='red')

        if node_labels:
            for node_tag in node_tags:
                if not offset_nd_label == 'above':
                    offset_nd_label_x, offset_nd_label_y = _offnl, _offnl
                    va = 'bottom'
                    # va = 'center'
                    ha = 'left'
                else:
                    offset_nd_label_x, offset_nd_label_y = 0.0, _offnl
                    va = 'bottom'
                    ha = 'center'

                plt.text(ops.nodeCoord(node_tag)[0]+offset_nd_label_x,
                         ops.nodeCoord(node_tag)[1]+offset_nd_label_y,
                         f'{node_tag}', va=va, ha=ha, color='blue')

        plt.axis('equal')

    # 2d quadrilateral (quad9n) elements plot_model
    elif nen == 9:

        for node_tag in node_tags:
            x_crd = ops.nodeCoord(node_tag)[0]
            y_crd = ops.nodeCoord(node_tag)[1]
            if x_crd > max_x_crd:
                max_x_crd = x_crd
            if y_crd > max_y_crd:
                max_y_crd = y_crd

        max_crd = np.amax([max_x_crd, max_y_crd])
        _offset = 0.005 * max_crd
        _offnl = 0.003 * max_crd

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6, nd7, nd8, nd9 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0],
                           ops.nodeCoord(nd5)[0],
                           ops.nodeCoord(nd6)[0],
                           ops.nodeCoord(nd7)[0],
                           ops.nodeCoord(nd8)[0],
                           ops.nodeCoord(nd9)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1],
                           ops.nodeCoord(nd5)[1],
                           ops.nodeCoord(nd6)[1],
                           ops.nodeCoord(nd7)[1],
                           ops.nodeCoord(nd8)[1],
                           ops.nodeCoord(nd9)[1]])

            # location of label
            xt = sum(ex)/nen
            yt = sum(ey)/nen

            plt.plot([ex[0], ex[4], ex[1], ex[5], ex[2], ex[6],
                      ex[3], ex[7], ex[0]],
                     [ey[0], ey[4], ey[1], ey[5], ey[2], ey[6],
                      ey[3], ey[7], ey[0]], 'b.-',
                     lw=0.4, ms=2, mfc='g', mec='g')
            plt.scatter([ex[8]], [ey[8]], s=2, color='g')

            if element_labels:
                va = 'center'
                ha = 'center'
                plt.text(xt, yt, f'{ele_tag}', va=va, ha=ha, color='red')

        if node_labels:
            for node_tag in node_tags:
                if not offset_nd_label == 'above':
                    offset_nd_label_x, offset_nd_label_y = _offnl, _offnl
                    va = 'bottom'
                    # va = 'center'
                    ha = 'left'
                else:
                    offset_nd_label_x, offset_nd_label_y = 0.0, _offnl
                    va = 'bottom'
                    ha = 'center'

                plt.text(ops.nodeCoord(node_tag)[0]+offset_nd_label_x,
                         ops.nodeCoord(node_tag)[1]+offset_nd_label_y,
                         f'{node_tag}', va=va, ha=ha, color='blue')

        plt.axis('equal')

    # 2d triangle (tri6n) elements plot_model
    elif nen == 6:

        for node_tag in node_tags:
            x_crd = ops.nodeCoord(node_tag)[0]
            y_crd = ops.nodeCoord(node_tag)[1]
            if x_crd > max_x_crd:
                max_x_crd = x_crd
            if y_crd > max_y_crd:
                max_y_crd = y_crd

        max_crd = np.amax([max_x_crd, max_y_crd])
        _offset = 0.005 * max_crd
        _offnl = 0.003 * max_crd

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0],
                           ops.nodeCoord(nd5)[0],
                           ops.nodeCoord(nd6)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1],
                           ops.nodeCoord(nd5)[1],
                           ops.nodeCoord(nd6)[1]])

            # location of label
            xt = sum(ex)/nen
            yt = sum(ey)/nen

            # plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]), 'bo-')
            plt.plot(np.append(ex[:3], ex[0]), np.append(ey[:3], ey[0]), 'b-',
                     lw=0.4, ms=2)

            if element_labels:
                va = 'center'
                ha = 'center'
                plt.text(xt, yt, f'{ele_tag}', va=va, ha=ha, color='red')

        if node_labels:
            for node_tag in node_tags:
                if not offset_nd_label == 'above':
                    offset_nd_label_x, offset_nd_label_y = _offnl, _offnl
                    va = 'bottom'
                    # va = 'center'
                    ha = 'left'
                else:
                    offset_nd_label_x, offset_nd_label_y = 0.0, _offnl
                    va = 'bottom'
                    ha = 'center'

                plt.text(ops.nodeCoord(node_tag)[0]+offset_nd_label_x,
                         ops.nodeCoord(node_tag)[1]+offset_nd_label_y,
                         f'{node_tag}', va=va, ha=ha, color='blue')

        plt.axis('equal')


def _plot_model_3d(node_labels, element_labels, offset_nd_label, axis_off,
                   az_el, fig_wi_he, fig_lbrt):

    node_tags = ops.getNodeTags()
    ele_tags = ops.getEleTags()

    azim, elev = az_el

    fig_wi, fig_he = fig_wi_he
    fleft, fbottom, fright, ftop = fig_lbrt

    fig = plt.figure(figsize=(fig_wi/2.54, fig_he/2.54))
    fig.subplots_adjust(left=.08, bottom=.08, right=.985, top=.94)

    ax = fig.add_subplot(111, projection=Axes3D.name)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.view_init(azim=azim, elev=elev)

    max_x_crd, max_y_crd, max_z_crd, max_crd = -np.inf, -np.inf, \
        -np.inf, -np.inf

    nen = np.shape(ops.eleNodes(ele_tags[0]))[0]

    # truss and beam/frame elements
    if nen == 2:
        for node_tag in node_tags:
            x_crd = ops.nodeCoord(node_tag)[0]
            y_crd = ops.nodeCoord(node_tag)[1]
            z_crd = ops.nodeCoord(node_tag)[2]
            if x_crd > max_x_crd:
                max_x_crd = x_crd
            if y_crd > max_y_crd:
                max_y_crd = y_crd
            if z_crd > max_z_crd:
                max_z_crd = z_crd

        if offset_nd_label == 0 or offset_nd_label == 0.:
            _offset = 0.
        else:
            max_crd = np.amax([max_x_crd, max_y_crd, max_z_crd])
            _offset = 0.005 * max_crd

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2 = ops.eleNodes(ele_tag)

            # element node1-node2, x,  y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0], ops.nodeCoord(nd2)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1], ops.nodeCoord(nd2)[1]])
            ez = np.array([ops.nodeCoord(nd1)[2], ops.nodeCoord(nd2)[2]])

            # location of label
            xt = sum(ex)/nen
            yt = sum(ey)/nen
            zt = sum(ez)/nen

            ax.plot(ex, ey, ez, 'b.-')

            # fixme: placement of node_tag labels
            if element_labels:
                if ex[1]-ex[0] == 0:
                    va = 'center'
                    ha = 'left'
                    offset_x, offset_y, offset_z = _offset, 0.0, 0.0
                elif ey[1]-ey[0] == 0:
                    va = 'bottom'
                    ha = 'center'
                    offset_x, offset_y, offset_z = 0.0, _offset, 0.0
                elif ez[1]-ez[0] == 0:
                    va = 'bottom'
                    ha = 'center'
                    offset_x, offset_y, offset_z = 0.0, 0.0, _offset
                else:
                    va = 'bottom'
                    ha = 'left'
                    offset_x, offset_y, offset_z = 0.03, 0.03, 0.03

                ax.text(xt+offset_x, yt+offset_y, zt+offset_z, f'{ele_tag}',
                        va=va, ha=ha, color='red')

        if node_labels:
            for node_tag in node_tags:
                ax.text(ops.nodeCoord(node_tag)[0]+_offset,
                        ops.nodeCoord(node_tag)[1]+_offset,
                        ops.nodeCoord(node_tag)[2]+_offset,
                        f'{node_tag}', va='bottom', ha='left', color='blue')

    # quad in 3d
    elif nen == 4:
        for node_tag in node_tags:
            x_crd = ops.nodeCoord(node_tag)[0]
            y_crd = ops.nodeCoord(node_tag)[1]
            z_crd = ops.nodeCoord(node_tag)[2]
            if x_crd > max_x_crd:
                max_x_crd = x_crd
            if y_crd > max_y_crd:
                max_y_crd = y_crd
            if z_crd > max_z_crd:
                max_z_crd = z_crd

            # ax.plot([x_crd], [y_crd], [z_crd], 'ro')

        max_crd = np.amax([max_x_crd, max_y_crd, max_z_crd])
        _offset = 0.002 * max_crd

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4 = ops.eleNodes(ele_tag)

            # element node1-node2, x,  y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1]])
            ez = np.array([ops.nodeCoord(nd1)[2],
                           ops.nodeCoord(nd2)[2],
                           ops.nodeCoord(nd3)[2],
                           ops.nodeCoord(nd4)[2]])

            # location of label
            xt = sum(ex)/nen
            yt = sum(ey)/nen
            zt = sum(ez)/nen

            ax.plot(np.append(ex, ex[0]),
                    np.append(ey, ey[0]),
                    np.append(ez, ez[0]), 'b.-')

            # fixme: placement of node_tag labels
            if element_labels:
                if ex[1]-ex[0] == 0:
                    va = 'center'
                    ha = 'left'
                    offset_x, offset_y, offset_z = _offset, 0.0, 0.0
                elif ey[1]-ey[0] == 0:
                    va = 'bottom'
                    ha = 'center'
                    offset_x, offset_y, offset_z = 0.0, _offset, 0.0
                elif ez[1]-ez[0] == 0:
                    va = 'bottom'
                    ha = 'center'
                    offset_x, offset_y, offset_z = 0.0, 0.0, _offset
                else:
                    va = 'bottom'
                    ha = 'left'
                    offset_x, offset_y, offset_z = 0.03, 0.03, 0.03

                ax.text(xt+offset_x, yt+offset_y, zt+offset_z, f'{ele_tag}',
                        va=va, ha=ha, color='red')

        if node_labels:
            for node_tag in node_tags:
                ax.text(ops.nodeCoord(node_tag)[0]+_offset,
                        ops.nodeCoord(node_tag)[1]+_offset,
                        ops.nodeCoord(node_tag)[2]+_offset,
                        f'{node_tag}', va='bottom', ha='left', color='blue')

    # 8-node brick, 3d model
    elif nen == 8:
        for node_tag in node_tags:
            x_crd = ops.nodeCoord(node_tag)[0]
            y_crd = ops.nodeCoord(node_tag)[1]
            z_crd = ops.nodeCoord(node_tag)[2]
            if x_crd > max_x_crd:
                max_x_crd = x_crd
            if y_crd > max_y_crd:
                max_y_crd = y_crd
            if z_crd > max_z_crd:
                max_z_crd = z_crd

            # ax.plot([x_crd], [y_crd], [z_crd], 'ro')

        max_crd = np.amax([max_x_crd, max_y_crd, max_z_crd])
        _offset = 0.005 * max_crd

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6, nd7, nd8 = ops.eleNodes(ele_tag)

            # element node1-node2, x,  y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0],
                           ops.nodeCoord(nd5)[0],
                           ops.nodeCoord(nd6)[0],
                           ops.nodeCoord(nd7)[0],
                           ops.nodeCoord(nd8)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1],
                           ops.nodeCoord(nd5)[1],
                           ops.nodeCoord(nd6)[1],
                           ops.nodeCoord(nd7)[1],
                           ops.nodeCoord(nd8)[1]])
            ez = np.array([ops.nodeCoord(nd1)[2],
                           ops.nodeCoord(nd2)[2],
                           ops.nodeCoord(nd3)[2],
                           ops.nodeCoord(nd4)[2],
                           ops.nodeCoord(nd5)[2],
                           ops.nodeCoord(nd6)[2],
                           ops.nodeCoord(nd7)[2],
                           ops.nodeCoord(nd8)[2]])

            # location of label
            xt = sum(ex)/nen
            yt = sum(ey)/nen
            zt = sum(ez)/nen

            ax.plot(np.append(ex[0:4], ex[0]),
                    np.append(ey[0:4], ey[0]),
                    np.append(ez[0:4], ez[0]), 'b.-')
            ax.plot(np.append(ex[4:8], ex[4]),
                    np.append(ey[4:8], ey[4]),
                    np.append(ez[4:8], ez[4]), 'b.-')
            ax.plot([ex[0], ex[4]], [ey[0], ey[4]], [ez[0], ez[4]], 'b.-')
            ax.plot([ex[1], ex[5]], [ey[1], ey[5]], [ez[1], ez[5]], 'b.-')
            ax.plot([ex[2], ex[6]], [ey[2], ey[6]], [ez[2], ez[6]], 'b.-')
            ax.plot([ex[3], ex[7]], [ey[3], ey[7]], [ez[3], ez[7]], 'b.-')

            # fixme: placement of node_tag labels
            if element_labels:
                if ex[1]-ex[0] == 0:
                    va = 'center'
                    ha = 'left'
                    offset_x, offset_y, offset_z = _offset, 0.0, 0.0
                elif ey[1]-ey[0] == 0:
                    va = 'bottom'
                    ha = 'center'
                    offset_x, offset_y, offset_z = 0.0, _offset, 0.0
                elif ez[1]-ez[0] == 0:
                    va = 'bottom'
                    ha = 'center'
                    offset_x, offset_y, offset_z = 0.0, 0.0, _offset
                else:
                    va = 'bottom'
                    ha = 'left'
                    offset_x, offset_y, offset_z = 0.03, 0.03, 0.03

                ax.text(xt+offset_x, yt+offset_y, zt+offset_z, f'{ele_tag}',
                        va=va, ha=ha, color='red')

        if node_labels:
            for node_tag in node_tags:
                ax.text(ops.nodeCoord(node_tag)[0]+_offset,
                        ops.nodeCoord(node_tag)[1]+_offset,
                        ops.nodeCoord(node_tag)[2]+_offset,
                        f'{node_tag}', va='bottom', ha='left', color='blue')

    ax.set_box_aspect((np.ptp(ax.get_xlim3d()),
                       np.ptp(ax.get_ylim3d()),
                       np.ptp(ax.get_zlim3d())))


def plot_model(node_labels=1, element_labels=1, offset_nd_label=False,
               axis_off=0, az_el=az_el, fig_wi_he=fig_wi_he,
               fig_lbrt=fig_lbrt):
    """Plot defined model of the structure.

    Args:
        node_labels (int): 1 - plot node labels, 0 - do not plot them;
            (default: 1)

        element_labels (int): 1 - plot element labels, 0 - do not plot
            them; (default: 1)

        offset_nd_label (bool): False - do not offset node labels from the
            actual node location. This option can enhance visibility.

        axis_off (int): 0 - turn off axes, 1 - display axes; (default: 0)

        az_el (tuple): contains azimuth and elevation for 3d plots. For 2d
            plots this parameter is neglected.

        fig_wi_he (tuple): contains width and height of the figure

        fig_lbrt (tuple): a tuple contating left, bottom, right and top offsets

    Usage:

    ``plot_model()`` - plot model with node and element labels.

    ``plot_model(node_labels=0, element_labels=0)`` - plot model without node
    element labels

    ``plot_model(fig_wi_he=(20., 14.))`` - plot model in a window 20 cm long,
    and 14 cm high.
    """

    # az_el - azimut, elevation used for 3d plots only
    node_tags = ops.getNodeTags()

    ndim = np.shape(ops.nodeCoord(node_tags[0]))[0]

    if ndim == 2:
        _plot_model_2d(node_labels, element_labels, offset_nd_label, axis_off,
                       fig_wi_he, fig_lbrt)
        if axis_off:
            plt.axis('off')

    elif ndim == 3:
        _plot_model_3d(node_labels, element_labels, offset_nd_label, axis_off,
                       az_el, fig_wi_he, fig_lbrt)
        if axis_off:
            plt.axis('off')

    else:
        print(f'\nWarning! ndim: {ndim} not supported yet.')

    # plt.show()  # call this from main py file for more control


def _plot_defo_mode_2d(modeNo, sfac, nep, unDefoFlag, fmt_defo, fmt_undefo,
                       interpFlag, endDispFlag, fmt_interp, fmt_nodes):

    ele_tags = ops.getEleTags()

    nen = np.shape(ops.eleNodes(ele_tags[0]))[0]

    # truss and beam/frame elements
    if nen == 2:

        ndf = np.shape(ops.nodeDOFs(ops.eleNodes(ele_tags[0])[0]))[0]

        # truss element plot_defo
        if ndf == 2:

            for ele_tag in ele_tags:
                nd1, nd2 = ops.eleNodes(ele_tag)

                # element x, y coordinates
                ex = np.array([ops.nodeCoord(nd1)[0],
                               ops.nodeCoord(nd2)[0]])
                ey = np.array([ops.nodeCoord(nd1)[1],
                               ops.nodeCoord(nd2)[1]])

                if modeNo:
                    eux = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                                    ops.nodeEigenvector(nd2, modeNo)[0]])
                    euy = np.array([ops.nodeEigenvector(nd1, modeNo)[1],
                                    ops.nodeEigenvector(nd2, modeNo)[1]])
                else:
                    eux = np.array([ops.nodeDisp(nd1)[0],
                                    ops.nodeDisp(nd2)[0]])
                    euy = np.array([ops.nodeDisp(nd1)[1],
                                    ops.nodeDisp(nd2)[1]])

                # displaced element coordinates (scaled by sfac factor)
                edx = np.array([ex[0] + sfac*eux[0], ex[1] + sfac*eux[1]])
                edy = np.array([ey[0] + sfac*euy[0], ey[1] + sfac*euy[1]])

                if unDefoFlag:
                    plt.plot(ex, ey, fmt_undefo)

                plt.plot(edx, edy, fmt_interp)

        # beam/frame element plot_defo
        elif ndf == 3:

            for ele_tag in ele_tags:
                nd1, nd2 = ops.eleNodes(ele_tag)

                # element x, y coordinates
                ex = np.array([ops.nodeCoord(nd1)[0],
                               ops.nodeCoord(nd2)[0]])
                ey = np.array([ops.nodeCoord(nd1)[1],
                               ops.nodeCoord(nd2)[1]])

                if modeNo:
                    ed = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                                   ops.nodeEigenvector(nd1, modeNo)[1],
                                   ops.nodeEigenvector(nd1, modeNo)[2],
                                   ops.nodeEigenvector(nd2, modeNo)[0],
                                   ops.nodeEigenvector(nd2, modeNo)[1],
                                   ops.nodeEigenvector(nd2, modeNo)[2]])
                else:
                    ed = np.array([ops.nodeDisp(nd1)[0],
                                   ops.nodeDisp(nd1)[1],
                                   ops.nodeDisp(nd1)[2],
                                   ops.nodeDisp(nd2)[0],
                                   ops.nodeDisp(nd2)[1],
                                   ops.nodeDisp(nd2)[2]])

                if unDefoFlag:
                    plt.plot(ex, ey, fmt_undefo)

                # interpolated displacement field
                if interpFlag:
                    xcdi, ycdi = beam_defo_interp_2d(ex, ey, ed, sfac, nep)
                    plt.plot(xcdi, ycdi, fmt_interp)

                # translations of ends
                if endDispFlag:
                    xdi, ydi = beam_disp_ends(ex, ey, ed, sfac)
                    plt.plot(xdi, ydi, fmt_nodes)

        plt.axis('equal')
        # plt.show()  # call this from main py file for more control

    # 2d triangular (tri31) elements plot_defo
    elif nen == 3:
        for ele_tag in ele_tags:
            nd1, nd2, nd3 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1]])

            if modeNo:
                ed = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                               ops.nodeEigenvector(nd1, modeNo)[1],
                               ops.nodeEigenvector(nd2, modeNo)[0],
                               ops.nodeEigenvector(nd2, modeNo)[1],
                               ops.nodeEigenvector(nd3, modeNo)[0],
                               ops.nodeEigenvector(nd3, modeNo)[1]])
            else:
                ed = np.array([ops.nodeDisp(nd1)[0],
                               ops.nodeDisp(nd1)[1],
                               ops.nodeDisp(nd2)[0],
                               ops.nodeDisp(nd2)[1],
                               ops.nodeDisp(nd3)[0],
                               ops.nodeDisp(nd3)[1]])

            if unDefoFlag:
                plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]),
                         fmt_undefo)

            # xcdi, ycdi = beam_defo_interp_2d(ex, ey, ed, sfac, nep)
            # xdi, ydi = beam_disp_ends(ex, ey, ed, sfac)
            # # interpolated displacement field
            # plt.plot(xcdi, ycdi, 'b.-')
            # # translations of ends only
            # plt.plot(xdi, ydi, 'ro')

            # xc = [x, x[0, :]]
            # yc = [x, x[0, :]]
            # test it with one element
            x = ex+sfac*ed[[0, 2, 4]]
            y = ey+sfac*ed[[1, 3, 5]]
            # x = ex+sfac*ed[[0, 2, 4, 6]]
            # y = ey+sfac*ed[[1, 3, 5, 7]]
            plt.plot(np.append(x, x[0]), np.append(y, y[0]), fmt_defo)

        plt.axis('equal')

    # 2d quadrilateral (quad) elements plot_defo
    elif nen == 4:
        for ele_tag in ele_tags:
            nd1, nd2, nd3, nd4 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1]])

            if modeNo:
                ed = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                               ops.nodeEigenvector(nd1, modeNo)[1],
                               ops.nodeEigenvector(nd2, modeNo)[0],
                               ops.nodeEigenvector(nd2, modeNo)[1],
                               ops.nodeEigenvector(nd3, modeNo)[0],
                               ops.nodeEigenvector(nd3, modeNo)[1],
                               ops.nodeEigenvector(nd4, modeNo)[0],
                               ops.nodeEigenvector(nd4, modeNo)[1]])
            else:
                ed = np.array([ops.nodeDisp(nd1)[0],
                               ops.nodeDisp(nd1)[1],
                               ops.nodeDisp(nd2)[0],
                               ops.nodeDisp(nd2)[1],
                               ops.nodeDisp(nd3)[0],
                               ops.nodeDisp(nd3)[1],
                               ops.nodeDisp(nd4)[0],
                               ops.nodeDisp(nd4)[1]])

            if unDefoFlag:
                plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]),
                         fmt_undefo)

            # xcdi, ycdi = beam_defo_interp_2d(ex, ey, ed, sfac, nep)
            # xdi, ydi = beam_disp_ends(ex, ey, ed, sfac)
            # # interpolated displacement field
            # plt.plot(xcdi, ycdi, 'b.-')
            # # translations of ends only
            # plt.plot(xdi, ydi, 'ro')

            # test it with one element
            x = ex+sfac*ed[[0, 2, 4, 6]]
            y = ey+sfac*ed[[1, 3, 5, 7]]
            plt.plot(np.append(x, x[0]), np.append(y, y[0]), fmt_defo)

        plt.axis('equal')

    # 2d quadrilateral (quad8n) elements plot_defo
    elif nen == 8:
        for ele_tag in ele_tags:
            nd1, nd2, nd3, nd4, nd5, nd6, nd7, nd8 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0],
                           ops.nodeCoord(nd5)[0],
                           ops.nodeCoord(nd6)[0],
                           ops.nodeCoord(nd7)[0],
                           ops.nodeCoord(nd8)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1],
                           ops.nodeCoord(nd5)[1],
                           ops.nodeCoord(nd6)[1],
                           ops.nodeCoord(nd7)[1],
                           ops.nodeCoord(nd8)[1]])

            if modeNo:
                ed = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                               ops.nodeEigenvector(nd1, modeNo)[1],
                               ops.nodeEigenvector(nd2, modeNo)[0],
                               ops.nodeEigenvector(nd2, modeNo)[1],
                               ops.nodeEigenvector(nd3, modeNo)[0],
                               ops.nodeEigenvector(nd3, modeNo)[1],
                               ops.nodeEigenvector(nd4, modeNo)[0],
                               ops.nodeEigenvector(nd4, modeNo)[1],
                               ops.nodeEigenvector(nd5, modeNo)[0],
                               ops.nodeEigenvector(nd5, modeNo)[1],
                               ops.nodeEigenvector(nd6, modeNo)[0],
                               ops.nodeEigenvector(nd6, modeNo)[1],
                               ops.nodeEigenvector(nd7, modeNo)[0],
                               ops.nodeEigenvector(nd7, modeNo)[1],
                               ops.nodeEigenvector(nd8, modeNo)[0],
                               ops.nodeEigenvector(nd8, modeNo)[1]])
            else:
                ed = np.array([ops.nodeDisp(nd1)[0],
                               ops.nodeDisp(nd1)[1],
                               ops.nodeDisp(nd2)[0],
                               ops.nodeDisp(nd2)[1],
                               ops.nodeDisp(nd3)[0],
                               ops.nodeDisp(nd3)[1],
                               ops.nodeDisp(nd4)[0],
                               ops.nodeDisp(nd4)[1],
                               ops.nodeDisp(nd5)[0],
                               ops.nodeDisp(nd5)[1],
                               ops.nodeDisp(nd6)[0],
                               ops.nodeDisp(nd6)[1],
                               ops.nodeDisp(nd7)[0],
                               ops.nodeDisp(nd7)[1],
                               ops.nodeDisp(nd8)[0],
                               ops.nodeDisp(nd8)[1]])

            if unDefoFlag:
                plt.plot([ex[0], ex[4], ex[1], ex[5], ex[2], ex[6],
                          ex[3], ex[7], ex[0]],
                         [ey[0], ey[4], ey[1], ey[5], ey[2], ey[6],
                          ey[3], ey[7], ey[0]],
                         fmt_undefo)

            # xcdi, ycdi = beam_defo_interp_2d(ex, ey, ed, sfac, nep)
            # xdi, ydi = beam_disp_ends(ex, ey, ed, sfac)
            # # interpolated displacement field
            # plt.plot(xcdi, ycdi, 'b.-')
            # # translations of ends only
            # plt.plot(xdi, ydi, 'ro')

            # test it with one element
            x = ex+sfac*ed[[0, 2, 4, 6, 8, 10, 12, 14]]
            y = ey+sfac*ed[[1, 3, 5, 7, 9, 11, 13, 15]]
            plt.plot([x[0], x[4], x[1], x[5], x[2], x[6], x[3], x[7], x[0]],
                     [y[0], y[4], y[1], y[5], y[2], y[6], y[3], y[7], y[0]],
                     fmt_defo)

        plt.axis('equal')

    # 2d quadrilateral (quad9n) elements plot_defo
    elif nen == 9:
        for ele_tag in ele_tags:
            nd1, nd2, nd3, nd4, nd5, nd6, nd7, nd8, nd9 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0],
                           ops.nodeCoord(nd5)[0],
                           ops.nodeCoord(nd6)[0],
                           ops.nodeCoord(nd7)[0],
                           ops.nodeCoord(nd8)[0],
                           ops.nodeCoord(nd9)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1],
                           ops.nodeCoord(nd5)[1],
                           ops.nodeCoord(nd6)[1],
                           ops.nodeCoord(nd7)[1],
                           ops.nodeCoord(nd8)[1],
                           ops.nodeCoord(nd9)[1]])

            if modeNo:
                ed = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                               ops.nodeEigenvector(nd1, modeNo)[1],
                               ops.nodeEigenvector(nd2, modeNo)[0],
                               ops.nodeEigenvector(nd2, modeNo)[1],
                               ops.nodeEigenvector(nd3, modeNo)[0],
                               ops.nodeEigenvector(nd3, modeNo)[1],
                               ops.nodeEigenvector(nd4, modeNo)[0],
                               ops.nodeEigenvector(nd4, modeNo)[1],
                               ops.nodeEigenvector(nd5, modeNo)[0],
                               ops.nodeEigenvector(nd5, modeNo)[1],
                               ops.nodeEigenvector(nd6, modeNo)[0],
                               ops.nodeEigenvector(nd6, modeNo)[1],
                               ops.nodeEigenvector(nd7, modeNo)[0],
                               ops.nodeEigenvector(nd7, modeNo)[1],
                               ops.nodeEigenvector(nd8, modeNo)[0],
                               ops.nodeEigenvector(nd8, modeNo)[1],
                               ops.nodeEigenvector(nd9, modeNo)[0],
                               ops.nodeEigenvector(nd9, modeNo)[1]])
            else:
                ed = np.array([ops.nodeDisp(nd1)[0],
                               ops.nodeDisp(nd1)[1],
                               ops.nodeDisp(nd2)[0],
                               ops.nodeDisp(nd2)[1],
                               ops.nodeDisp(nd3)[0],
                               ops.nodeDisp(nd3)[1],
                               ops.nodeDisp(nd4)[0],
                               ops.nodeDisp(nd4)[1],
                               ops.nodeDisp(nd5)[0],
                               ops.nodeDisp(nd5)[1],
                               ops.nodeDisp(nd6)[0],
                               ops.nodeDisp(nd6)[1],
                               ops.nodeDisp(nd7)[0],
                               ops.nodeDisp(nd7)[1],
                               ops.nodeDisp(nd8)[0],
                               ops.nodeDisp(nd8)[1],
                               ops.nodeDisp(nd9)[0],
                               ops.nodeDisp(nd9)[1]])

            if unDefoFlag:
                plt.plot([ex[0], ex[4], ex[1], ex[5], ex[2], ex[6],
                          ex[3], ex[7], ex[0]],
                         [ey[0], ey[4], ey[1], ey[5], ey[2], ey[6],
                          ey[3], ey[7], ey[0]],
                         fmt_undefo)

            # xcdi, ycdi = beam_defo_interp_2d(ex, ey, ed, sfac, nep)
            # xdi, ydi = beam_disp_ends(ex, ey, ed, sfac)
            # # interpolated displacement field
            # plt.plot(xcdi, ycdi, 'b.-')
            # # translations of ends only
            # plt.plot(xdi, ydi, 'ro')

            # test it with one element
            x = ex+sfac*ed[[0, 2, 4, 6, 8, 10, 12, 14, 16]]
            y = ey+sfac*ed[[1, 3, 5, 7, 9, 11, 13, 15, 17]]
            plt.plot([x[0], x[4], x[1], x[5], x[2], x[6],
                      x[3], x[7], x[0]],
                     [y[0], y[4], y[1], y[5], y[2], y[6],
                      y[3], y[7], y[0]], fmt_defo)
            plt.plot([x[8]], [y[8]], 'b.-')

        plt.axis('equal')

    # 2d triangle (tri6n) elements plot_defo
    elif nen == 6:
        for ele_tag in ele_tags:
            nd1, nd2, nd3, nd4, nd5, nd6 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0],
                           ops.nodeCoord(nd5)[0],
                           ops.nodeCoord(nd6)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1],
                           ops.nodeCoord(nd5)[1],
                           ops.nodeCoord(nd6)[1]])

            if modeNo:
                ed = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                               ops.nodeEigenvector(nd1, modeNo)[1],
                               ops.nodeEigenvector(nd2, modeNo)[0],
                               ops.nodeEigenvector(nd2, modeNo)[1],
                               ops.nodeEigenvector(nd3, modeNo)[0],
                               ops.nodeEigenvector(nd3, modeNo)[1],
                               ops.nodeEigenvector(nd4, modeNo)[0],
                               ops.nodeEigenvector(nd4, modeNo)[1],
                               ops.nodeEigenvector(nd5, modeNo)[0],
                               ops.nodeEigenvector(nd5, modeNo)[1],
                               ops.nodeEigenvector(nd6, modeNo)[0],
                               ops.nodeEigenvector(nd6, modeNo)[1]])
            else:
                ed = np.array([ops.nodeDisp(nd1)[0],
                               ops.nodeDisp(nd1)[1],
                               ops.nodeDisp(nd2)[0],
                               ops.nodeDisp(nd2)[1],
                               ops.nodeDisp(nd3)[0],
                               ops.nodeDisp(nd3)[1],
                               ops.nodeDisp(nd4)[0],
                               ops.nodeDisp(nd4)[1],
                               ops.nodeDisp(nd5)[0],
                               ops.nodeDisp(nd5)[1],
                               ops.nodeDisp(nd6)[0],
                               ops.nodeDisp(nd6)[1]])

            if unDefoFlag:
                plt.plot([ex[0], ex[3], ex[1], ex[4], ex[2], ex[5],
                          ex[0]],
                         [ey[0], ey[3], ey[1], ey[4], ey[2], ey[5],
                          ey[0]],
                         fmt_undefo)

            # xcdi, ycdi = beam_defo_interp_2d(ex, ey, ed, sfac, nep)
            # xdi, ydi = beam_disp_ends(ex, ey, ed, sfac)
            # # interpolated displacement field
            # plt.plot(xcdi, ycdi, 'b.-')
            # # translations of ends only
            # plt.plot(xdi, ydi, 'ro')

            # test it with one element
            x = ex+sfac*ed[[0, 2, 4, 6, 8, 10]]
            y = ey+sfac*ed[[1, 3, 5, 7, 9, 11]]
            plt.plot([x[0], x[3], x[1], x[4], x[2], x[5], x[0]],
                     [y[0], y[3], y[1], y[4], y[2], y[5], y[0]], fmt_defo)

        plt.axis('equal')

    # 2d 8-node quadratic elements
    # elif nen == 8:
    #     x = ex+sfac*ed[:, [0, 2, 4, 6, 8, 10, 12, 14]]
    #     y = ex+sfac*ed[:, [1, 3, 5, 7, 9, 11, 13, 15]]

    #     t = -1
    #     n = 0
    #     for s in range(-1, 1.4, 0.4):
    #         n += 1
    #     ...

    else:
        print(f'\nWarning! Elements not supported yet. nen: {nen}; must be: 2, 3, 4, 8.')  # noqa: E501


def _plot_defo_mode_3d(modeNo, sfac, nep, unDefoFlag, fmt_defo, fmt_undefo,
                       interpFlag, endDispFlag, fmt_interp, fmt_nodes, az_el,
                       fig_wi_he, fig_lbrt):

    ele_tags = ops.getEleTags()

    azim, elev = az_el
    fig_wi, fig_he = fig_wi_he
    fleft, fbottom, fright, ftop = fig_lbrt

    fig = plt.figure(figsize=(fig_wi/2.54, fig_he/2.54))
    fig.subplots_adjust(left=.08, bottom=.08, right=.985, top=.94)

    ax = fig.add_subplot(111, projection=Axes3D.name)
    # ax.axis('equal')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.view_init(azim=azim, elev=elev)

    nen = np.shape(ops.eleNodes(ele_tags[0]))[0]

    # plot: truss and beam/frame elements in 3d
    if nen == 2:

        ndf = np.shape(ops.nodeDOFs(ops.eleNodes(ele_tags[0])[0]))[0]

        # plot: beam/frame element in 3d
        if ndf == 6:

            for i, ele_tag in enumerate(ele_tags):
                nd1, nd2 = ops.eleNodes(ele_tag)

                # element x, y coordinates
                ex = np.array([ops.nodeCoord(nd1)[0],
                               ops.nodeCoord(nd2)[0]])
                ey = np.array([ops.nodeCoord(nd1)[1],
                               ops.nodeCoord(nd2)[1]])
                ez = np.array([ops.nodeCoord(nd1)[2],
                               ops.nodeCoord(nd2)[2]])

                if modeNo:
                    ed = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                                   ops.nodeEigenvector(nd1, modeNo)[1],
                                   ops.nodeEigenvector(nd1, modeNo)[2],
                                   ops.nodeEigenvector(nd1, modeNo)[3],
                                   ops.nodeEigenvector(nd1, modeNo)[4],
                                   ops.nodeEigenvector(nd1, modeNo)[5],
                                   ops.nodeEigenvector(nd2, modeNo)[0],
                                   ops.nodeEigenvector(nd2, modeNo)[1],
                                   ops.nodeEigenvector(nd2, modeNo)[2],
                                   ops.nodeEigenvector(nd2, modeNo)[3],
                                   ops.nodeEigenvector(nd2, modeNo)[4],
                                   ops.nodeEigenvector(nd2, modeNo)[5]])
                else:
                    ed = np.array([ops.nodeDisp(nd1)[0],
                                   ops.nodeDisp(nd1)[1],
                                   ops.nodeDisp(nd1)[2],
                                   ops.nodeDisp(nd1)[3],
                                   ops.nodeDisp(nd1)[4],
                                   ops.nodeDisp(nd1)[5],
                                   ops.nodeDisp(nd2)[0],
                                   ops.nodeDisp(nd2)[1],
                                   ops.nodeDisp(nd2)[2],
                                   ops.nodeDisp(nd2)[3],
                                   ops.nodeDisp(nd2)[4],
                                   ops.nodeDisp(nd2)[5]])

                # eo = Eo[i, :]
                xloc = ops.eleResponse(ele_tag, 'xlocal')
                yloc = ops.eleResponse(ele_tag, 'ylocal')
                zloc = ops.eleResponse(ele_tag, 'zlocal')
                g = np.vstack((xloc, yloc, zloc))

                if unDefoFlag:
                    plt.plot(ex, ey, ez, fmt_undefo)

                # interpolated displacement field
                if interpFlag:
                    xcd, ycd, zcd = beam_defo_interp_3d(ex, ey, ez, g,
                                                        ed, sfac, nep)
                    ax.plot(xcd, ycd, zcd, fmt_interp)
                    ax.set_xlabel('X')
                    ax.set_ylabel('Y')
                    ax.set_zlabel('Z')

                # translations of ends
                if endDispFlag:
                    xd, yd, zd = beam_disp_ends3d(ex, ey, ez, ed, sfac)
                    ax.plot(xd, yd, zd, fmt_nodes)

    # plot: quad in 3d
    elif nen == 4:

        ndf = np.shape(ops.nodeDOFs(ops.eleNodes(ele_tags[0])[0]))[0]

        # plot: shell in 3d
        if ndf == 6:

            for i, ele_tag in enumerate(ele_tags):
                nd1, nd2, nd3, nd4 = ops.eleNodes(ele_tag)

                # element node1-node2, x,  y coordinates
                ex = np.array([ops.nodeCoord(nd1)[0],
                               ops.nodeCoord(nd2)[0],
                               ops.nodeCoord(nd3)[0],
                               ops.nodeCoord(nd4)[0]])
                ey = np.array([ops.nodeCoord(nd1)[1],
                               ops.nodeCoord(nd2)[1],
                               ops.nodeCoord(nd3)[1],
                               ops.nodeCoord(nd4)[1]])
                ez = np.array([ops.nodeCoord(nd1)[2],
                               ops.nodeCoord(nd2)[2],
                               ops.nodeCoord(nd3)[2],
                               ops.nodeCoord(nd4)[2]])

                if modeNo:
                    ed = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                                   ops.nodeEigenvector(nd1, modeNo)[1],
                                   ops.nodeEigenvector(nd1, modeNo)[2],
                                   ops.nodeEigenvector(nd2, modeNo)[0],
                                   ops.nodeEigenvector(nd2, modeNo)[1],
                                   ops.nodeEigenvector(nd2, modeNo)[2],
                                   ops.nodeEigenvector(nd3, modeNo)[0],
                                   ops.nodeEigenvector(nd3, modeNo)[1],
                                   ops.nodeEigenvector(nd3, modeNo)[2],
                                   ops.nodeEigenvector(nd4, modeNo)[0],
                                   ops.nodeEigenvector(nd4, modeNo)[1],
                                   ops.nodeEigenvector(nd4, modeNo)[2]])
                else:
                    ed = np.array([ops.nodeDisp(nd1)[0],
                                   ops.nodeDisp(nd1)[1],
                                   ops.nodeDisp(nd1)[2],
                                   ops.nodeDisp(nd2)[0],
                                   ops.nodeDisp(nd2)[1],
                                   ops.nodeDisp(nd2)[2],
                                   ops.nodeDisp(nd3)[0],
                                   ops.nodeDisp(nd3)[1],
                                   ops.nodeDisp(nd3)[2],
                                   ops.nodeDisp(nd4)[0],
                                   ops.nodeDisp(nd4)[1],
                                   ops.nodeDisp(nd4)[2]])

                if unDefoFlag:
                    ax.plot(np.append(ex, ex[0]),
                            np.append(ey, ey[0]),
                            np.append(ez, ez[0]),
                            fmt_undefo)

                x = ex+sfac*ed[[0, 3, 6, 9]]
                y = ey+sfac*ed[[1, 4, 7, 10]]
                z = ez+sfac*ed[[2, 5, 8, 11]]
                # ax.plot(np.append(x, x[0]),
                #         np.append(y, y[0]),
                #         np.append(z, z[0]),
                #         'b.-')
                # ax.axis('equal')

                pts = [[x[0], y[0], z[0]],
                       [x[1], y[1], z[1]],
                       [x[2], y[2], z[2]],
                       [x[3], y[3], z[3]]]

                verts = [[pts[0], pts[1], pts[2], pts[3]]]
                ax.add_collection3d(Poly3DCollection(verts, linewidths=1,
                                                     edgecolors='k',
                                                     alpha=.25))

                ax.scatter(x, y, z, s=0)

    # 8-node brick, 3d model
    elif nen == 8:

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6, nd7, nd8 = ops.eleNodes(ele_tag)

            # element node1-node2, x,  y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0],
                           ops.nodeCoord(nd5)[0],
                           ops.nodeCoord(nd6)[0],
                           ops.nodeCoord(nd7)[0],
                           ops.nodeCoord(nd8)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1],
                           ops.nodeCoord(nd5)[1],
                           ops.nodeCoord(nd6)[1],
                           ops.nodeCoord(nd7)[1],
                           ops.nodeCoord(nd8)[1]])
            ez = np.array([ops.nodeCoord(nd1)[2],
                           ops.nodeCoord(nd2)[2],
                           ops.nodeCoord(nd3)[2],
                           ops.nodeCoord(nd4)[2],
                           ops.nodeCoord(nd5)[2],
                           ops.nodeCoord(nd6)[2],
                           ops.nodeCoord(nd7)[2],
                           ops.nodeCoord(nd8)[2]])

            if modeNo:
                ed = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                               ops.nodeEigenvector(nd1, modeNo)[1],
                               ops.nodeEigenvector(nd1, modeNo)[2],
                               ops.nodeEigenvector(nd2, modeNo)[0],
                               ops.nodeEigenvector(nd2, modeNo)[1],
                               ops.nodeEigenvector(nd2, modeNo)[2],
                               ops.nodeEigenvector(nd3, modeNo)[0],
                               ops.nodeEigenvector(nd3, modeNo)[1],
                               ops.nodeEigenvector(nd3, modeNo)[2],
                               ops.nodeEigenvector(nd4, modeNo)[0],
                               ops.nodeEigenvector(nd4, modeNo)[1],
                               ops.nodeEigenvector(nd4, modeNo)[2],
                               ops.nodeEigenvector(nd5, modeNo)[0],
                               ops.nodeEigenvector(nd5, modeNo)[1],
                               ops.nodeEigenvector(nd5, modeNo)[2],
                               ops.nodeEigenvector(nd6, modeNo)[0],
                               ops.nodeEigenvector(nd6, modeNo)[1],
                               ops.nodeEigenvector(nd6, modeNo)[2],
                               ops.nodeEigenvector(nd7, modeNo)[0],
                               ops.nodeEigenvector(nd7, modeNo)[1],
                               ops.nodeEigenvector(nd7, modeNo)[2],
                               ops.nodeEigenvector(nd8, modeNo)[0],
                               ops.nodeEigenvector(nd8, modeNo)[1],
                               ops.nodeEigenvector(nd8, modeNo)[2]])
            else:
                ed = np.array([ops.nodeDisp(nd1)[0],
                               ops.nodeDisp(nd1)[1],
                               ops.nodeDisp(nd1)[2],
                               ops.nodeDisp(nd2)[0],
                               ops.nodeDisp(nd2)[1],
                               ops.nodeDisp(nd2)[2],
                               ops.nodeDisp(nd3)[0],
                               ops.nodeDisp(nd3)[1],
                               ops.nodeDisp(nd3)[2],
                               ops.nodeDisp(nd4)[0],
                               ops.nodeDisp(nd4)[1],
                               ops.nodeDisp(nd4)[2],
                               ops.nodeDisp(nd5)[0],
                               ops.nodeDisp(nd5)[1],
                               ops.nodeDisp(nd5)[2],
                               ops.nodeDisp(nd6)[0],
                               ops.nodeDisp(nd6)[1],
                               ops.nodeDisp(nd6)[2],
                               ops.nodeDisp(nd7)[0],
                               ops.nodeDisp(nd7)[1],
                               ops.nodeDisp(nd7)[2],
                               ops.nodeDisp(nd8)[0],
                               ops.nodeDisp(nd8)[1],
                               ops.nodeDisp(nd8)[2]])

            if unDefoFlag:
                ax.plot(np.append(ex[0:4], ex[0]),
                        np.append(ey[0:4], ey[0]),
                        np.append(ez[0:4], ez[0]), fmt_undefo)
                ax.plot(np.append(ex[4:8], ex[4]),
                        np.append(ey[4:8], ey[4]),
                        np.append(ez[4:8], ez[4]), fmt_undefo)
                ax.plot([ex[0], ex[4]],
                        [ey[0], ey[4]],
                        [ez[0], ez[4]], fmt_undefo)
                ax.plot([ex[1], ex[5]],
                        [ey[1], ey[5]],
                        [ez[1], ez[5]], fmt_undefo)
                ax.plot([ex[2], ex[6]],
                        [ey[2], ey[6]],
                        [ez[2], ez[6]], fmt_undefo)
                ax.plot([ex[3], ex[7]],
                        [ey[3], ey[7]],
                        [ez[3], ez[7]], fmt_undefo)

            x = ex+sfac*ed[[0, 3, 6, 9, 12, 15, 18, 21]]
            y = ey+sfac*ed[[1, 4, 7, 10, 13, 16, 19, 22]]
            z = ez+sfac*ed[[2, 5, 8, 11, 14, 17, 20, 23]]
            ax.plot(np.append(x[:4], x[0]),
                    np.append(y[:4], y[0]),
                    np.append(z[:4], z[0]),
                    'b.-')
            ax.plot(np.append(x[4:8], x[4]),
                    np.append(y[4:8], y[4]),
                    np.append(z[4:8], z[4]),
                    'b.-')
            ax.plot([x[0], x[4]],
                    [y[0], y[4]],
                    [z[0], z[4]], 'b.-')
            ax.plot([x[1], x[5]],
                    [y[1], y[5]],
                    [z[1], z[5]], 'b.-')
            ax.plot([x[2], x[6]],
                    [y[2], y[6]],
                    [z[2], z[6]], 'b.-')
            ax.plot([x[3], x[7]],
                    [y[3], y[7]],
                    [z[3], z[7]], 'b.-')

    ax.set_box_aspect((np.ptp(ax.get_xlim3d()),
                       np.ptp(ax.get_ylim3d()),
                       np.ptp(ax.get_zlim3d())))


def plot_defo(sfac=False, nep=17, unDefoFlag=1, fmt_defo=fmt_defo,
              fmt_undefo=fmt_undefo, interpFlag=1, endDispFlag=0,
              fmt_interp=fmt_interp, fmt_nodes=fmt_nodes, Eo=0, az_el=az_el,
              fig_wi_he=fig_wi_he, fig_lbrt=fig_lbrt):
    """Plot deformed shape of the structure.

    Args:
        sfac (float): scale factor to increase/decrease displacements obtained
            from FE analysis. If not specified (False), sfac is automatically
            calculated based on the maximum overall displacement and this
            maximum displacement is plotted as 20 percent (hordcoded) of
            the maximum model dimension.

        interpFlag (int): 1 - use interpolated deformation using shape
            function, 0 - do not use interpolation, just show displaced element
            nodes (default is 1)

        nep (int): number of evaluation points for shape function interpolation
            (default: 17)

    Returns:
        sfac (float): the automatically calculated scale factor can be
            returned.

    Usage:

    ``sfac = plot_defo()`` - plot deformed shape with default parameters and
    automatically calcutated scale factor.

    ``plot_defo(interpFlag=0)`` - plot simplified deformation by
    displacing the nodes connected with straight lines (shape function
    interpolation)

    ``plot_defo(sfac=1.5)`` - plot with specified scale factor

    ``plot_defo(unDefoFlag=0, endDispFlag=0)`` - plot without showing
    undeformed (original) mesh and without showing markers at the
    element ends.
    """
    node_tags = ops.getNodeTags()

    # calculate sfac
    min_x, min_y, min_z = np.inf, np.inf, np.inf
    max_x, max_y, max_z = -np.inf, -np.inf, -np.inf
    max_ux, max_uy, max_uz = -np.inf, -np.inf, -np.inf
    ratio = 0.1

    ndim = np.shape(ops.nodeCoord(node_tags[0]))[0]

    if ndim == 2:
        if not sfac:
            for node_tag in node_tags:
                x_crd = ops.nodeCoord(node_tag)[0]
                y_crd = ops.nodeCoord(node_tag)[1]
                ux = ops.nodeDisp(node_tag)[0]
                uy = ops.nodeDisp(node_tag)[1]

                min_x = min(min_x, x_crd)
                min_y = min(min_y, y_crd)
                max_x = max(max_x, x_crd)
                max_y = max(max_y, y_crd)
                max_ux = max(max_ux, np.abs(ux))
                max_uy = max(max_uy, np.abs(uy))

            dxmax = max_x - min_x
            dymax = max_y - min_y
            dlmax = max(dxmax, dymax)
            edmax = max(max_ux, max_uy)
            sfac = ratio * dlmax/edmax
            if sfac > 1000.:
                print("""\nWarning!\nsfac is quite large - perhaps try to specify \
sfac value yourself.
This usually happens when translational DOFs are too small\n\n""")

        _plot_defo_mode_2d(0, sfac, nep, unDefoFlag, fmt_defo, fmt_undefo,
                           interpFlag, endDispFlag, fmt_interp,
                           fmt_nodes)

    elif ndim == 3:
        if not sfac:
            for node_tag in node_tags:
                x_crd = ops.nodeCoord(node_tag)[0]
                y_crd = ops.nodeCoord(node_tag)[1]
                z_crd = ops.nodeCoord(node_tag)[2]
                ux = ops.nodeDisp(node_tag)[0]
                uy = ops.nodeDisp(node_tag)[1]
                uz = ops.nodeDisp(node_tag)[2]

                min_x = min(min_x, x_crd)
                min_y = min(min_y, y_crd)
                min_z = min(min_z, z_crd)
                max_x = max(max_x, x_crd)
                max_y = max(max_y, y_crd)
                max_z = max(max_z, z_crd)
                max_ux = max(max_ux, np.abs(ux))
                max_uy = max(max_uy, np.abs(uy))
                max_uz = max(max_uz, np.abs(uz))

            dxmax = max_x - min_x
            dymax = max_y - min_y
            dzmax = max_z - min_z
            dlmax = max(dxmax, dymax, dzmax)
            edmax = max(max_ux, max_uy, max_uz)
            sfac = ratio * dlmax/edmax

        _plot_defo_mode_3d(0, sfac, nep, unDefoFlag, fmt_defo, fmt_undefo,
                           interpFlag, endDispFlag, fmt_interp,
                           fmt_nodes, az_el, fig_wi_he, fig_lbrt)

    else:
        print(f'\nWarning! ndim: {ndim} not supported yet.')

    return sfac


def _anim_mode_2d(modeNo, sfac, nep, unDefoFlag, fmt_defo, fmt_undefo,
                  interpFlag, endDispFlag, fmt_interp, fmt_nodes, fig_wi_he,
                  xlim, ylim, lw):

    fig_wi, fig_he = fig_wi_he
    ele_tags = ops.getEleTags()

    nen = np.shape(ops.eleNodes(ele_tags[0]))[0]

    # truss and beam/frame elements
    if nen == 2:

        ndf = np.shape(ops.nodeDOFs(ops.eleNodes(ele_tags[0])[0]))[0]

        # truss element
        if ndf == 2:

            for ele_tag in ele_tags:
                nd1, nd2 = ops.eleNodes(ele_tag)

                # element x, y coordinates
                ex = np.array([ops.nodeCoord(nd1)[0],
                               ops.nodeCoord(nd2)[0]])
                ey = np.array([ops.nodeCoord(nd1)[1],
                               ops.nodeCoord(nd2)[1]])

                if modeNo:
                    eux = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                                    ops.nodeEigenvector(nd2, modeNo)[0]])
                    euy = np.array([ops.nodeEigenvector(nd1, modeNo)[1],
                                    ops.nodeEigenvector(nd2, modeNo)[1]])
                else:
                    eux = np.array([ops.nodeDisp(nd1)[0],
                                    ops.nodeDisp(nd2)[0]])
                    euy = np.array([ops.nodeDisp(nd1)[1],
                                    ops.nodeDisp(nd2)[1]])

                # displaced element coordinates (scaled by sfac factor)
                edx = np.array([ex[0] + sfac*eux[0], ex[1] + sfac*eux[1]])
                edy = np.array([ey[0] + sfac*euy[0], ey[1] + sfac*euy[1]])

                if unDefoFlag:
                    plt.plot(ex, ey, fmt_undefo)

                plt.plot(edx, edy, fmt_interp)

        # beam/frame element anim eigen
        elif ndf == 3:

            fig, ax = plt.subplots(figsize=(fig_wi/2.54, fig_he/2.54))
            ax.axis('equal')
            ax.set_xlim(xlim[0], xlim[1])
            ax.set_ylim(ylim[0], ylim[1])

            nel = len(ele_tags)
            Ex = np.zeros((nel, 2))
            Ey = np.zeros((nel, 2))
            Ed = np.zeros((nel, 6))
            # time vector for one cycle (period)
            n_cycles = 10
            n_frames = n_cycles * 32 + 1
            t = np.linspace(0., n_cycles*2*np.pi, n_frames)
            lines = []

            for i, ele_tag in enumerate(ele_tags):
                nd1, nd2 = ops.eleNodes(ele_tag)

                # element x, y coordinates
                Ex[i, :] = np.array([ops.nodeCoord(nd1)[0],
                                     ops.nodeCoord(nd2)[0]])
                Ey[i, :] = np.array([ops.nodeCoord(nd1)[1],
                                     ops.nodeCoord(nd2)[1]])

                Ed[i, :] = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                                     ops.nodeEigenvector(nd1, modeNo)[1],
                                     ops.nodeEigenvector(nd1, modeNo)[2],
                                     ops.nodeEigenvector(nd2, modeNo)[0],
                                     ops.nodeEigenvector(nd2, modeNo)[1],
                                     ops.nodeEigenvector(nd2, modeNo)[2]])

                lines.append(ax.plot([], [], fmt_nodes, lw=lw)[0])

            def init():
                for j, ele_tag in enumerate(ele_tags):
                    lines[j].set_data([], [])
                return lines

            def animate(i):
                for j, ele_tag in enumerate(ele_tags):

                    if interpFlag:
                        xcdi, ycdi = beam_defo_interp_2d(Ex[j, :],
                                                         Ey[j, :],
                                                         Ed[j, :],
                                                         sfac*np.sin(t[i]),
                                                         nep)
                        lines[j].set_data(xcdi, ycdi)
                    else:
                        xdi, ydi = beam_disp_ends(Ex[j, :], Ey[j, :], Ed[j, :],
                                                  sfac*np.cos(t[i]))
                        lines[j].set_data(xdi, ydi)

                    # plt.plot(xcdi, ycdi, fmt_interp)

                return lines

            anim = FuncAnimation(fig, animate, init_func=init,
                                 frames=n_frames, interval=50, blit=True,
                                 repeat=False)

        # plt.axis('equal')
        # plt.show()  # call this from main py file for more control

    # 2d triangular elements - todo
    # elif nen == 3:
    #     x = ex+sfac*ed[:, [0, 2, 4]]
    #     y = ex+sfac*ed[:, [1, 3, 5]]
    #     xc = [x, x[0, :]]
    #     yc = [x, x[0, :]]

    # 2d quadrilateral (quad) elements
    elif nen == 4:
        for ele_tag in ele_tags:
            nd1, nd2, nd3, nd4 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1]])

            if modeNo:
                ed = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
                               ops.nodeEigenvector(nd1, modeNo)[1],
                               ops.nodeEigenvector(nd2, modeNo)[0],
                               ops.nodeEigenvector(nd2, modeNo)[1],
                               ops.nodeEigenvector(nd3, modeNo)[0],
                               ops.nodeEigenvector(nd3, modeNo)[1],
                               ops.nodeEigenvector(nd4, modeNo)[0],
                               ops.nodeEigenvector(nd4, modeNo)[1]])
            else:
                ed = np.array([ops.nodeDisp(nd1)[0],
                               ops.nodeDisp(nd1)[1],
                               ops.nodeDisp(nd2)[0],
                               ops.nodeDisp(nd2)[1],
                               ops.nodeDisp(nd3)[0],
                               ops.nodeDisp(nd3)[1],
                               ops.nodeDisp(nd4)[0],
                               ops.nodeDisp(nd4)[1]])

            if unDefoFlag:
                plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]),
                         fmt_undefo)

            # xcdi, ycdi = beam_defo_interp_2d(ex, ey, ed, sfac, nep)
            # xdi, ydi = beam_disp_ends(ex, ey, ed, sfac)
            # # interpolated displacement field
            # plt.plot(xcdi, ycdi, 'b.-')
            # # translations of ends only
            # plt.plot(xdi, ydi, 'ro')

            # test it with one element
            x = ex+sfac*ed[[0, 2, 4, 6]]
            y = ey+sfac*ed[[1, 3, 5, 7]]
            plt.plot(np.append(x, x[0]), np.append(y, y[0]), 'b.-')

        plt.axis('equal')

    # 2d 8-node quadratic elements
    # elif nen == 8:
    #     x = ex+sfac*ed[:, [0, 2, 4, 6, 8, 10, 12, 14]]
    #     y = ex+sfac*ed[:, [1, 3, 5, 7, 9, 11, 13, 15]]

    #     t = -1
    #     n = 0
    #     for s in range(-1, 1.4, 0.4):
    #         n += 1
    #     ...

    else:
        print(f'\nWarning! Elements not supported yet. nen: {nen}; must be: 2, 3, 4, 8.')  # noqa: E501

    return anim


def anim_mode(modeNo, sfac=False, nep=17, unDefoFlag=1, fmt_defo=fmt_defo,
              fmt_undefo=fmt_undefo, interpFlag=1, endDispFlag=1,
              fmt_interp=fmt_interp, fmt_nodes='b-', Eo=0, az_el=az_el,
              fig_wi_he=fig_wi_he, fig_lbrt=fig_lbrt, xlim=[0, 1], ylim=[0, 1],
              lw=3.):
    """Make animation of a mode shape obtained from eigenvalue solution.

    Args:
        modeNo (int): indicates which mode shape to animate.

        sfac (float): scale factor

        nep (integer): number of evaluation points inside the element and
            including both element ends

        unDefoFlag (integer): 1 - plot the undeformed model (mesh), 0 - do not
            plot the mesh

        interpFlag (integer): 1 - interpolate deformation inside element,
            0 - no interpolation

        endDispFlag (integer): 1 - plot marks at element ends, 0 - no marks

        fmt_interp (string): format line string for interpolated (continuous)
            deformated shape. The format contains information on line color,
            style and marks as in the standard matplotlib plot function.

        fmt_nodes (string): format string for the marks of element ends

        az_el (tuple): a tuple containing the azimuth and elevation

        fig_lbrt (tuple): a tuple contating left, bottom, right and top offsets

        fig_wi_he (tuple): contains width and height of the figure

    Examples:
        sfac_a = 100.
        Eds = np.zeros((n_steps, nel, 6))
        timeV = np.zeros(n_steps)

        for step in range(n_steps):
            ops.analyze(1, dt)
            timeV[step] = ops.getTime()
            # collect disp for element nodes
            for el_i, ele_tag in enumerate(el_tags):
                nd1, nd2 = ops.eleNodes(ele_tag)
                # uAll[step, inode, 0] = ops.nodeDisp()
                Eds[step, el_i, :] = np.array([ops.nodeDisp(nd1)[0],
                                               ops.nodeDisp(nd1)[1],
                                               ops.nodeDisp(nd1)[2],
                                               ops.nodeDisp(nd2)[0],
                                               ops.nodeDisp(nd2)[1],
                                               ops.nodeDisp(nd2)[2]])
        fw = 20.
        fh = 1.2 * 4./6. * fw

        anim = opsv.anim_defo(Eds, timeV, sfac_a, interpFlag=1, xlim=[-1, 7],
                              ylim=[-1, 5], fig_wi_he=(fw, fh))

    Notes:

    See also:
        anim_mode()
    """

    node_tags = ops.getNodeTags()

    # calculate sfac
    # min_x, min_y, min_z = np.inf, np.inf, np.inf
    # max_x, max_y, max_z = -np.inf, -np.inf, -np.inf
    # max_ux, max_uy, max_uz = -np.inf, -np.inf, -np.inf
    min_x, min_y = np.inf, np.inf
    max_x, max_y = -np.inf, -np.inf
    max_ux, max_uy = -np.inf, -np.inf
    ratio = 0.1

    ndim = np.shape(ops.nodeCoord(node_tags[0]))[0]

    if ndim == 2:
        if not sfac:
            for node_tag in node_tags:
                x_crd = ops.nodeCoord(node_tag)[0]
                y_crd = ops.nodeCoord(node_tag)[1]
                ux = ops.nodeEigenvector(node_tag, modeNo)[0]
                uy = ops.nodeEigenvector(node_tag, modeNo)[1]

                min_x = min(min_x, x_crd)
                min_y = min(min_y, y_crd)
                max_x = max(max_x, x_crd)
                max_y = max(max_y, y_crd)
                max_ux = max(max_ux, np.abs(ux))
                max_uy = max(max_uy, np.abs(uy))

            dxmax = max_x - min_x
            dymax = max_y - min_y
            dlmax = max(dxmax, dymax)
            edmax = max(max_ux, max_uy)
            sfac = ratio * dlmax/edmax

        anim = _anim_mode_2d(modeNo, sfac, nep, unDefoFlag, fmt_defo,
                             fmt_undefo, interpFlag, endDispFlag, fmt_interp,
                             fmt_nodes, fig_wi_he, xlim, ylim, lw)

    # elif ndim == 3:
    #     if not sfac:
    #         for node_tag in node_tags:
    #             x_crd = ops.nodeCoord(node_tag)[0]
    #             y_crd = ops.nodeCoord(node_tag)[1]
    #             z_crd = ops.nodeCoord(node_tag)[2]
    #             ux = ops.nodeEigenvector(node_tag, modeNo)[0]
    #             uy = ops.nodeEigenvector(node_tag, modeNo)[1]
    #             uz = ops.nodeEigenvector(node_tag, modeNo)[2]

    #             min_x = min(min_x, x_crd)
    #             min_y = min(min_y, y_crd)
    #             min_z = min(min_z, z_crd)
    #             max_x = max(max_x, x_crd)
    #             max_y = max(max_y, y_crd)
    #             max_z = max(max_z, z_crd)
    #             max_ux = max(max_ux, np.abs(ux))
    #             max_uy = max(max_uy, np.abs(uy))
    #             max_uz = max(max_uz, np.abs(uz))

    #         dxmax = max_x - min_x
    #         dymax = max_y - min_y
    #         dzmax = max_z - min_z
    #         dlmax = max(dxmax, dymax, dzmax)
    #         edmax = max(max_ux, max_uy, max_uz)
    #         sfac = ratio * dlmax/edmax

    #     _plot_defo_mode_3d(modeNo, sfac, nep, unDefoFlag, fmt_defo,
    #                        fmt_undefo, interpFlag, endDispFlag, fmt_interp,
    #                         fmt_nodes, Eo, az_el, fig_wi_he, fig_lbrt)

    else:
        print(f'\nWarning! ndim: {ndim} not supported yet.')

    return anim


def plot_mode_shape(modeNo, sfac=False, nep=17, unDefoFlag=1,
                    fmt_undefo=fmt_undefo, interpFlag=1, endDispFlag=1,
                    fmt_interp=fmt_interp, fmt_nodes=fmt_nodes, Eo=0,
                    az_el=az_el, fig_wi_he=fig_wi_he, fig_lbrt=fig_lbrt):
    """Plot mode shape of the structure obtained from eigenvalue analysis.

    Args:
        modeNo (int): indicates which mode shape to plot

        sfac (float): scale factor to increase/decrease displacements obtained
            from FE analysis. If not specified (False), sfac is automatically
            calculated based on the maximum overall displacement and this
            maximum displacement is plotted as 20 percent (hordcoded) of
            the maximum model dimension.

        interpFlag (int): 1 - use interpolated deformation using shape
            function, 0 - do not use interpolation, just show displaced element
            nodes (default is 1)

        nep (int): number of evaluation points for shape function interpolation
            (default: 17)

    Usage:

    ``plot_mode_shape(1)`` - plot the first mode shape with default parameters
    and automatically calcutated scale factor.

    ``plot_mode_shape(2, interpFlag=0)`` - plot the 2nd mode shape by
    displacing the nodes connected with straight lines (shape function
    interpolation)

    ``plot_mode_shape(3, sfac=1.5)`` - plot the 3rd mode shape with specified
    scale factor

    ``plot_mode_shape(4, unDefoFlag=0, endDispFlag=0)`` - plot the 4th mode
    shape without showing undeformed (original) mesh and without showing
    markers at the element ends.

    Examples:

    Notes:

    See also:
    """

    node_tags = ops.getNodeTags()

    # calculate sfac
    min_x, min_y, min_z = np.inf, np.inf, np.inf
    max_x, max_y, max_z = -np.inf, -np.inf, -np.inf
    max_ux, max_uy, max_uz = -np.inf, -np.inf, -np.inf
    ratio = 0.1

    ndim = np.shape(ops.nodeCoord(node_tags[0]))[0]

    if ndim == 2:
        if not sfac:
            for node_tag in node_tags:
                x_crd = ops.nodeCoord(node_tag)[0]
                y_crd = ops.nodeCoord(node_tag)[1]
                ux = ops.nodeEigenvector(node_tag, modeNo)[0]
                uy = ops.nodeEigenvector(node_tag, modeNo)[1]

                min_x = min(min_x, x_crd)
                min_y = min(min_y, y_crd)
                max_x = max(max_x, x_crd)
                max_y = max(max_y, y_crd)
                max_ux = max(max_ux, np.abs(ux))
                max_uy = max(max_uy, np.abs(uy))

            dxmax = max_x - min_x
            dymax = max_y - min_y
            dlmax = max(dxmax, dymax)
            edmax = max(max_ux, max_uy)
            sfac = ratio * dlmax/edmax

        _plot_defo_mode_2d(modeNo, sfac, nep, unDefoFlag, fmt_defo, fmt_undefo,
                           interpFlag, endDispFlag, fmt_interp, fmt_nodes)

    elif ndim == 3:
        if not sfac:
            for node_tag in node_tags:
                x_crd = ops.nodeCoord(node_tag)[0]
                y_crd = ops.nodeCoord(node_tag)[1]
                z_crd = ops.nodeCoord(node_tag)[2]
                ux = ops.nodeEigenvector(node_tag, modeNo)[0]
                uy = ops.nodeEigenvector(node_tag, modeNo)[1]
                uz = ops.nodeEigenvector(node_tag, modeNo)[2]

                min_x = min(min_x, x_crd)
                min_y = min(min_y, y_crd)
                min_z = min(min_z, z_crd)
                max_x = max(max_x, x_crd)
                max_y = max(max_y, y_crd)
                max_z = max(max_z, z_crd)
                max_ux = max(max_ux, np.abs(ux))
                max_uy = max(max_uy, np.abs(uy))
                max_uz = max(max_uz, np.abs(uz))

            dxmax = max_x - min_x
            dymax = max_y - min_y
            dzmax = max_z - min_z
            dlmax = max(dxmax, dymax, dzmax)
            edmax = max(max_ux, max_uy, max_uz)
            sfac = ratio * dlmax/edmax

        _plot_defo_mode_3d(modeNo, sfac, nep, unDefoFlag, fmt_defo, fmt_undefo,
                           interpFlag, endDispFlag, fmt_interp, fmt_nodes,
                           az_el, fig_wi_he, fig_lbrt)

    else:
        print(f'\nWarning! ndim: {ndim} not supported yet.')


def rot_transf_3d(ex, ey, ez, g):

    Lxyz = np.array([ex[1]-ex[0], ey[1]-ey[0], ez[1]-ez[0]])

    L = np.sqrt(Lxyz @ Lxyz)

    z = np.zeros((3, 3))

    G = np.block([[g, z, z, z],
                  [z, g, z, z],
                  [z, z, g, z],
                  [z, z, z, g]])

    return G, L


def beam_defo_interp_2d(ex, ey, u, sfac, nep=17):
    """
    Interpolate element displacements at nep points.

    Parametrs:
    ex, ey : element x, y coordinates,
    u : element nodal displacements
    sfac : scale factor for deformation plot
    nep : number of evaluation points (including end nodes)

    Returns:
    crd_xc, crd_yc : x, y coordinates of interpolated (at nep points)
    beam deformation required for plot_defo() function
    """

    Lxy = np.array([ex[1]-ex[0], ey[1]-ey[0]])
    L = np.sqrt(Lxy @ Lxy)
    cosa, cosb = Lxy / L
    G = np.array([[cosa,  cosb, 0., 0.,    0.,   0.],
                  [-cosb, cosa, 0., 0.,    0.,   0.],
                  [0.,    0.,   1., 0.,    0.,   0.],
                  [0.,    0.,   0., cosa,  cosb, 0.],
                  [0.,    0.,   0., -cosb, cosa, 0.],
                  [0.,    0.,   0., 0.,    0.,   1.]])

    u_l = G @ u
    xl = np.linspace(0., L, num=nep)
    one = np.ones(xl.shape)

    # longitudinal deformation (1)
    N_a = np.column_stack((one - xl/L, xl/L))
    u_ac = N_a @ np.array([u_l[0], u_l[3]])

    # transverse deformation (2)
    N_t = np.column_stack((one - 3*xl**2/L**2 + 2*xl**3/L**3,
                           xl - 2*xl**2/L + xl**3/L**2,
                           3*xl**2/L**2 - 2*xl**3/L**3,
                           -xl**2/L + xl**3/L**2))

    u_tc = N_t @ np.array([u_l[1], u_l[2], u_l[4], u_l[5]])

    # combined two row vectors
    # 1-st vector longitudinal deformation (1)
    # 2-nd vector transverse deformation (2)
    u_atc = np.vstack((u_ac, u_tc))

    # project longitudinal (u_ac) and transverse deformation
    # (local u and v) to (global u and v)
    G1 = np.array([[cosa, -cosb],
                   [cosb, cosa]])

    u_xyc = G1 @ u_atc

    # discretize element coordinates
    # first  row = X + [0 dx 2dx ... 4-dx 4]
    # second row = Y + [0 dy 2dy ... 3-dy 3]
    xy_c = np.vstack((np.linspace(ex[0], ex[1], num=nep),
                      np.linspace(ey[0], ey[1], num=nep)))

    # Continuous x, y displacement coordinates
    crd_xc = xy_c[0, :] + sfac * u_xyc[0, :]
    crd_yc = xy_c[1, :] + sfac * u_xyc[1, :]
    # latex_array(ecrd_xc)
    # latex_array(ecrd_yc)

    return crd_xc, crd_yc


def beam_defo_interp_3d(ex, ey, ez, g, u, sfac, nep=17):
    """
    3d beam version of beam_defo_interp_2d.
    """
    G, L = rot_transf_3d(ex, ey, ez, g)
    ul = G @ u

    _, crd_yc = beam_defo_interp_2d(np.array([0., L]),
                                    np.array([0., 0.]),
                                    np.array([ul[0], ul[1], ul[5], ul[6],
                                              ul[7], ul[11]]), sfac, nep)
    crd_xc, crd_zc = beam_defo_interp_2d(np.array([0., L]),
                                         np.array([0., 0.]),
                                         np.array([ul[0], ul[2], -ul[4], ul[6],
                                                   ul[8], -ul[10]]), sfac, nep)

    xl = np.linspace(0., L, num=nep)
    crd_xc = crd_xc - xl

    crd_xyzc = np.vstack([crd_xc, crd_yc, crd_zc])

    u_xyzc = np.transpose(g) @ crd_xyzc

    xyz_c = np.vstack((np.linspace(ex[0], ex[1], num=nep),
                       np.linspace(ey[0], ey[1], num=nep),
                       np.linspace(ez[0], ez[1], num=nep)))

    crd_xc = xyz_c[0, :] + u_xyzc[0, :]
    crd_yc = xyz_c[1, :] + u_xyzc[1, :]
    crd_zc = xyz_c[2, :] + u_xyzc[2, :]

    return crd_xc, crd_yc, crd_zc


def beam_disp_ends(ex, ey, d, sfac):
    """
    Calculate the element deformation at element ends only.
    """

    #  indx: 0   1   2   3   4   5
    # Ed = ux1 uy1 ur1 ux2 uy2 ur2
    exd = np.array([ex[0] + sfac*d[0], ex[1] + sfac*d[3]])
    eyd = np.array([ey[0] + sfac*d[1], ey[1] + sfac*d[4]])

    return exd, eyd


def beam_disp_ends3d(ex, ey, ez, d, sfac):
    """
    Calculate the element deformation at element ends only.
    """

    #  indx: 0   1   2   3   4   5   6   7   8   9  10  11
    # Ed = ux1 uy1 uz1 rx1 ry1 rz1 ux2 uy2 uz2 rx2 ry2 rz2
    exd = np.array([ex[0] + sfac*d[0], ex[1] + sfac*d[6]])
    eyd = np.array([ey[0] + sfac*d[1], ey[1] + sfac*d[7]])
    ezd = np.array([ez[0] + sfac*d[2], ez[1] + sfac*d[8]])

    return exd, eyd, ezd


def plot_fiber_section(fib_sec_list, fillflag=1,
                       matcolor=['y', 'b', 'r', 'g', 'm', 'k']):
    """Plot fiber cross-section.

    Args:
        fib_sec_list (list): list of lists in the format similar to the parameters
            for the section, layer, patch, fiber OpenSees commands

        fillflag (int): 1 - filled fibers with color specified in matcolor
            list, 0 - no color, only the outline of fibers

        matcolor (list): sequence of colors for various material tags
            assigned to fibers

    Examples:
        ::

            fib_sec_1 = [['section', 'Fiber', 1, '-GJ', 1.0e6],
                         ['patch', 'quad', 1, 4, 1,  0.032, 0.317, -0.311, 0.067, -0.266, 0.005, 0.077, 0.254],  # noqa: E501
                         ['patch', 'quad', 1, 1, 4,  -0.075, 0.144, -0.114, 0.116, 0.075, -0.144, 0.114, -0.116],  # noqa: E501
                         ['patch', 'quad', 1, 4, 1,  0.266, -0.005,  -0.077, -0.254,  -0.032, -0.317,  0.311, -0.067]  # noqa: E501
                         ]
            opsv.fib_sec_list_to_cmds(fib_sec_1)
            matcolor = ['r', 'lightgrey', 'gold', 'w', 'w', 'w']
            opsv.plot_fiber_section(fib_sec_1, matcolor=matcolor)
            plt.axis('equal')
            # plt.savefig('fibsec_rc.png')
            plt.show()

    Notes:
        ``fib_sec_list`` can be reused by means of a python helper function
            ``ops_vis.fib_sec_list_to_cmds(fib_sec_list_1)``

    See also:
        ``ops_vis.fib_sec_list_to_cmds()``
    """

    fig, ax = plt.subplots()
    ax.set_xlabel('z')
    ax.set_ylabel('y')
    ax.grid(False)

    for item in fib_sec_list:

        if item[0] == 'layer':
            matTag = item[2]
            if item[1] == 'straight':
                n_bars = item[3]
                As = item[4]
                Iy, Iz, Jy, Jz = item[5], item[6], item[7], item[8]
                r = np.sqrt(As / np.pi)
                Y = np.linspace(Iy, Jy, n_bars)
                Z = np.linspace(Iz, Jz, n_bars)
                for zi, yi in zip(Z, Y):
                    bar = Circle((zi, yi), r, ec='k', fc='k', zorder=10)
                    ax.add_patch(bar)
            if item[1] == 'circ':
                n_bars, As = item[3], item[4]
                yC, zC, arc_radius = item[5], item[6], item[7]
                if len(item) > 8:
                    a0_deg, a1_deg = item[8], item[9]
                else:
                    a0_deg, a1_deg = 0., 360. - 360./n_bars

                a0_rad, a1_rad = np.pi * a0_deg / 180., np.pi * a1_deg / 180.
                r_bar = np.sqrt(As / np.pi)
                thetas = np.linspace(a0_rad, a1_rad, n_bars)
                Y = yC + arc_radius * np.cos(thetas)
                Z = zC + arc_radius * np.sin(thetas)
                for zi, yi in zip(Z, Y):
                    bar = Circle((zi, yi), r_bar, ec='k', fc='k', zorder=10)
                    ax.add_patch(bar)

        if (item[0] == 'patch' and (item[1] == 'quad' or item[1] == 'quadr' or
                                  item[1] == 'rect')):
            matTag, nIJ, nJK = item[2], item[3], item[4]

            if item[1] == 'quad' or item[1] == 'quadr':
                Iy, Iz, Jy, Jz = item[5], item[6], item[7], item[8]
                Ky, Kz, Ly, Lz = item[9], item[10], item[11], item[12]

            if item[1] == 'rect':
                Iy, Iz, Ky, Kz = item[5], item[6], item[7], item[8]
                Jy, Jz, Ly, Lz = Ky, Iz, Iy, Kz

            # check for convexity (vector products)
            outIJxIK = (Jy-Iy)*(Kz-Iz) - (Ky-Iy)*(Jz-Iz)
            outIKxIL = (Ky-Iy)*(Lz-Iz) - (Ly-Iy)*(Kz-Iz)
            # check if I, J, L points are colinear
            outIJxIL = (Jy-Iy)*(Lz-Iz) - (Ly-Iy)*(Jz-Iz)
            # outJKxJL = (Ky-Jy)*(Lz-Jz) - (Ly-Jy)*(Kz-Jz)

            if outIJxIK <= 0 or outIKxIL <= 0 or outIJxIL <= 0:
                print('\nWarning! Patch quad is non-convex or counter-clockwise defined or has at least 3 colinear points in line')  # noqa: E501

            IJz, IJy = np.linspace(Iz, Jz, nIJ+1), np.linspace(Iy, Jy, nIJ+1)
            JKz, JKy = np.linspace(Jz, Kz, nJK+1), np.linspace(Jy, Ky, nJK+1)
            LKz, LKy = np.linspace(Lz, Kz, nIJ+1), np.linspace(Ly, Ky, nIJ+1)
            ILz, ILy = np.linspace(Iz, Lz, nJK+1), np.linspace(Iy, Ly, nJK+1)

            if fillflag:
                Z = np.zeros((nIJ+1, nJK+1))
                Y = np.zeros((nIJ+1, nJK+1))

                for j in range(nIJ+1):
                    Z[j, :] = np.linspace(IJz[j], LKz[j], nJK+1)
                    Y[j, :] = np.linspace(IJy[j], LKy[j], nJK+1)

                for j in range(nIJ):
                    for k in range(nJK):
                        zy = np.array([[Z[j, k], Y[j, k]],
                                       [Z[j, k+1], Y[j, k+1]],
                                       [Z[j+1, k+1], Y[j+1, k+1]],
                                       [Z[j+1, k], Y[j+1, k]]])
                        poly = Polygon(zy, True, ec='k', fc=matcolor[matTag-1])
                        ax.add_patch(poly)

            else:
                # horizontal lines
                for az, bz, ay, by in zip(IJz, LKz, IJy, LKy):
                    plt.plot([az, bz], [ay, by], 'b-', zorder=1)

                # vertical lines
                for az, bz, ay, by in zip(JKz, ILz, JKy, ILy):
                    plt.plot([az, bz], [ay, by], 'b-', zorder=1)

        if item[0] == 'patch' and item[1] == 'circ':
            matTag, nc, nr = item[2], item[3], item[4]

            yC, zC, ri, re = item[5], item[6], item[7], item[8]
            a0, a1 = item[9], item[10]

            dr = (re - ri) / nr
            dth = (a1 - a0) / nc

            for j in range(nr):
                rj = ri + j * dr
                rj1 = rj + dr

                for i in range(nc):
                    thi = a0 + i * dth
                    thi1 = thi + dth
                    wedge = Wedge((yC, zC), rj1, thi, thi1, width=dr, ec='k',
                                  lw=1, fc=matcolor[matTag-1])
                    ax.add_patch(wedge)

            ax.axis('equal')


def fib_sec_list_to_cmds(fib_sec_list):
    """Reuses fib_sec_list to define fiber section in OpenSees.

    At present it is not possible to extract fiber section data from
    the OpenSees domain, this function is a workaround. The idea is to
    prepare data similar to the one the regular OpenSees commands
    (``section('Fiber', ...)``, ``fiber()``, ``patch()`` and/or
    ``layer()``) require.

    Args:
        fib_sec_list (list): is a list of fiber section data. First sub-list
        also defines the torsional stiffness (GJ).

    Warning:

    If you use this function, do not issue the regular OpenSees:
    section, Fiber, Patch or Layer commands.

    See also:

    ``ops_vis.plot_fiber_section()``

    """
    for dat in fib_sec_list:
        if dat[0] == 'section':
            secTag, GJ = dat[2], dat[4]
            ops.section('Fiber', secTag, '-GJ', GJ)

        if dat[0] == 'layer':
            matTag = dat[2]
            if dat[1] == 'straight':
                n_bars = dat[3]
                As = dat[4]
                Iy, Iz, Jy, Jz = dat[5], dat[6], dat[7], dat[8]
                ops.layer('straight', matTag, n_bars, As, Iy, Iz, Jy, Jz)

        if dat[0] == 'patch':
            matTag = dat[2]
            nIJ = dat[3]
            nJK = dat[4]

            if dat[1] == 'quad' or dat[1] == 'quadr':
                Iy, Iz, Jy, Jz = dat[5], dat[6], dat[7], dat[8]
                Ky, Kz, Ly, Lz = dat[9], dat[10], dat[11], dat[12]
                ops.patch('quad', matTag, nIJ, nJK, Iy, Iz, Jy, Jz, Ky, Kz,
                          Ly, Lz)

            if dat[1] == 'rect':
                Iy, Iz, Ky, Kz = dat[5], dat[6], dat[7], dat[8]
                Jy, Jz, Ly, Lz = Ky, Iz, Iy, Kz
                ops.patch('rect', matTag, nIJ, nJK, Iy, Iz, Ky, Kz)


def _anim_defo_2d(Eds, timeV, sfac, nep, unDefoFlag, fmt_defo, fmt_undefo,
                  interpFlag, endDispFlag, fmt_interp, fmt_nodes, fig_wi_he,
                  xlim, ylim):

    fig_wi, fig_he = fig_wi_he
    ele_tags = ops.getEleTags()

    nen = np.shape(ops.eleNodes(ele_tags[0]))[0]

    # truss and beam/frame elements
    if nen == 2:

        ndf = np.shape(ops.nodeDOFs(ops.eleNodes(ele_tags[0])[0]))[0]

        # truss element
        if ndf == 2:

            for ele_tag in ele_tags:
                nd1, nd2 = ops.eleNodes(ele_tag)

                # element x, y coordinates
                ex = np.array([ops.nodeCoord(nd1)[0],
                               ops.nodeCoord(nd2)[0]])
                ey = np.array([ops.nodeCoord(nd1)[1],
                               ops.nodeCoord(nd2)[1]])

                eux = np.array([ops.nodeDisp(nd1)[0],
                                ops.nodeDisp(nd2)[0]])
                euy = np.array([ops.nodeDisp(nd1)[1],
                                ops.nodeDisp(nd2)[1]])

                # displaced element coordinates (scaled by sfac factor)
                edx = np.array([ex[0] + sfac*eux[0], ex[1] + sfac*eux[1]])
                edy = np.array([ey[0] + sfac*euy[0], ey[1] + sfac*euy[1]])

                if unDefoFlag:
                    plt.plot(ex, ey, fmt_undefo)

                plt.plot(edx, edy, fmt_interp)

        # beam/frame element anim defo
        elif ndf == 3:

            fig, ax = plt.subplots(figsize=(fig_wi/2.54, fig_he/2.54))
            ax.axis('equal')
            ax.set_xlim(xlim[0], xlim[1])
            ax.set_ylim(ylim[0], ylim[1])
            # ax.grid()

            nel = len(ele_tags)
            Ex = np.zeros((nel, 2))
            Ey = np.zeros((nel, 2))
            # no of frames equal to time intervals
            n_frames, _, _ = np.shape(Eds)
            lines = []

            # time_text = ax.set_title('')  # does not work
            time_text = ax.text(.05, .95, '', transform=ax.transAxes)
            for i, ele_tag in enumerate(ele_tags):
                nd1, nd2 = ops.eleNodes(ele_tag)

                # element x, y coordinates
                Ex[i, :] = np.array([ops.nodeCoord(nd1)[0],
                                     ops.nodeCoord(nd2)[0]])
                Ey[i, :] = np.array([ops.nodeCoord(nd1)[1],
                                     ops.nodeCoord(nd2)[1]])

                lines.append(ax.plot([], [], fmt_nodes, lw=3)[0])

            def init():
                for j, ele_tag in enumerate(ele_tags):
                    lines[j].set_data([], [])

                time_text.set_text('')

                return tuple(lines) + (time_text,)

            def animate(i):
                for j, ele_tag in enumerate(ele_tags):

                    if interpFlag:
                        xcdi, ycdi = beam_defo_interp_2d(Ex[j, :],
                                                         Ey[j, :],
                                                         Eds[i, j, :],
                                                         sfac,
                                                         nep)
                        lines[j].set_data(xcdi, ycdi)
                    else:
                        xdi, ydi = beam_disp_ends(Ex[j, :], Ey[j, :],
                                                  Eds[i, j, :], sfac)
                        lines[j].set_data(xdi, ydi)

                    # plt.plot(xcdi, ycdi, fmt_interp)

                # time_text.set_text(f'f')
                time_text.set_text(f'frame: {i+1}/{n_frames}, \
time: {timeV[i]:.3f} s')

                return tuple(lines) + (time_text,)

            anim = FuncAnimation(fig, animate, init_func=init, frames=n_frames,
                                 interval=50, blit=True, repeat=False)

        # plt.axis('equal')
        # plt.show()  # call this from main py file for more control

    # 2d triangular elements
    # elif nen == 3:
    #     x = ex+sfac*ed[:, [0, 2, 4]]
    #     y = ex+sfac*ed[:, [1, 3, 5]]
    #     xc = [x, x[0, :]]
    #     yc = [x, x[0, :]]

    # 2d quadrilateral (quad) elements
    elif nen == 4:
        for ele_tag in ele_tags:
            nd1, nd2, nd3, nd4 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0],
                           ops.nodeCoord(nd4)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1],
                           ops.nodeCoord(nd4)[1]])

            # if modeNo:
            #     ed = np.array([ops.nodeEigenvector(nd1, modeNo)[0],
            #                    ops.nodeEigenvector(nd1, modeNo)[1],
            #                    ops.nodeEigenvector(nd2, modeNo)[0],
            #                    ops.nodeEigenvector(nd2, modeNo)[1],
            #                    ops.nodeEigenvector(nd3, modeNo)[0],
            #                    ops.nodeEigenvector(nd3, modeNo)[1],
            #                    ops.nodeEigenvector(nd4, modeNo)[0],
            #                    ops.nodeEigenvector(nd4, modeNo)[1]])
            # else:
            ed = np.array([ops.nodeDisp(nd1)[0],
                           ops.nodeDisp(nd1)[1],
                           ops.nodeDisp(nd2)[0],
                           ops.nodeDisp(nd2)[1],
                           ops.nodeDisp(nd3)[0],
                           ops.nodeDisp(nd3)[1],
                           ops.nodeDisp(nd4)[0],
                           ops.nodeDisp(nd4)[1]])

            if unDefoFlag:
                plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]),
                         fmt_undefo)

            # xcdi, ycdi = beam_defo_interp_2d(ex, ey, ed, sfac, nep)
            # xdi, ydi = beam_disp_ends(ex, ey, ed, sfac)
            # # interpolated displacement field
            # plt.plot(xcdi, ycdi, 'b.-')
            # # translations of ends only
            # plt.plot(xdi, ydi, 'ro')

            # test it with one element
            x = ex+sfac*ed[[0, 2, 4, 6]]
            y = ey+sfac*ed[[1, 3, 5, 7]]
            plt.plot(np.append(x, x[0]), np.append(y, y[0]), 'b.-')

        plt.axis('equal')

    # 2d 8-node quadratic elements
    # elif nen == 8:
    #     x = ex+sfac*ed[:, [0, 2, 4, 6, 8, 10, 12, 14]]
    #     y = ex+sfac*ed[:, [1, 3, 5, 7, 9, 11, 13, 15]]

    #     t = -1
    #     n = 0
    #     for s in range(-1, 1.4, 0.4):
    #         n += 1
    #     ...

    else:
        print(f'\nWarning! Elements not supported yet. nen: {nen}; must be: 2, 3, 4, 8.')  # noqa: E501

    return anim


def anim_defo(Eds, timeV, sfac, nep=17, unDefoFlag=1, fmt_defo=fmt_defo,
              fmt_undefo=fmt_undefo, interpFlag=1, endDispFlag=1,
              fmt_interp=fmt_interp, fmt_nodes='b-', az_el=az_el,
              fig_lbrt=fig_lbrt, fig_wi_he=fig_wi_he, xlim=[0, 1],
              ylim=[0, 1]):
    """Make animation of the deformed shape computed by transient analysis

    Args:
        Eds (ndarray): A 3d array (n_steps x n_eles x n_dof_per_element)
            containing the collected displacements per element for all
            time steps.

        timeV (1darray): vector of discretized time values

        sfac (float): scale factor

        nep (integer): number of evaluation points inside the element and
            including both element ends

        unDefoFlag (integer): 1 - plot the undeformed model (mesh), 0 - do not
            plot the mesh

        interpFlag (integer): 1 - interpolate deformation inside element,
            0 - no interpolation

        endDispFlag (integer): 1 - plot marks at element ends, 0 - no marks

        fmt_interp (string): format line string for interpolated (continuous)
            deformated shape. The format contains information on line color,
            style and marks as in the standard matplotlib plot function.

        fmt_nodes (string): format string for the marks of element ends

        az_el (tuple): a tuple containing the azimuth and elevation

        fig_lbrt (tuple): a tuple contating left, bottom, right and top offsets

        fig_wi_he (tuple): contains width and height of the figure

    Examples:

    Notes:

    See also:
    """

    node_tags = ops.getNodeTags()

    ndim = np.shape(ops.nodeCoord(node_tags[0]))[0]

    if ndim == 2:
        anim = _anim_defo_2d(Eds, timeV, sfac, nep, unDefoFlag, fmt_defo,
                             fmt_undefo, interpFlag, endDispFlag, fmt_interp,
                             fmt_nodes, fig_wi_he, xlim, ylim)

    else:
        print(f'\nWarning! ndim: {ndim} not supported yet.')

    return anim


def section_force_distribution_2d(ex, ey, pl, nep=2,
                                  ele_load_data=['-beamUniform', 0., 0.]):
    """
    Calculate section forces (N, V, M) for an elastic 2D Euler-Bernoulli beam.

    Input:
    ex, ey - x, y element coordinates in global system
    nep - number of evaluation points, by default (2) at element ends
    ele_load_list - list of transverse and longitudinal element load
      syntax: [ele_load_type, Wy, Wx]
      For now only '-beamUniform' element load type is acceptable

    Output:
    s = [N V M]; shape: (nep,3)
        section forces at nep points along local x
    xl: coordinates of local x-axis; shape: (nep,)

    Use it with dia_sf to draw N, V, M diagrams.

    TODO: add '-beamPoint' element load type
    """

    # eload_type, Wy, Wx = ele_load_data[0], ele_load_data[1], ele_load_data[2]
    Wy, Wx = ele_load_data[1], ele_load_data[2]

    nlf = len(pl)
    if nlf == 2:  # trusses
        N_1 = pl[0]
    elif nlf == 6:  # plane frames
        # N_1, V_1, M_1 = pl[0], pl[1], pl[2]
        N_1, V_1, M_1 = pl[:3]
    else:
        print('\nWarning! Not supported. Number of nodal forces: {nlf}')

    Lxy = np.array([ex[1]-ex[0], ey[1]-ey[0]])
    L = np.sqrt(Lxy @ Lxy)

    xl = np.linspace(0., L, nep)
    one = np.ones(nep)

    N = -1.*(N_1 * one + Wx * xl)

    if nlf == 6:
        V = V_1 * one + Wy * xl
        M = -M_1 * one + V_1 * xl + 0.5 * Wy * xl**2
        s = np.column_stack((N, V, M))
    elif nlf == 2:
        s = np.column_stack((N))

    # if eload_type == '-beamUniform':
    # else:

    return s, xl


def section_force_distribution_3d(ex, ey, ez, pl, nep=2,
                                  ele_load_data=['-beamUniform', 0., 0., 0.]):
    """
    Calculate section forces (N, Vy, Vz, T, My, Mz) for an elastic 3d beam.

    Longer description

    Parameters
    ----------

    ex : list
        x element coordinates
    ey : list
        y element coordinates
    ez : list
        z element coordinates
    pl : ndarray
    nep : int
        number of evaluation points, by default (2) at element ends

    ele_load_list : list
        list of transverse and longitudinal element load
        syntax: [ele_load_type, Wy, Wz, Wx]
        For now only '-beamUniform' element load type is acceptable.

    Returns
    -------

    s : ndarray
        [N Vx Vy T My Mz]; shape: (nep,6)
        column vectors of section forces along local x-axis

    uvwfi : ndarray
        [u v w fi]; shape (nep,4)
        displacements at nep points along local x

    xl : ndarray
        coordinates of local x-axis; shape (nep,)

    Notes
    -----

    Todo: add '-beamPoint' element load type

    """

    # eload_type = ele_load_data[0]
    Wy, Wz, Wx = ele_load_data[1], ele_load_data[2], ele_load_data[3]

    N1, Vy1, Vz1, T1, My1, Mz1 = pl[:6]

    Lxyz = np.array([ex[1]-ex[0], ey[1]-ey[0], ez[1]-ez[0]])
    L = np.sqrt(Lxyz @ Lxyz)

    xl = np.linspace(0., L, nep)
    one = np.ones(nep)

    N = -1.*(N1*one + Wx*xl)
    Vy = Vy1*one + Wy*xl
    Vz = Vz1*one + Wz*xl
    T = -T1*one
    Mz = -Mz1*one + Vy1*xl + 0.5*Wy*xl**2
    My = My1*one + Vz1*xl + 0.5*Wz*xl**2

    s = np.column_stack((N, Vy, Vz, T, My, Mz))

    return s, xl


def section_force_diagram_2d(sf_type, Ew, sfac=1., nep=17,
                             fmt_secforce=fmt_secforce):
    """Display section forces diagram for 2d beam column model.

    This function plots a section forces diagram for 2d beam column elements
    with or without element loads. For now only '-beamUniform' constant
    transverse or axial element loads are supported.

    Args:
        sf_type (str): type of section force: 'N' - normal force,
            'V' - shear force, 'M' - bending moments.

        Ew (dict): Ew Python dictionary contains information on non-zero
            element loads, therfore each item of the Python dictionary
            is in the form: 'ele_tag: ['-beamUniform', Wy, Wx]'.

        sfac (float): scale factor by wich the values of section forces are
            multiplied.

        nep (int): number of evaluation points including both end nodes
            (default: 17)

        fmt_secforce (str): format line string for section force distribution
            curve. The format contains information on line color, style and
            marks as in the standard matplotlib plot function.
            (default: fmt_secforce = 'b-'  # blue solid line)

    Usage:
    ::

        Wy, Wx = -10.e+3, 0.
        Ew = {3: ['-beamUniform', Wy, Wx]}
        sfacM = 5.e-5
        plt.figure()
        minVal, maxVal = opsv.section_force_diagram_2d('M', Ew, sfacM)
        plt.title('Bending moments')

    Todo:

    Add support for other element loads available in OpenSees: partial
    (trapezoidal) uniform element load, and 'beamPoint' element load.
    """

    maxVal, minVal = -np.inf, np.inf
    ele_tags = ops.getEleTags()

    for ele_tag in ele_tags:

        # by default no element load
        eload_data = ['', 0., 0.]
        if ele_tag in Ew:
            eload_data = Ew[ele_tag]

        nd1, nd2 = ops.eleNodes(ele_tag)

        # element x, y coordinates
        ex = np.array([ops.nodeCoord(nd1)[0],
                       ops.nodeCoord(nd2)[0]])
        ey = np.array([ops.nodeCoord(nd1)[1],
                       ops.nodeCoord(nd2)[1]])

        Lxy = np.array([ex[1]-ex[0], ey[1]-ey[0]])
        L = np.sqrt(Lxy @ Lxy)
        cosa, cosb = Lxy / L

        pl = ops.eleResponse(ele_tag, 'localForces')

        s_all, xl = section_force_distribution_2d(ex, ey, pl, nep, eload_data)

        if sf_type == 'N' or sf_type == 'axial':
            s = s_all[:, 0]
        elif sf_type == 'V' or sf_type == 'shear' or sf_type == 'T':
            s = s_all[:, 1]
        elif sf_type == 'M' or sf_type == 'moment':
            s = s_all[:, 2]

        minVal = min(minVal, np.min(s))
        maxVal = max(maxVal, np.max(s))

        s = s*sfac

        s_0 = np.zeros((nep, 2))
        s_0[0, :] = [ex[0], ey[0]]

        s_0[1:, 0] = s_0[0, 0] + xl[1:] * cosa
        s_0[1:, 1] = s_0[0, 1] + xl[1:] * cosb

        s_p = np.copy(s_0)

        # positive M are opposite to N and V
        if sf_type == 'M' or sf_type == 'moment':
            s *= -1.

        s_p[:, 0] -= s * cosb
        s_p[:, 1] += s * cosa

        plt.axis('equal')

        # section force curve
        plt.plot(s_p[:, 0], s_p[:, 1], fmt_secforce,
                 solid_capstyle='round', solid_joinstyle='round',
                 dash_capstyle='butt', dash_joinstyle='round')

        # model
        plt.plot(ex, ey, 'k-', solid_capstyle='round', solid_joinstyle='round',
                 dash_capstyle='butt', dash_joinstyle='round')

        # reference perpendicular lines
        for i in np.arange(nep):
            plt.plot([s_0[i, 0], s_p[i, 0]], [s_0[i, 1], s_p[i, 1]],
                     fmt_secforce, solid_capstyle='round',
                     solid_joinstyle='round', dash_capstyle='butt',
                     dash_joinstyle='round')

    return minVal, maxVal


def section_force_diagram_3d(sf_type, Ew, sfac=1., nep=17,
                             fmt_secforce=fmt_secforce, dir_plt=0):
    """Display section forces diagram of a 3d beam column model.

    This function plots section forces diagrams for 3d beam column elements
    with or without element loads. For now only '-beamUniform' constant
    transverse or axial element loads are supported.

    Args:
        sf_type (str): type of section force: 'N' - normal force,
            'Vy' or 'Vz' - shear force, 'My' or 'Mz' - bending moments,
            'T' - torsional moment.

        Ew (dict): Ew Python dictionary contains information on non-zero
            element loads, therfore each item of the Python dictionary
            is in the form: 'ele_tag: ['-beamUniform', Wy, Wz, Wx]'.

        sfac (float): scale factor by wich the values of section forces are
            multiplied.

        nep (int): number of evaluation points including both end nodes
            (default: 17)

        fmt_secforce (str): format line string for section force distribution
            curve. The format contains information on line color, style and
            marks as in the standard matplotlib plot function.
            (default: fmt_secforce = 'b-'  # blue solid line)
        
        dir_plt {0, 1, 2}: direction in which to plot the load effects:
            0 (default) - as defined in the code for each load effect type
            1 - in the y-axis (default for N, Vy, T, Mz)
            2 - in the z-axis (default for Vz, My)

    Usage:
    ::

        Wy, Wz, Wx = -5., 0., 0.
        Ew = {3: ['-beamUniform', Wy, Wz, Wx]}
        sfacMz = 1.e-1
        plt.figure()
        minY, maxY = opsv.section_force_diagram_3d('Mz', Ew, sfacMz)
        plt.title(f'Bending moments Mz, max = {maxY:.2f}, min = {minY:.2f}')

    Todo:

    Add support for other element loads available in OpenSees: partial
    (trapezoidal) uniform element load, and 'beamPoint' element load.
    """

    maxVal, minVal = -np.inf, np.inf
    ele_tags = ops.getEleTags()

    azim, elev = az_el
    fig_wi, fig_he = fig_wi_he
    fleft, fbottom, fright, ftop = fig_lbrt

    fig = plt.figure(figsize=(fig_wi/2.54, fig_he/2.54))
    fig.subplots_adjust(left=.08, bottom=.08, right=.985, top=.94)

    ax = fig.add_subplot(111, projection=Axes3D.name)
    # ax.axis('equal')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.view_init(azim=azim, elev=elev)

    for i, ele_tag in enumerate(ele_tags):

        # by default no element load
        eload_data = ['-beamUniform', 0., 0., 0.]
        if ele_tag in Ew:
            eload_data = Ew[ele_tag]

        nd1, nd2 = ops.eleNodes(ele_tag)

        # element x, y coordinates
        ex = np.array([ops.nodeCoord(nd1)[0],
                       ops.nodeCoord(nd2)[0]])
        ey = np.array([ops.nodeCoord(nd1)[1],
                       ops.nodeCoord(nd2)[1]])
        ez = np.array([ops.nodeCoord(nd1)[2],
                       ops.nodeCoord(nd2)[2]])

        # eo = Eo[i, :]
        xloc = ops.eleResponse(ele_tag, 'xlocal')
        yloc = ops.eleResponse(ele_tag, 'ylocal')
        zloc = ops.eleResponse(ele_tag, 'zlocal')
        g = np.vstack((xloc, yloc, zloc))

        G, _ = rot_transf_3d(ex, ey, ez, g)

        g = G[:3, :3]

        pl = ops.eleResponse(ele_tag, 'localForces')

        s_all, xl = section_force_distribution_3d(ex, ey, ez, pl, nep,
                                                  eload_data)

        # 1:'y' 2:'z'
        if sf_type == 'N':
            s = s_all[:, 0]
            dir_plt_tmp = 1
        elif sf_type == 'Vy':
            s = s_all[:, 1]
            dir_plt_tmp = 1
        elif sf_type == 'Vz':
            s = s_all[:, 2]
            dir_plt_tmp = 2
        elif sf_type == 'T':
            s = s_all[:, 3]
            dir_plt_tmp = 1
        elif sf_type == 'My':
            s = s_all[:, 4]
            dir_plt_tmp = 2
        elif sf_type == 'Mz':
            s = s_all[:, 5]
            dir_plt_tmp = 1
        
        if dir_plt == 0:
            dir_plt = dir_plt_tmp

        minVal = min(minVal, np.min(s))
        maxVal = max(maxVal, np.max(s))

        s = s*sfac

        # FIXME - can be simplified
        s_0 = np.zeros((nep, 3))
        s_0[0, :] = [ex[0], ey[0], ez[0]]

        s_0[1:, 0] = s_0[0, 0] + xl[1:] * g[0, 0]
        s_0[1:, 1] = s_0[0, 1] + xl[1:] * g[0, 1]
        s_0[1:, 2] = s_0[0, 2] + xl[1:] * g[0, 2]

        s_p = np.copy(s_0)

        # positive M are opposite to N and V
        # if sf_type == 'Mz' or sf_type == 'My':
        if sf_type == 'Mz':
            s *= -1.

        s_p[:, 0] += s * g[dir_plt, 0]
        s_p[:, 1] += s * g[dir_plt, 1]
        s_p[:, 2] += s * g[dir_plt, 2]

        # plt.axis('equal')

        # section force curve
        plt.plot(s_p[:, 0], s_p[:, 1], s_p[:, 2], fmt_secforce,
                 solid_capstyle='round', solid_joinstyle='round',
                 dash_capstyle='butt', dash_joinstyle='round')

        # model
        plt.plot(ex, ey, ez, 'k-', solid_capstyle='round',
                 solid_joinstyle='round', dash_capstyle='butt',
                 dash_joinstyle='round')

        # reference perpendicular lines
        for i in np.arange(nep):
            plt.plot([s_0[i, 0], s_p[i, 0]],
                     [s_0[i, 1], s_p[i, 1]],
                     [s_0[i, 2], s_p[i, 2]], fmt_secforce,
                     solid_capstyle='round', solid_joinstyle='round',
                     dash_capstyle='butt', dash_joinstyle='round')

    return minVal, maxVal


def sig_out_per_node(how_many='all'):
    """Return a 2d numpy array of stress components per OpenSees node.

    Three first stress components (sxx, syy, sxy) are calculated and
    extracted from OpenSees, while the rest svm (Huber-Mieses-Hencky),
    two principal stresses (s1, s2) and directional angle are calculated
    as postprocessed quantities.

    Args:
        how_many (str): supported options are: 'all' - all components,
            'sxx', 'syy', 'sxy', 'svm' (or 'vmis'), 's1', 's2', 'angle'.

    Returns:
        sig_out (ndarray): a 2d array of stress components per node with
            the following components: sxx, syy, sxy, svm, s1, s2, angle.
            Size (n_nodes x 7).

    Examples:
        sig_out = opsv.sig_out_per_node()

    Notes:
       s1, s2: principal stresses
       angle: angle of the principal stress s1
    """
    ele_tags = ops.getEleTags()
    node_tags = ops.getNodeTags()
    n_nodes = len(node_tags)

    # initialize helper arrays
    sig_out = np.zeros((n_nodes, 7))

    nodes_tag_count = np.zeros((n_nodes, 2), dtype=int)
    nodes_tag_count[:, 0] = node_tags

    nen = np.shape(ops.eleNodes(ele_tags[0]))[0]

    if nen == 3:
        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3 = ops.eleNodes(ele_tag)

            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            nodes_tag_count[[ind1, ind2, ind3], 1] += 1

            sig_nd_el = ops.eleResponse(ele_tag, 'stressAtNodes')
            sigM_nd = np.vstack(([sig_nd_el[0:3],
                                  sig_nd_el[3:6],
                                  sig_nd_el[6:9]]))
            # sig_ip_el = ops.eleResponse(ele_tag, 'stress')
            # # assign the same value to all nodes
            # sigM_nd = np.vstack((sig_ip_el, sig_ip_el, sig_ip_el))
            # sxx
            sig_out[ind1, 0] += sigM_nd[0, 0]
            sig_out[ind2, 0] += sigM_nd[1, 0]
            sig_out[ind3, 0] += sigM_nd[2, 0]
            # syy
            sig_out[ind1, 1] += sigM_nd[0, 1]
            sig_out[ind2, 1] += sigM_nd[1, 1]
            sig_out[ind3, 1] += sigM_nd[2, 1]
            # sxy
            sig_out[ind1, 2] += sigM_nd[0, 2]
            sig_out[ind2, 2] += sigM_nd[1, 2]
            sig_out[ind3, 2] += sigM_nd[2, 2]

    elif nen == 4:
        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4 = ops.eleNodes(ele_tag)
            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            ind4 = node_tags.index(nd4)
            nodes_tag_count[[ind1, ind2, ind3, ind4], 1] += 1

            sig_ip_el = ops.eleResponse(ele_tag, 'stress')
            nip = len(sig_ip_el)
            # 4 gauss point quad
            if nip == 12:
                sig_nd_el = ops.eleResponse(ele_tag, 'stressAtNodes')
                sigM_nd = np.vstack(([sig_nd_el[0:3],
                                      sig_nd_el[3:6],
                                      sig_nd_el[6:9],
                                      sig_nd_el[9:12]]))
                # sigM_ip = np.vstack(([sig_ip_el[0:3],
                #                       sig_ip_el[3:6],
                #                       sig_ip_el[6:9],
                #                       sig_ip_el[9:12]]))
                # sigM_nd = extrapolate_ip_to_node_quad(sigM_ip)

            # SSPquad - stabilized single point quad
            elif nip == 3:
                # assign the same value to all nodes
                sigM_nd = np.vstack((sig_ip_el, sig_ip_el,
                                     sig_ip_el, sig_ip_el))

            # sxx
            sig_out[ind1, 0] += sigM_nd[0, 0]
            sig_out[ind2, 0] += sigM_nd[1, 0]
            sig_out[ind3, 0] += sigM_nd[2, 0]
            sig_out[ind4, 0] += sigM_nd[3, 0]
            # syy
            sig_out[ind1, 1] += sigM_nd[0, 1]
            sig_out[ind2, 1] += sigM_nd[1, 1]
            sig_out[ind3, 1] += sigM_nd[2, 1]
            sig_out[ind4, 1] += sigM_nd[3, 1]
            # sxy
            sig_out[ind1, 2] += sigM_nd[0, 2]
            sig_out[ind2, 2] += sigM_nd[1, 2]
            sig_out[ind3, 2] += sigM_nd[2, 2]
            sig_out[ind4, 2] += sigM_nd[3, 2]

    elif nen == 6:
        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6 = ops.eleNodes(ele_tag)
            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            ind4 = node_tags.index(nd4)
            ind5 = node_tags.index(nd5)
            ind6 = node_tags.index(nd6)
            nodes_tag_count[[ind1, ind2, ind3, ind4, ind5, ind6], 1] += 1

            # FIXME: wait until stressAtNodes is available in OpenSees upstream
            # locally it works
            sig_nd_el = ops.eleResponse(ele_tag, 'stressAtNodes')
            sigM_nd = np.vstack(([sig_nd_el[0:3],
                                  sig_nd_el[3:6],
                                  sig_nd_el[6:9],
                                  sig_nd_el[9:12],
                                  sig_nd_el[12:15],
                                  sig_nd_el[15:18]]))
            # sig_ip_el = ops.eleResponse(ele_tag, 'stress')
            # sigM_ip = np.vstack(([sig_ip_el[0:3],
            #                       sig_ip_el[3:6],
            #                       sig_ip_el[6:9]]))
            # sigM_nd = extrapolate_ip_to_node_tri6n(sigM_ip)
            # sxx
            sig_out[ind1, 0] += sigM_nd[0, 0]
            sig_out[ind2, 0] += sigM_nd[1, 0]
            sig_out[ind3, 0] += sigM_nd[2, 0]
            sig_out[ind4, 0] += sigM_nd[3, 0]
            sig_out[ind5, 0] += sigM_nd[4, 0]
            sig_out[ind6, 0] += sigM_nd[5, 0]
            # syy
            sig_out[ind1, 1] += sigM_nd[0, 1]
            sig_out[ind2, 1] += sigM_nd[1, 1]
            sig_out[ind3, 1] += sigM_nd[2, 1]
            sig_out[ind4, 1] += sigM_nd[3, 1]
            sig_out[ind5, 1] += sigM_nd[4, 1]
            sig_out[ind6, 1] += sigM_nd[5, 1]
            # sxy
            sig_out[ind1, 2] += sigM_nd[0, 2]
            sig_out[ind2, 2] += sigM_nd[1, 2]
            sig_out[ind3, 2] += sigM_nd[2, 2]
            sig_out[ind4, 2] += sigM_nd[3, 2]
            sig_out[ind5, 2] += sigM_nd[4, 2]
            sig_out[ind6, 2] += sigM_nd[5, 2]

    elif nen == 8:
        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6, nd7, nd8 = ops.eleNodes(ele_tag)
            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            ind4 = node_tags.index(nd4)
            ind5 = node_tags.index(nd5)
            ind6 = node_tags.index(nd6)
            ind7 = node_tags.index(nd7)
            ind8 = node_tags.index(nd8)
            nodes_tag_count[[ind1, ind2, ind3, ind4, ind5, ind6, ind7, ind8],
                            1] += 1

            # sig_ip_el = ops.eleResponse(ele_tag, 'stress')
            sig_nd_el = ops.eleResponse(ele_tag, 'stressAtNodes')
            sigM_nd = np.vstack(([sig_nd_el[0:3],
                                  sig_nd_el[3:6],
                                  sig_nd_el[6:9],
                                  sig_nd_el[9:12],
                                  sig_nd_el[12:15],
                                  sig_nd_el[15:18],
                                  sig_nd_el[18:21],
                                  sig_nd_el[21:24]]))
            # sig_nd_el[21:24],
            # sig_ip_el[24:27]]))
    indxs, = np.where(nodes_tag_count[:, 1] > 1)

    # n_indxs < n_nodes: e.g. 21<25 (bous), 2<6 (2el) etc.
    n_indxs = np.shape(indxs)[0]

    # divide summed stresses by the number of common nodes
    sig_out[indxs, :] = \
        sig_out[indxs, :]/nodes_tag_count[indxs, 1].reshape(n_indxs, 1)

    if how_many == 'all' or how_many == 'svm' or how_many == 'vmis':
        # warning reshape from (pts,ncomp) to (ncomp,pts)
        vm_out = vm_stress(np.transpose(sig_out[:, :3]))
        sig_out[:, 3] = vm_out

    if (how_many == 'all' or how_many == 's1' or how_many == 's2' or how_many == 'angle'):  # noqa: E501
        princ_sig_out = princ_stress(np.transpose(sig_out[:, :3]))

        sig_out[:, 4:7] = np.transpose(princ_sig_out)

    print('-- WARNING!!! full sig_out matrix calculated here --')

    return sig_out


def sig_component_per_node(stress_str):
    """Return a 2d numpy array of stress components per OpenSees node.

    Three first stress components (sxx, syy, sxy) are calculated and
    extracted from OpenSees, while the rest svm (Huber-Mieses-Hencky),
    two principal stresses (s1, s2) and directional angle are calculated
    as postprocessed quantities.

    Args:
        how_many (str): supported options are: 'all' - all components,
            'sxx', 'syy', 'sxy', 'svm' (or 'vmis'), 's1', 's2', 'angle'.

    Returns:
        sig_out (ndarray): a 2d array of stress components per node with
            the following components: sxx, syy, sxy, svm, s1, s2, angle.
            Size (n_nodes x 7).

    Examples:
        sig_out = opsv.sig_out_per_node()

    Notes:
       s1, s2: principal stresses
       angle: angle of the principal stress s1
    """
    ele_tags = ops.getEleTags()
    node_tags = ops.getNodeTags()
    n_nodes = len(node_tags)

    # initialize helper arrays
    sig_out = np.zeros((n_nodes, 4))

    nodes_tag_count = np.zeros((n_nodes, 2), dtype=int)
    nodes_tag_count[:, 0] = node_tags

    nen = np.shape(ops.eleNodes(ele_tags[0]))[0]

    if nen == 3:
        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3 = ops.eleNodes(ele_tag)

            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            nodes_tag_count[[ind1, ind2, ind3], 1] += 1

            sig_nd_el = ops.eleResponse(ele_tag, 'stressAtNodes')
            sigM_nd = np.vstack(([sig_nd_el[0:3],
                                  sig_nd_el[3:6],
                                  sig_nd_el[6:9]]))
            # sig_ip_el = ops.eleResponse(ele_tag, 'stress')
            # # assign the same value to all nodes
            # sigM_nd = np.vstack((sig_ip_el, sig_ip_el, sig_ip_el))
            # sxx
            sig_out[ind1, 0] += sigM_nd[0, 0]
            sig_out[ind2, 0] += sigM_nd[1, 0]
            sig_out[ind3, 0] += sigM_nd[2, 0]
            # syy
            sig_out[ind1, 1] += sigM_nd[0, 1]
            sig_out[ind2, 1] += sigM_nd[1, 1]
            sig_out[ind3, 1] += sigM_nd[2, 1]
            # sxy
            sig_out[ind1, 2] += sigM_nd[0, 2]
            sig_out[ind2, 2] += sigM_nd[1, 2]
            sig_out[ind3, 2] += sigM_nd[2, 2]

    elif nen == 4:
        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4 = ops.eleNodes(ele_tag)
            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            ind4 = node_tags.index(nd4)
            nodes_tag_count[[ind1, ind2, ind3, ind4], 1] += 1

            sig_ip_el = ops.eleResponse(ele_tag, 'stress')
            nip = len(sig_ip_el)
            # 4 gauss point quad
            if nip == 12:
                sig_nd_el = ops.eleResponse(ele_tag, 'stressAtNodes')
                sigM_nd = np.vstack(([sig_nd_el[0:3],
                                      sig_nd_el[3:6],
                                      sig_nd_el[6:9],
                                      sig_nd_el[9:12]]))
                # sigM_ip = np.vstack(([sig_ip_el[0:3],
                #                       sig_ip_el[3:6],
                #                       sig_ip_el[6:9],
                #                       sig_ip_el[9:12]]))
                # sigM_nd = extrapolate_ip_to_node_quad(sigM_ip)

            # SSPquad - stabilized single point quad
            elif nip == 3:
                # assign the same value to all nodes
                sigM_nd = np.vstack((sig_ip_el, sig_ip_el,
                                     sig_ip_el, sig_ip_el))

            # sxx
            sig_out[ind1, 0] += sigM_nd[0, 0]
            sig_out[ind2, 0] += sigM_nd[1, 0]
            sig_out[ind3, 0] += sigM_nd[2, 0]
            sig_out[ind4, 0] += sigM_nd[3, 0]
            # syy
            sig_out[ind1, 1] += sigM_nd[0, 1]
            sig_out[ind2, 1] += sigM_nd[1, 1]
            sig_out[ind3, 1] += sigM_nd[2, 1]
            sig_out[ind4, 1] += sigM_nd[3, 1]
            # sxy
            sig_out[ind1, 2] += sigM_nd[0, 2]
            sig_out[ind2, 2] += sigM_nd[1, 2]
            sig_out[ind3, 2] += sigM_nd[2, 2]
            sig_out[ind4, 2] += sigM_nd[3, 2]

    elif nen == 6:
        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6 = ops.eleNodes(ele_tag)
            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            ind4 = node_tags.index(nd4)
            ind5 = node_tags.index(nd5)
            ind6 = node_tags.index(nd6)
            nodes_tag_count[[ind1, ind2, ind3, ind4, ind5, ind6], 1] += 1

            # FIXME: wait until stressAtNodes is available in OpenSees upstream
            # locally it works
            sig_nd_el = ops.eleResponse(ele_tag, 'stressAtNodes')
            sigM_nd = np.vstack(([sig_nd_el[0:3],
                                  sig_nd_el[3:6],
                                  sig_nd_el[6:9],
                                  sig_nd_el[9:12],
                                  sig_nd_el[12:15],
                                  sig_nd_el[15:18]]))
            # sig_ip_el = ops.eleResponse(ele_tag, 'stress')
            # sigM_ip = np.vstack(([sig_ip_el[0:3],
            #                       sig_ip_el[3:6],
            #                       sig_ip_el[6:9]]))
            # sigM_nd = extrapolate_ip_to_node_tri6n(sigM_ip)
            # sxx
            sig_out[ind1, 0] += sigM_nd[0, 0]
            sig_out[ind2, 0] += sigM_nd[1, 0]
            sig_out[ind3, 0] += sigM_nd[2, 0]
            sig_out[ind4, 0] += sigM_nd[3, 0]
            sig_out[ind5, 0] += sigM_nd[4, 0]
            sig_out[ind6, 0] += sigM_nd[5, 0]
            # syy
            sig_out[ind1, 1] += sigM_nd[0, 1]
            sig_out[ind2, 1] += sigM_nd[1, 1]
            sig_out[ind3, 1] += sigM_nd[2, 1]
            sig_out[ind4, 1] += sigM_nd[3, 1]
            sig_out[ind5, 1] += sigM_nd[4, 1]
            sig_out[ind6, 1] += sigM_nd[5, 1]
            # sxy
            sig_out[ind1, 2] += sigM_nd[0, 2]
            sig_out[ind2, 2] += sigM_nd[1, 2]
            sig_out[ind3, 2] += sigM_nd[2, 2]
            sig_out[ind4, 2] += sigM_nd[3, 2]
            sig_out[ind5, 2] += sigM_nd[4, 2]
            sig_out[ind6, 2] += sigM_nd[5, 2]

    elif nen == 8:
        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6, nd7, nd8 = ops.eleNodes(ele_tag)
            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            ind4 = node_tags.index(nd4)
            ind5 = node_tags.index(nd5)
            ind6 = node_tags.index(nd6)
            ind7 = node_tags.index(nd7)
            ind8 = node_tags.index(nd8)
            nodes_tag_count[[ind1, ind2, ind3, ind4, ind5, ind6, ind7, ind8],
                            1] += 1

            # sig_ip_el = ops.eleResponse(ele_tag, 'stress')
            sig_nd_el = ops.eleResponse(ele_tag, 'stressAtNodes')
            sigM_nd = np.vstack(([sig_nd_el[0:3],
                                  sig_nd_el[3:6],
                                  sig_nd_el[6:9],
                                  sig_nd_el[9:12],
                                  sig_nd_el[12:15],
                                  sig_nd_el[15:18],
                                  sig_nd_el[18:21],
                                  sig_nd_el[21:24]]))
            # sig_nd_el[21:24],
            # sig_ip_el[24:27]]))
    indxs, = np.where(nodes_tag_count[:, 1] > 1)

    # n_indxs < n_nodes: e.g. 21<25 (bous), 2<6 (2el) etc.
    n_indxs = np.shape(indxs)[0]

    # divide summed stresses by the number of common nodes
    sig_out[indxs, :] = \
        sig_out[indxs, :]/nodes_tag_count[indxs, 1].reshape(n_indxs, 1)

    if stress_str == 'sxx':
        sig_out_vec = sig_out[:, 0]
    elif stress_str == 'syy':
        sig_out_vec = sig_out[:, 1]
    elif stress_str == 'sxy':
        sig_out_vec = sig_out[:, 2]
    elif stress_str == 'svm' or stress_str == 'vmis':
        # warning reshape from (pts,ncomp) to (ncomp,pts)
        sig_out_vec = vm_stress(np.transpose(sig_out[:, :3]))
    elif (stress_str == 's1' or stress_str == 's2' or stress_str == 'angle'):
        princ_sig_out = princ_stress(np.transpose(sig_out[:, :3]))
        if stress_str == 's1':
            # sig_out_vec = np.transpose(princ_sig_out)[:, 0]
            sig_out_vec = princ_sig_out[0, :]
        elif stress_str == 's2':
            sig_out_vec = princ_sig_out[1, :]
        elif stress_str == 'angle':
            sig_out_vec = princ_sig_out[2, :]

    return sig_out_vec


def extrapolate_ip_to_node_tri6n(yip):
    """Exprapolate from 3 integration points to 6 nodes of a tri6n element.

    The integration points are at (2/3, 1/6), (1/6, 2/3), (1/6, 1/6).
    Other possible 3 Gauss points are (1/2, 1/2), (1/2, 0), (0, 1/2).

    Integration points of Gauss quadrature.
    Usefull for : stress components (sxx, syy, sxy)

    yip - either a single vector (6,) or array (6,3) /sxx syy sxy/
          or array (6, n)
    """

    W = np.array([[1.6666666666666667, -0.3333333333333333, -0.3333333333333333],  # noqa: E501
                  [-0.3333333333333333,  1.6666666666666667, -0.3333333333333333],  # noqa: E501
                  [-0.3333333333333333, -0.3333333333333333,  1.6666666666666667],  # noqa: E501
                  [0.6666666666666667,  0.6666666666666667, -0.3333333333333333],  # noqa: E501
                  [-0.3333333333333333,  0.6666666666666667,  0.6666666666666667],  # noqa: E501
                  [0.6666666666666667, -0.3333333333333333,  0.6666666666666667]])  # noqa: E501
    ynp = W @ yip

    return ynp


def extrapolate_ip_to_node_quad(yip):
    """
    Exprapolate values at 4 integration points to 4 nodes of a quad element.

    Integration points of Gauss quadrature.
    Usefull for : stress components (sxx, syy, sxy)

    yip - either a single vector (4,) or array (4,3) /sxx syy sxy/
          or array (4, n)
    """

    xep = np.sqrt(3.)/2
    W = np.array([[1.+xep, -1/2., 1.-xep, -1/2.],
                  [-1/2., 1.+xep, -1/2., 1.-xep],
                  [1.-xep, -1/2., 1.+xep, -1/2.],
                  [-1/2., 1.-xep, -1/2., 1.+xep]])

    ynp = W @ yip
    return ynp


def extrapolate_ip_to_node_quad9n(yip):
    """
    Exprapolate values at 9 integration points to 9 nodes of a quad element.

    Integration points of Gauss quadrature.
    Usefull for : stress components (sxx, syy, sxy)

    yip - either a single vector (4,) or array (4,3) /sxx syy sxy/
          or array (4, n)
    """

    W = np.array([[2.1869398183909485, 0.2777777777777778, 0.0352824038312731, 0.2777777777777778, -0.9858870384674904, -0.1252240726436203, -0.1252240726436203, -0.9858870384674904, 0.4444444444444444],  # noqa: E501
                  [0.2777777777777778, 2.1869398183909485, 0.2777777777777778, 0.0352824038312731, -0.9858870384674904, -0.9858870384674904, -0.1252240726436203, -0.1252240726436203, 0.4444444444444444],  # noqa: E501
                  [0.0352824038312731, 0.2777777777777778, 2.1869398183909485, 0.2777777777777778, -0.1252240726436203, -0.9858870384674904, -0.9858870384674904, -0.1252240726436203, 0.4444444444444444],  # noqa: E501
                  [0.2777777777777778, 0.0352824038312731, 0.2777777777777778, 2.1869398183909485, -0.1252240726436203, -0.1252240726436203, -0.9858870384674904, -0.9858870384674904, 0.4444444444444444],  # noqa: E501
                  [0., 0., 0., 0., 1.4788305577012359, 0., 0.1878361089654305, 0., -0.6666666666666667],  # noqa: E501
                  [0., 0., 0., 0., 0., 1.4788305577012359, 0., 0.1878361089654305, -0.6666666666666667],  # noqa: E501
                  [0., 0., 0., 0., 0.1878361089654305, 0., 1.4788305577012359, 0., -0.6666666666666667],  # noqa: E501
                  [0., 0., 0., 0., 0., 0.1878361089654305, 0., 1.4788305577012359, -0.6666666666666667],  # noqa: E501
                  [0., 0., 0., 0., 0., 0., 0., 0., 1.]])

    ynp = W @ yip
    # ynp = 1.0

    return ynp


def extrapolate_ip_to_node_quad8n(yip):
    """
    Exprapolate values at 8 integration points to 8 nodes of a quad element.

    Integration points of Gauss quadrature.
    Usefull for : stress components (sxx, syy, sxy)

    yip - either a single vector (4,) or array (4,3) /sxx syy sxy/
          or array (4, n)
    """

    W = np.array([[2.0758287072798374, 0.1666666666666666, -0.075828707279838,  0.1666666666666666, -0.7636648162452683, 0.0969981495786018, 0.0969981495786018, -0.7636648162452683, 0.],  # noqa: E501
                  [0.1666666666666666, 2.0758287072798374, 0.1666666666666666, -0.075828707279838, -0.7636648162452683, -0.7636648162452683, 0.0969981495786018, 0.0969981495786018, 0.],  # noqa: E501
                  [-0.075828707279838,  0.1666666666666666, 2.0758287072798374, 0.1666666666666666, 0.0969981495786018, -0.7636648162452683, -0.7636648162452683, 0.0969981495786018, 0.],  # noqa: E501
                  [0.1666666666666666, -0.075828707279838,  0.1666666666666666, 2.0758287072798374, 0.0969981495786018, 0.0969981495786018, -0.7636648162452683, -0.7636648162452683, 0.],  # noqa: E501
                  [0.1666666666666666, 0.1666666666666666, 0.1666666666666666, 0.1666666666666666, 1.1454972243679027, -0.3333333333333333, -0.1454972243679028, -0.3333333333333333, 0.],  # noqa: E501
                  [0.1666666666666666, 0.1666666666666666, 0.1666666666666666, 0.1666666666666666, -0.3333333333333333, 1.1454972243679027, -0.3333333333333333, -0.1454972243679028, 0.],  # noqa: E501
                  [0.1666666666666666, 0.1666666666666666, 0.1666666666666666, 0.1666666666666666, -0.1454972243679028, -0.3333333333333333, 1.1454972243679027, -0.3333333333333333, 0.],  # noqa: E501
                  [0.1666666666666666, 0.1666666666666666, 0.1666666666666666, 0.1666666666666666, -0.3333333333333333, -0.1454972243679028, -0.3333333333333333, 1.1454972243679027, 0.]])  # noqa: E501

    ynp = W @ yip
    # ynp = 1.0

    return ynp


def quad_interpolate_node_to_ip(ynp):
    """
    Interpolate values at 4 nodes to 4 integration points a quad element.

    Integration points of Gauss quadrature.
    Usefull for : stress components (sxx, syy, sxy)

    ynp - either a single vector (4,) or array (4,3) /sxx syy sxy/
          or array (4, n)
    """
    jsz = 1./6.
    jtr = 1./3.
    p2 = jsz * np.sqrt(3.)
    W = np.array([[jtr+p2, jsz, jtr-p2, jsz],
                  [jsz, jtr+p2, jsz, jtr-p2],
                  [jtr-p2, jsz, jtr+p2, jsz],
                  [jsz, jtr-p2, jsz, jtr+p2]])

    yip = W @ ynp
    return yip


def princ_stress(sig):
    """Return a tuple (s1, s2, angle): principal stresses (plane stress) and angle
    Args:
        sig (ndarray): input array of stresses at nodes: sxx, syy, sxy (tau)

    Returns:
        out (ndarray): 1st row is first principal stress s1, 2nd row is second
           principal stress s2, 3rd row is the angle of s1
    """
    sx, sy, tau = sig[0], sig[1], sig[2]

    ds = (sx-sy)/2
    R = np.sqrt(ds**2 + tau**2)

    s1 = (sx+sy)/2. + R
    s2 = (sx+sy)/2. - R
    angle = np.arctan2(tau, ds)/2

    out = np.vstack((s1, s2, angle))

    return out


def vm_stress(sig):
    n_sig_comp, n_pts = np.shape(sig)
    if n_sig_comp > 3:
        x, y, z, xy, xz, yz = sig
    else:
        x, y, xy = sig
        z, xz, yz = 0., 0., 0.

    _a = 0.5*((x-y)**2 + (y-z)**2 + (z-x)**2 + 6.*(xy**2 + xz**2 + yz**2))
    return np.sqrt(_a)


def quad_crds_node_to_ip():
    """
    Return global coordinates of 4 quad ip nodes and corner nodes.

    It also returns quad connectivity.
    """
    node_tags, ele_tags = ops.getNodeTags(), ops.getEleTags()
    n_nodes, n_eles = len(node_tags), len(ele_tags)

    # idiom coordinates as ordered in node_tags
    nds_crd = np.zeros((n_nodes, 2))
    for i, node_tag in enumerate(node_tags):
        nds_crd[i] = ops.nodeCoord(node_tag)

    quads_conn = np.zeros((n_eles, 4), dtype=int)
    # quads_conn_ops = np.zeros((n_eles, 4), dtype=int)
    eles_nds_crd = np.zeros((n_eles, 4, 2))
    eles_ips_crd = np.zeros((n_eles, 4, 2))

    for i, ele_tag in enumerate(ele_tags):
        nd1, nd2, nd3, nd4 = ops.eleNodes(ele_tag)

        ind1 = node_tags.index(nd1)
        ind2 = node_tags.index(nd2)
        ind3 = node_tags.index(nd3)
        ind4 = node_tags.index(nd4)
        quads_conn[i] = np.array([ind1, ind2, ind3, ind4])
        # quads_conn_ops[i] = np.array([nd1, nd2, nd3, nd4])

        eles_nds_crd[i] = np.array([[ops.nodeCoord(nd1, 1),
                                     ops.nodeCoord(nd1, 2)],
                                    [ops.nodeCoord(nd2, 1),
                                     ops.nodeCoord(nd2, 2)],
                                    [ops.nodeCoord(nd3, 1),
                                     ops.nodeCoord(nd3, 2)],
                                    [ops.nodeCoord(nd4, 1),
                                     ops.nodeCoord(nd4, 2)]])
        eles_ips_crd[i] = quad_interpolate_node_to_ip(eles_nds_crd[i])

    return eles_ips_crd, eles_nds_crd, nds_crd, quads_conn


def sig_out_per_ele_quad():
    """
    Extract stress components for all elements from OpenSees analysis.

    Returns:
        eles_ips_sig_out, eles_nds_sig_out (tuple of ndarrays):
            eles_ips_sig_out - values at integration points of elements
            (n_eles x 4 x 4)
            eles_nds_sig_out - values at nodes of elements (n_eles x 4 x 4)
    Examples:
        eles_ips_sig_out, eles_nds_sig_out = opsv.sig_out_per_ele_quad()

    Notes:
        Stress components in array columns are: Sxx, Syy, Sxy, Svmis, empty
        Used e.g. by plot_mesh_with_ips_2d function
    """
    node_tags, ele_tags = ops.getNodeTags(), ops.getEleTags()
    n_nodes, n_eles = len(node_tags), len(ele_tags)

    eles_ips_sig_out = np.zeros((n_eles, 4, 4))
    eles_nds_sig_out = np.zeros((n_eles, 4, 4))

    # array (n_nodes, 2):
    # node_tags, number of occurrence in quad elements)
    # correspondence indx and node_tag is in node_tags.index
    # (a) data in np.array of integers
    nodes_tag_count = np.zeros((n_nodes, 2), dtype=int)
    nodes_tag_count[:, 0] = node_tags

    for i, ele_tag in enumerate(ele_tags):
        nd1, nd2, nd3, nd4 = ops.eleNodes(ele_tag)

        ind1 = node_tags.index(nd1)
        ind2 = node_tags.index(nd2)
        ind3 = node_tags.index(nd3)
        ind4 = node_tags.index(nd4)
        nodes_tag_count[[ind1, ind2, ind3, ind4], 1] += 1

        sig_ip_el = ops.eleResponse(ele_tag, 'stress')
        sigM_ip = np.vstack(([sig_ip_el[0:3],
                              sig_ip_el[3:6],
                              sig_ip_el[6:9],
                              sig_ip_el[9:12]]))
        sigM_nd = extrapolate_ip_to_node_quad(sigM_ip)
        eles_ips_sig_out[i, :, :3] = sigM_ip
        eles_nds_sig_out[i, :, :3] = sigM_nd

        vm_ip_out = vm_stress(np.transpose(eles_ips_sig_out[i, :, :3]))
        vm_nd_out = vm_stress(np.transpose(eles_nds_sig_out[i, :, :3]))
        eles_ips_sig_out[i, :, 3] = vm_ip_out
        eles_nds_sig_out[i, :, 3] = vm_nd_out

    return eles_ips_sig_out, eles_nds_sig_out


def quads_to_4tris(quads_conn, nds_crd, nds_val):
    """
    Get triangles connectivity, coordinates and new values at quad centroids.

    Args:
        quads_conn (ndarray):

        nds_crd (ndarray):

        nds_val (ndarray):

    Returns:
        tris_conn, nds_c_crd, nds_c_val (tuple):

    Notes:
        Triangles connectivity array is based on
        quadrilaterals connectivity.
        Each quad is split into four triangles.
        New nodes are created at the quad centroid.

    See also:
        function: quads_to_8tris_9n, quads_to_8tris_8n
    """
    n_quads, _ = quads_conn.shape
    n_nds, _ = nds_crd.shape

    # coordinates and values at quad centroids _c_
    nds_c_crd = np.zeros((n_quads, 2))
    nds_c_val = np.zeros(n_quads)

    tris_conn = np.zeros((4*n_quads, 3), dtype=int)

    for i, quad_conn in enumerate(quads_conn):
        j = 4*i
        n0, n1, n2, n3 = quad_conn

        # quad centroids
        nds_c_crd[i] = np.array([np.sum(nds_crd[[n0, n1, n2, n3], 0])/4.,
                                 np.sum(nds_crd[[n0, n1, n2, n3], 1])/4.])
        nds_c_val[i] = np.sum(nds_val[[n0, n1, n2, n3]])/4.

        # triangles connectivity
        tris_conn[j] = np.array([n0, n1, n_nds+i])
        tris_conn[j+1] = np.array([n1, n2, n_nds+i])
        tris_conn[j+2] = np.array([n2, n3, n_nds+i])
        tris_conn[j+3] = np.array([n3, n0, n_nds+i])

    return tris_conn, nds_c_crd, nds_c_val


def tris6n_to_4tris(tris_conn):
    """Get triangles connectivity.

    Six-node triangle is subdivided into four triangles

    Args:
        tris_conn (ndarray):

    Returns:
        tris_conn_subdiv (ndarray):
    """
    n_tris, _ = tris_conn.shape
    # n_nds, _ = nds_crd.shape

    tris_conn_subdiv = np.zeros((4*n_tris, 3), dtype=int)

    for i, tri_conn in enumerate(tris_conn):
        j = 4*i
        n0, n1, n2, n3, n4, n5 = tri_conn

        # triangles connectivity
        tris_conn_subdiv[j] = np.array([n0, n3, n5])
        tris_conn_subdiv[j+1] = np.array([n3, n1, n4])
        tris_conn_subdiv[j+2] = np.array([n3, n4, n5])
        tris_conn_subdiv[j+3] = np.array([n5, n4, n2])

    return tris_conn_subdiv


def plot_mesh_2d(nds_crd, eles_conn, lw=0.4, ec='k'):
    """
    Plot 2d mesh (quads or triangles) outline.
    """
    nen = np.shape(eles_conn)[1]
    if nen == 3 or nen == 4:
        for ele_conn in eles_conn:
            x = nds_crd[ele_conn, 0]
            y = nds_crd[ele_conn, 1]
            plt.fill(x, y, edgecolor=ec, lw=lw, fill=False)

    elif nen == 6:
        for ele_conn in eles_conn:
            x = nds_crd[[ele_conn[0], ele_conn[3], ele_conn[1], ele_conn[4],
                         ele_conn[2], ele_conn[5]], 0]
            y = nds_crd[[ele_conn[0], ele_conn[3], ele_conn[1], ele_conn[4],
                         ele_conn[2], ele_conn[5]], 1]
            plt.fill(x, y, edgecolor=ec, lw=lw, fill=False)

    elif nen == 9:
        for ele_conn in eles_conn:
            x = nds_crd[[ele_conn[0], ele_conn[4], ele_conn[1], ele_conn[5],
                         ele_conn[2], ele_conn[6], ele_conn[3], ele_conn[7]],
                        0]
            y = nds_crd[[ele_conn[0], ele_conn[4], ele_conn[1], ele_conn[5],
                         ele_conn[2], ele_conn[6], ele_conn[3], ele_conn[7]],
                        1]
            plt.fill(x, y, edgecolor=ec, lw=lw, fill=False)

    elif nen == 8:
        for ele_conn in eles_conn:
            x = nds_crd[[ele_conn[0], ele_conn[4], ele_conn[1], ele_conn[5],
                         ele_conn[2], ele_conn[6], ele_conn[3], ele_conn[7]],
                        0]
            y = nds_crd[[ele_conn[0], ele_conn[4], ele_conn[1], ele_conn[5],
                         ele_conn[2], ele_conn[6], ele_conn[3], ele_conn[7]],
                        1]
            plt.fill(x, y, edgecolor=ec, lw=lw, fill=False)


def plot_stress_2d(nds_val, mesh_outline=1, cmap='turbo', levels=50):
    """
    Plot stress distribution of a 2d elements of a 2d model.

    Args:
        nds_val (ndarray): the values of a stress component, which can
            be extracted from sig_out array (see sig_out_per_node
            function)

        mesh_outline (int): 1 - mesh is plotted, 0 - no mesh plotted.

        cmap (str): Matplotlib color map (default is 'turbo')

    Usage:
        ::

            sig_out = opsv.sig_out_per_node()
            j, jstr = 3, 'vmis'
            nds_val = sig_out[:, j]
            opsv.plot_stress_2d(nds_val)
            plt.xlabel('x [m]')
            plt.ylabel('y [m]')
            plt.title(f'{jstr}')
            plt.show()

    See also:

    :ref:`ops_vis_sig_out_per_node`
    """

    node_tags, ele_tags = ops.getNodeTags(), ops.getEleTags()
    n_nodes, n_eles = len(node_tags), len(ele_tags)

    nen = np.shape(ops.eleNodes(ele_tags[0]))[0]

    # idiom coordinates as ordered in node_tags
    # use node_tags.index(tag) for correspondence
    nds_crd = np.zeros((n_nodes, 2))
    for i, node_tag in enumerate(node_tags):
        nds_crd[i] = ops.nodeCoord(node_tag)

    # from utils / sig_out_per_node
    # fixme: if this can be simplified
    # index (starts from 0) to node_tag correspondence
    # (a) data in np.array of integers
    # nodes_tag_count = np.zeros((n_nodes, 2), dtype=int)
    # nodes_tag_count[:, 0] = node_tags
    #
    # correspondence indx and node_tag is in node_tags.index
    # after testing remove the above

    if nen == 3:
        tris_conn = np.zeros((n_eles, 3), dtype=int)

        nds_crd = np.zeros((n_nodes, 2))
        for i, node_tag in enumerate(node_tags):
            nds_crd[i] = ops.nodeCoord(node_tag)

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3 = ops.eleNodes(ele_tag)
            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            tris_conn[i] = np.array([ind1, ind2, ind3])

        # 1. plot contour maps
        triangulation = tri.Triangulation(nds_crd[:, 0],
                                          nds_crd[:, 1],
                                          tris_conn)

        plt.tricontourf(triangulation, nds_val, levels=levels, cmap=cmap)

        # 2. plot original mesh (quad) without subdivision into triangles
        if mesh_outline:
            plot_mesh_2d(nds_crd, tris_conn)

    elif nen == 4:
        quads_conn = np.zeros((n_eles, 4), dtype=int)

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4 = ops.eleNodes(ele_tag)
            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            ind4 = node_tags.index(nd4)
            quads_conn[i] = np.array([ind1, ind2, ind3, ind4])

        tris_conn, nds_c_crd, nds_c_val = \
            quads_to_4tris(quads_conn, nds_crd, nds_val)

        nds_crd_all = np.vstack((nds_crd, nds_c_crd))
        # nds_val_all = np.concatenate((nds_val, nds_c_val))
        nds_val_all = np.hstack((nds_val, nds_c_val))

        # 1. plot contour maps
        triangulation = tri.Triangulation(nds_crd_all[:, 0],
                                          nds_crd_all[:, 1],
                                          tris_conn)

        plt.tricontourf(triangulation, nds_val_all, levels=levels, cmap=cmap)

        # 2. plot original mesh (quad) without subdivision into triangles
        if mesh_outline:
            plot_mesh_2d(nds_crd, quads_conn)

    elif nen == 6:
        tris_conn = np.zeros((n_eles, 6), dtype=int)

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6 = ops.eleNodes(ele_tag)
            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            ind4 = node_tags.index(nd4)
            ind5 = node_tags.index(nd5)
            ind6 = node_tags.index(nd6)
            tris_conn[i] = np.array([ind1, ind2, ind3, ind4, ind5, ind6])

        tris_conn_subdiv = tris6n_to_4tris(tris_conn)

        # 1. plot contour maps
        triangulation = tri.Triangulation(nds_crd[:, 0],
                                          nds_crd[:, 1],
                                          tris_conn_subdiv)

        plt.tricontourf(triangulation, nds_val, levels=levels, cmap=cmap)

        # 2. plot original mesh (tri) without subdivision into triangles
        plot_mesh_2d(nds_crd, tris_conn)

    elif nen == 8:
        quads_conn = np.zeros((n_eles, 8), dtype=int)

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6, nd7, nd8 = ops.eleNodes(ele_tag)
            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            ind4 = node_tags.index(nd4)
            ind5 = node_tags.index(nd5)
            ind6 = node_tags.index(nd6)
            ind7 = node_tags.index(nd7)
            ind8 = node_tags.index(nd8)
            quads_conn[i] = np.array([ind1, ind2, ind3, ind4, ind5, ind6, ind7,
                                      ind8])

        # tris_conn = quads_to_8tris_8n(quads_conn)
        tris_conn, nds_c_crd, nds_c_val = quads_to_8tris_8n(quads_conn,
                                                            nds_crd, nds_val)

        nds_crd_all = np.vstack((nds_crd, nds_c_crd))
        # nds_val_all = np.concatenate((nds_val, nds_c_val))
        nds_val_all = np.hstack((nds_val, nds_c_val))

        # 1. plot contour maps
        triangulation = tri.Triangulation(nds_crd_all[:, 0],
                                          nds_crd_all[:, 1],
                                          tris_conn)

        plt.tricontourf(triangulation, nds_val_all, levels=levels, cmap=cmap)

        # 2. plot original mesh (quad) without subdivision into triangles
        plot_mesh_2d(nds_crd, quads_conn)

    elif nen == 9:
        quads_conn = np.zeros((n_eles, 9), dtype=int)

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3, nd4, nd5, nd6, nd7, nd8, nd9 = ops.eleNodes(ele_tag)
            ind1 = node_tags.index(nd1)
            ind2 = node_tags.index(nd2)
            ind3 = node_tags.index(nd3)
            ind4 = node_tags.index(nd4)
            ind5 = node_tags.index(nd5)
            ind6 = node_tags.index(nd6)
            ind7 = node_tags.index(nd7)
            ind8 = node_tags.index(nd8)
            ind9 = node_tags.index(nd9)
            quads_conn[i] = np.array([ind1, ind2, ind3, ind4, ind5, ind6, ind7,
                                      ind8, ind9])

        tris_conn = quads_to_8tris_9n(quads_conn)

        # 1. plot contour maps
        triangulation = tri.Triangulation(nds_crd[:, 0],
                                          nds_crd[:, 1],
                                          tris_conn)

        plt.tricontourf(triangulation, nds_val, levels=levels, cmap=cmap)

        # 2. plot original mesh (quad) without subdivision into triangles
        plot_mesh_2d(nds_crd, quads_conn)

    plt.colorbar()
    plt.axis('equal')


def plot_extruded_shapes_3d(ele_shapes, az_el=az_el,
                            fig_wi_he=fig_wi_he,
                            fig_lbrt=fig_lbrt):
    """Plot an extruded 3d model based on cross-section dimenions.

    Three arrows present local section axes: green - local x-axis,
    red - local z-axis, blue - local y-axis.

    Args:
        ele_shapes (dict): keys are ele_tags and values are lists of:
            shape_type (str): 'rect' - rectangular shape, 'I' - double T shape
            and shape_args (list): list of floats, which necessary section
            dimensions.
            For 'rect' the list is [b d]; width and depth,
            for 'I' shape - [bf d tw tf]; flange width, section depth, web
            and flange thicknesses
            Example: ele_shapes = {1: ['rect', [b, d]],
            2: ['I', [bf, d, tw, tf]]}

        az_el (tuple): azimuth and elevation

        fig_wi_he: figure width and height in centimeters

        fig_lbrt: figure left, bottom, right, top boundaries

    Usage:
        ::

            ele_shapes = {1: ['circ', [b]],
                          2: ['rect', [b, h]],
                          3: ['I', [b, h, b/10., h/6.]]}
            opsv.plot_extruded_shapes_3d(ele_shapes)

    Notes:

    - For now only rectangular, circular and double T sections are supported.

    - This function can be a source of inconsistency because OpenSees lacks
      functions to return section dimensions. A workaround is to have own
      Python helper functions to reuse data specified once
    """

    ele_tags = ops.getEleTags()

    azim, elev = az_el
    fig_wi, fig_he = fig_wi_he
    fleft, fbottom, fright, ftop = fig_lbrt

    fig = plt.figure(figsize=(fig_wi/2.54, fig_he/2.54))
    fig.subplots_adjust(left=.08, bottom=.08, right=.985, top=.94)

    ax = fig.add_subplot(111, projection=Axes3D.name)
    # ax.axis('equal')  # bug in matplotlib - does not work for 3d

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.view_init(azim=azim, elev=elev)

    for i, ele_tag in enumerate(ele_tags):

        nd1, nd2 = ops.eleNodes(ele_tag)

        # element x, y coordinates
        ex = np.array([ops.nodeCoord(nd1)[0],
                       ops.nodeCoord(nd2)[0]])
        ey = np.array([ops.nodeCoord(nd1)[1],
                       ops.nodeCoord(nd2)[1]])
        ez = np.array([ops.nodeCoord(nd1)[2],
                       ops.nodeCoord(nd2)[2]])

        # mesh outline
        ax.plot(ex, ey, ez, 'k--', solid_capstyle='round',
                solid_joinstyle='round', dash_capstyle='butt',
                dash_joinstyle='round')

        # eo = Eo[i, :]
        xloc = ops.eleResponse(ele_tag, 'xlocal')
        yloc = ops.eleResponse(ele_tag, 'ylocal')
        zloc = ops.eleResponse(ele_tag, 'zlocal')
        g = np.vstack((xloc, yloc, zloc))

        G, L = rot_transf_3d(ex, ey, ez, g)

        # by default empty
        shape_type, shape_args = ['circ', [0.]]
        if ele_tag in ele_shapes:
            shape_type, shape_args = ele_shapes[ele_tag]

        if shape_type == 'rect' or shape_type == 'I':
            if shape_type == 'rect':
                verts = _plot_extruded_shapes_3d_rect(ex, ey, ez, g,
                                                      shape_args)

            elif shape_type == 'I':
                verts = _plot_extruded_shapes_3d_double_T(ex, ey, ez, g,
                                                          shape_args)

            # plot 3d sides
            ax.add_collection3d(Poly3DCollection(verts, linewidths=0.6,
                                                 edgecolors='k', alpha=.25))

        elif shape_type == 'circ':
            X, Y, Z = _plot_extruded_shapes_3d_circ(ex, ey, ez, g,
                                                    shape_args)
            ax.plot_surface(X, Y, Z, linewidths=0.4, edgecolors='k',
                            alpha=.25)

        # common for all members
        Xm, Ym, Zm = sum(ex)/2, sum(ey)/2, sum(ez)/2

        alen = 0.1*L

        # plot local axis directional vectors: workaround quiver = arrow
        plt.quiver(Xm, Ym, Zm, g[0, 0], g[0, 1], g[0, 2], color='g',
                   lw=2, length=alen, alpha=.8, normalize=True)
        plt.quiver(Xm, Ym, Zm, g[1, 0], g[1, 1], g[1, 2], color='b',
                   lw=2, length=alen, alpha=.8, normalize=True)
        plt.quiver(Xm, Ym, Zm, g[2, 0], g[2, 1], g[2, 2], color='r',
                   lw=2, length=alen, alpha=.8, normalize=True)


def _plot_extruded_shapes_3d_double_T(ex, ey, ez, g, shape_args):
    bf, d, tw, tf = shape_args

    za, zb = tw/2, bf/2
    ya, yb = d/2 - tf, d/2

    g10a, g11a, g12a = g[1, 0]*ya, g[1, 1]*ya, g[1, 2]*ya
    g10b, g11b, g12b = g[1, 0]*yb, g[1, 1]*yb, g[1, 2]*yb

    g20a, g21a, g22a = g[2, 0]*za, g[2, 1]*za, g[2, 2]*za
    g20b, g21b, g22b = g[2, 0]*zb, g[2, 1]*zb, g[2, 2]*zb

    pts = np.zeros((24, 3))
    # beg node (I) cross-section vertices crds, counter-clockwise order
    pts[0] = [ex[0] - g10b - g20b, ey[0] - g11b - g21b, ez[0] - g12b - g22b]
    pts[1] = [ex[0] - g10a - g20b, ey[0] - g11a - g21b, ez[0] - g12a - g22b]
    pts[2] = [ex[0] - g10a - g20a, ey[0] - g11a - g21a, ez[0] - g12a - g22a]

    pts[3] = [ex[0] + g10a - g20a, ey[0] + g11a - g21a, ez[0] + g12a - g22a]
    pts[4] = [ex[0] + g10a - g20b, ey[0] + g11a - g21b, ez[0] + g12a - g22b]
    pts[5] = [ex[0] + g10b - g20b, ey[0] + g11b - g21b, ez[0] + g12b - g22b]

    pts[6] = [ex[0] + g10b + g20b, ey[0] + g11b + g21b, ez[0] + g12b + g22b]
    pts[7] = [ex[0] + g10a + g20b, ey[0] + g11a + g21b, ez[0] + g12a + g22b]
    pts[8] = [ex[0] + g10a + g20a, ey[0] + g11a + g21a, ez[0] + g12a + g22a]

    pts[9] = [ex[0] - g10a + g20a, ey[0] - g11a + g21a, ez[0] - g12a + g22a]
    pts[10] = [ex[0] - g10a + g20b, ey[0] - g11a + g21b, ez[0] - g12a + g22b]
    pts[11] = [ex[0] - g10b + g20b, ey[0] - g11b + g21b, ez[0] - g12b + g22b]

    # end node (J) cross-section vertices
    pts[12] = [ex[1] - g10b - g20b, ey[1] - g11b - g21b, ez[1] - g12b - g22b]
    pts[13] = [ex[1] - g10a - g20b, ey[1] - g11a - g21b, ez[1] - g12a - g22b]
    pts[14] = [ex[1] - g10a - g20a, ey[1] - g11a - g21a, ez[1] - g12a - g22a]

    pts[15] = [ex[1] + g10a - g20a, ey[1] + g11a - g21a, ez[1] + g12a - g22a]
    pts[16] = [ex[1] + g10a - g20b, ey[1] + g11a - g21b, ez[1] + g12a - g22b]
    pts[17] = [ex[1] + g10b - g20b, ey[1] + g11b - g21b, ez[1] + g12b - g22b]

    pts[18] = [ex[1] + g10b + g20b, ey[1] + g11b + g21b, ez[1] + g12b + g22b]
    pts[19] = [ex[1] + g10a + g20b, ey[1] + g11a + g21b, ez[1] + g12a + g22b]
    pts[20] = [ex[1] + g10a + g20a, ey[1] + g11a + g21a, ez[1] + g12a + g22a]

    pts[21] = [ex[1] - g10a + g20a, ey[1] - g11a + g21a, ez[1] - g12a + g22a]
    pts[22] = [ex[1] - g10a + g20b, ey[1] - g11a + g21b, ez[1] - g12a + g22b]
    pts[23] = [ex[1] - g10b + g20b, ey[1] - g11b + g21b, ez[1] - g12b + g22b]

    # list of sides
    verts = [[pts[0], pts[1], pts[2], pts[3], pts[4], pts[5], pts[6],
              pts[7], pts[8], pts[9], pts[10], pts[11]],  # beg
             [pts[12], pts[13], pts[14], pts[15], pts[16], pts[17],
              pts[18], pts[19], pts[20], pts[21], pts[22], pts[23]],  # end
             [pts[0], pts[12], pts[23], pts[11]],  # bot 1
             [pts[5], pts[17], pts[18], pts[6]],  # top 2
             [pts[9], pts[8], pts[20], pts[21]],  # 3
             [pts[2], pts[3], pts[15], pts[14]],  # 4
             [pts[11], pts[10], pts[22], pts[23]],  # 5
             [pts[0], pts[1], pts[13], pts[12]],  # 6
             [pts[7], pts[6], pts[18], pts[19]],  # 7
             [pts[4], pts[5], pts[17], pts[16]],  # 8
             [pts[10], pts[9], pts[21], pts[22]],  # 9
             [pts[2], pts[1], pts[13], pts[14]],  # 10
             [pts[7], pts[8], pts[20], pts[19]],  # 11
             [pts[3], pts[4], pts[16], pts[15]]]  # 12

    return verts


def _plot_extruded_shapes_3d_rect(ex, ey, ez, g, shape_args):
    b, d = shape_args
    b2, d2 = b/2, d/2

    g10, g11, g12 = g[1, 0]*d2, g[1, 1]*d2, g[1, 2]*d2
    g20, g21, g22 = g[2, 0]*b2, g[2, 1]*b2, g[2, 2]*b2

    pts = np.zeros((8, 3))
    # beg node cross-section vertices
    # collected i-beg, j-end node coordinates, counter-clockwise order
    pts[0] = [ex[0] - g10 - g20, ey[0] - g11 - g21, ez[0] - g12 - g22]
    pts[1] = [ex[0] + g10 - g20, ey[0] + g11 - g21, ez[0] + g12 - g22]
    pts[2] = [ex[0] + g10 + g20, ey[0] + g11 + g21, ez[0] + g12 + g22]
    pts[3] = [ex[0] - g10 + g20, ey[0] - g11 + g21, ez[0] - g12 + g22]
    # end node cross-section vertices
    pts[4] = [ex[1] - g10 - g20, ey[1] - g11 - g21, ez[1] - g12 - g22]
    pts[5] = [ex[1] + g10 - g20, ey[1] + g11 - g21, ez[1] + g12 - g22]
    pts[6] = [ex[1] + g10 + g20, ey[1] + g11 + g21, ez[1] + g12 + g22]
    pts[7] = [ex[1] - g10 + g20, ey[1] - g11 + g21, ez[1] - g12 + g22]

    # list of 4-node sides
    verts = [[pts[0], pts[1], pts[2], pts[3]],  # beg
             [pts[4], pts[5], pts[6], pts[7]],  # end
             [pts[0], pts[4], pts[5], pts[1]],  # bottom
             [pts[3], pts[7], pts[6], pts[2]],  # top
             [pts[0], pts[4], pts[7], pts[3]],  # front
             [pts[1], pts[5], pts[6], pts[2]]]  # back

    return verts


def _plot_extruded_shapes_3d_circ(ex, ey, ez, g, shape_args):
    d = shape_args[0]
    r = d/2

    Lxyz = np.array([ex[1]-ex[0], ey[1]-ey[0], ez[1]-ez[0]])
    L = np.sqrt(Lxyz @ Lxyz)

    xl = np.linspace(0, L, 3)  # subdivde member length
    alpha = np.linspace(0, 2 * np.pi, 10)  # subdivide circle

    xl, alpha = np.meshgrid(xl, alpha)
    X = (ex[0] + g[0, 0] * xl + r * np.sin(alpha) * g[1, 0]
         + r * np.cos(alpha) * g[2, 0])
    Y = (ey[0] + g[0, 1] * xl + r * np.sin(alpha) * g[1, 1]
         + r * np.cos(alpha) * g[2, 1])
    Z = (ez[0] + g[0, 2] * xl + r * np.sin(alpha) * g[1, 2]
         + r * np.cos(alpha) * g[2, 2])

    return X, Y, Z


def plot_mesh_with_ips_2d(nds_crd, eles_ips_crd, eles_nds_crd, quads_conn,
                          eles_ips_sig_out, eles_nds_sig_out, sig_out_indx):
    """
    Plot 2d element mesh with the values at integration points and nodes.

    Args:
        nds_crd (ndarray): nodes coordinates (n_nodes x 2)

        eles_ips_crd (ndarray): integration points coordinates of elements
            (n_eles x 4 x 2)

        eles_nds_crd (ndarray): nodal coordinates of elements (n_eles x 4 x 2)

        quads_conn (ndarray): connectivity array (n_eles x 4)

        eles_ips_sig_out (ndarray): stress component values at integration
            points (n_eles x 4 x 4)

        eles_nds_sig_out (ndarray): stress component values at element nodes
            (n_eles x 4 x 4)

        sig_out_indx (int): which sig_out component

    Notes: This function is suitable for small models for illustration
        purposes.
    """

    plot_mesh_2d(nds_crd, quads_conn, lw=1.2, ec='b')

    ele_tags = ops.getEleTags()
    n_eles = len(ele_tags)

    for i in range(n_eles):
        plt.plot(eles_ips_crd[i, :, 0], eles_ips_crd[i, :, 1],
                 'kx', markersize=3)

        ips_val = eles_ips_sig_out[i, :, sig_out_indx]
        nds_val = eles_nds_sig_out[i, :, sig_out_indx]

        # show ips values
        plt.text(eles_ips_crd[i, 0, 0], eles_ips_crd[i, 0, 1],
                 f'{ips_val[0]:.2f}', {'color': 'C0'},
                 ha='center', va='bottom')
        plt.text(eles_ips_crd[i, 1, 0], eles_ips_crd[i, 1, 1],
                 f'{ips_val[1]:.2f}', {'color': 'C1'},
                 ha='center', va='bottom')
        plt.text(eles_ips_crd[i, 2, 0], eles_ips_crd[i, 2, 1],
                 f'{ips_val[2]:.2f}', {'color': 'C2'},
                 ha='center', va='top')
        plt.text(eles_ips_crd[i, 3, 0], eles_ips_crd[i, 3, 1],
                 f'{ips_val[3]:.2f}', {'color': 'C3'},
                 ha='center', va='top')

        # show node values
        plt.text(eles_nds_crd[i, 0, 0], eles_nds_crd[i, 0, 1],
                 f' {nds_val[0]:.2f}', {'color': 'C0'},
                 ha='left', va='bottom')
        plt.text(eles_nds_crd[i, 1, 0], eles_nds_crd[i, 1, 1],
                 f'{nds_val[1]:.2f} ', {'color': 'C1'},
                 ha='right', va='bottom')
        plt.text(eles_nds_crd[i, 2, 0], eles_nds_crd[i, 2, 1],
                 f'{nds_val[2]:.2f} ', {'color': 'C2'},
                 ha='right', va='top')
        plt.text(eles_nds_crd[i, 3, 0], eles_nds_crd[i, 3, 1],
                 f' {nds_val[3]:.2f}', {'color': 'C3'},
                 ha='left', va='top')

    plt.axis('equal')


# see also quads_to_8tris_9n
def quads_to_8tris_8n(quads_conn, nds_crd, nds_val):
    """
    Get triangles connectivity, coordinates and new values at quad centroids.

    Args:
        quads_conn (ndarray):

        nds_crd (ndarray):

        nds_val (ndarray):

    Returns:
        tris_conn, nds_c_crd, nds_c_val (tuple):

    Notes:
        Triangles connectivity array is based on
        quadrilaterals connectivity.
        Each quad is split into eight triangles.
        New nodes are created at the quad centroid.

    See also:
        function: quads_to_8tris_9n, quads_to_4tris
    """
    n_quads, _ = quads_conn.shape
    n_nds, _ = nds_crd.shape

    # coordinates and values at quad centroids _c_
    nds_c_crd = np.zeros((n_quads, 2))
    nds_c_val = np.zeros(n_quads)

    tris_conn = np.zeros((8*n_quads, 3), dtype=int)

    for i, quad_conn in enumerate(quads_conn):
        j = 8*i
        n0, n1, n2, n3, n4, n5, n6, n7 = quad_conn

        # quad centroids
        # nds_c_crd[i] = np.array([np.sum(nds_crd[[n0, n1, n2, n3], 0])/4.,
        #                          np.sum(nds_crd[[n0, n1, n2, n3], 1])/4.])
        # nds_c_val[i] = np.sum(nds_val[[n0, n1, n2, n3]])/4.
        nds_c_crd[i] = quad8n_val_at_center(nds_crd[[n0, n1, n2, n3,
                                                     n4, n5, n6, n7]])
        nds_c_val[i] = quad8n_val_at_center(nds_val[[n0, n1, n2, n3,
                                                     n4, n5, n6, n7]])

        # triangles connectivity
        tris_conn[j] = np.array([n0, n4, n_nds+i])
        tris_conn[j+1] = np.array([n4, n1, n_nds+i])
        tris_conn[j+2] = np.array([n1, n5, n_nds+i])
        tris_conn[j+3] = np.array([n5, n2, n_nds+i])
        tris_conn[j+4] = np.array([n2, n6, n_nds+i])
        tris_conn[j+5] = np.array([n6, n3, n_nds+i])
        tris_conn[j+6] = np.array([n3, n7, n_nds+i])
        tris_conn[j+7] = np.array([n7, n0, n_nds+i])

    return tris_conn, nds_c_crd, nds_c_val


# see also quads_to_8tris_8n
def quads_to_8tris_9n(quads_conn):
    """
    Get triangles connectivity, coordinates and new values at quad centroids.

    Args:
        quads_conn (ndarray):

        nds_crd (ndarray):

        nds_val (ndarray):

    Returns:
        tris_conn, nds_c_crd, nds_c_val (tuple):

    Notes:
        Triangles connectivity array is based on
        quadrilaterals connectivity.
        Each quad is split into eight triangles.
        New nodes are created at the quad centroid.

    See also:
        function: quads_to_8tris_8n, quads_to_4tris
    """
    n_quads, _ = quads_conn.shape
    # n_nds, _ = nds_crd.shape

    tris_conn = np.zeros((8*n_quads, 3), dtype=int)

    for i, quad_conn in enumerate(quads_conn):
        j = 8*i
        n0, n1, n2, n3, n4, n5, n6, n7, n8 = quad_conn

        # center nodeds already present in quad 9n

        # triangles connectivity
        tris_conn[j] = np.array([n0, n4, n8])
        tris_conn[j+1] = np.array([n4, n1, n8])
        tris_conn[j+2] = np.array([n1, n5, n8])
        tris_conn[j+3] = np.array([n5, n2, n8])
        tris_conn[j+4] = np.array([n2, n6, n8])
        tris_conn[j+5] = np.array([n6, n3, n8])
        tris_conn[j+6] = np.array([n3, n7, n8])
        tris_conn[j+7] = np.array([n7, n0, n8])

    # return tris_conn, nds_c_crd, nds_c_val
    return tris_conn


def quad8n_val_at_center(vals):
    """
    Calculate values at the center of 8-node quad element.

    """

    val_c1 = -np.mean(vals[[0, 1, 2, 3]], axis=0) + 2*np.mean(vals[[4, 5, 6, 7]], axis=0)  # noqa: E501

    return val_c1


def plot_stress(stress_str, mesh_outline=1, cmap='turbo', levels=50):
    """Plot stress distribution of the model.

    Args:
        stress_str (string): stress component string. Available options are:
            'sxx', 'syy', 'sxy', 'vmis', 's1', 's2', 'alpha'

        mesh_outline (int): 1 - mesh is plotted, 0 - no mesh plotted.

        cmap (str): Matplotlib color map (default is 'turbo')

        levels (int): number and positions of the contour lines / regions.

    Usage:
        ::

            opsv.plot_stress('vmis')
            plt.xlabel('x [m]')
            plt.ylabel('y [m]')
            plt.show()

    See also:

    :ref:`ops_vis_sig_out_per_node`
    """

    # az_el - azimut, elevation used for 3d plots only
    ndim = np.shape(ops.nodeCoord(ops.getNodeTags()[0]))[0]

    if ndim == 2:
        _plot_stress_2d(stress_str, mesh_outline, cmap, levels)
        # if axis_off:
        #     plt.axis('off')

    # not implemented yet
    # elif ndim == 3:
    #     _plot_stress_3d(stress_str, mesh_outline, cmap, levels)

    else:
        print(f'\nWarning! ndim: {ndim} not implemented yet.')

    # plt.show()  # call this from main py file for more control


def _plot_stress_2d(stress_str, mesh_outline, cmap, levels):
    """See documentation for plot_stress command"""

    # node_tags = ops.getNodeTags()
    # ele_tags = ops.getEleTags()
    # n_nodes = len(node_tags)

    # second version - better - possible different types
    # of elements (mix of quad and tri)
    # for ele_tag in ele_tags:
    #     nen = np.shape(ops.eleNodes(ele_tag))[0]

    # avoid calculating and storing all stress components
    # sig_out = sig_out_per_node(stress_str)
    # switcher = {'sxx': 0,
    #             'syy': 1,
    #             'sxy': 2,
    #             'svm': 3,
    #             'vmis': 3,
    #             's1': 4,
    #             's2': 5,
    #             'angle': 6}

    # nds_val = sig_out[:, switcher[stress_str]]

    nds_val = sig_component_per_node(stress_str)
    plot_stress_2d(nds_val, mesh_outline, cmap, levels)
