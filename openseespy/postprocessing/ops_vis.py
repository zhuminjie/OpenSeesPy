# Developed by Seweryn Kokot
# Opole University of Technology, Opole, Poland
# ver. 0.81, 2020 April

# Some functions, implemented in this library, are inspired by:
# https://github.com/CALFEM/calfem-matlab
# https://github.com/CALFEM/calfem-python
# plot_section is inspired by similar Matlab function
# found on OpenSees forum and written by D. Vamvatsikos

# import openseespy.opensees as ops
import opensees as ops
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle, Polygon

# default settings

# fmt string sets color, marker and linestyle
# fmt for continuous interpolated shape line
fmtc = 'b-'

# fmt for element end nodes
fmte = 'rs'

# fmt for undeformed model
fmtu = 'g--'

# fmt for section forces
fmtsf = 'b-'

# figure left right bottom top offsets
fig_lbrt = (.04, .04, .96, .96)

# azimut and elevation in degrees
az_el = (-60., 30.)

# figure width and height in centimeters
fig_wi_he = (16., 10.)


def _plot_model_2d(node_labels, element_labels, offn, axis_off):

    max_x_crd, max_y_crd, max_crd = -np.inf, -np.inf, -np.inf

    node_tags = ops.getNodeTags()
    ele_tags = ops.getEleTags()

    nen = np.shape(ops.eleNodes(ele_tags[0]))[0]

    # truss and beam/frame elements
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
                if not offn == 'above':
                    offn_x, offn_y = _offset, _offset
                    va = 'bottom'
                    ha = 'left'
                else:
                    offn_x, offn_y = 0.0, _offset
                    va = 'bottom'
                    ha = 'center'

                plt.text(ops.nodeCoord(node_tag)[0]+offn_x,
                         ops.nodeCoord(node_tag)[1]+offn_y,
                         f'{node_tag}', va=va, ha=ha, color='blue')

        # plt.axis('equal')

    # 2d triangular (tri31) elements
    elif nen == 3:

        for node_tag in node_tags:
            x_crd = ops.nodeCoord(node_tag)[0]
            y_crd = ops.nodeCoord(node_tag)[1]
            if x_crd > max_x_crd:
                max_x_crd = x_crd
            if y_crd > max_y_crd:
                max_y_crd = y_crd

        max_crd = np.amax([max_x_crd, max_y_crd])
        # print(f'max_x_crd: {max_x_crd}')
        # print(f'max_y_crd: {max_y_crd}')
        # print(f'max_crd: {max_crd}')
        _offset = 0.005 * max_crd
        _offn = 0.003 * max_crd

        for i, ele_tag in enumerate(ele_tags):
            nd1, nd2, nd3 = ops.eleNodes(ele_tag)

            # element x, y coordinates
            ex = np.array([ops.nodeCoord(nd1)[0],
                           ops.nodeCoord(nd2)[0],
                           ops.nodeCoord(nd3)[0]])
            ey = np.array([ops.nodeCoord(nd1)[1],
                           ops.nodeCoord(nd2)[1],
                           ops.nodeCoord(nd3)[1]])

            # print(f'{i+1:3}. el. {ele_tag}: {nd1}-{nd2}-{nd3}-{nd4}')

            # location of label
            xt = sum(ex)/nen
            yt = sum(ey)/nen
            # print(f'xt:\n{xt}')
            # print(f'yt:\n{yt}')

            plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]), 'bo-')

            if element_labels:
                va = 'center'
                ha = 'center'
                plt.text(xt, yt, f'{ele_tag}', va=va, ha=ha, color='red')

        if node_labels:
            for node_tag in node_tags:
                if not offn == 'above':
                    offn_x, offn_y = _offn, _offn
                    va = 'bottom'
                    # va = 'center'
                    ha = 'left'
                else:
                    offn_x, offn_y = 0.0, _offn
                    va = 'bottom'
                    ha = 'center'

                plt.text(ops.nodeCoord(node_tag)[0]+offn_x,
                         ops.nodeCoord(node_tag)[1]+offn_y,
                         f'{node_tag}', va=va, ha=ha, color='blue')

    # 2d quadrilateral (quad) elements
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
        _offn = 0.003 * max_crd

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

            plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]), 'bo-')

            if element_labels:
                va = 'center'
                ha = 'center'
                plt.text(xt, yt, f'{ele_tag}', va=va, ha=ha, color='red')

        if node_labels:
            for node_tag in node_tags:
                if not offn == 'above':
                    offn_x, offn_y = _offn, _offn
                    va = 'bottom'
                    # va = 'center'
                    ha = 'left'
                else:
                    offn_x, offn_y = 0.0, _offn
                    va = 'bottom'
                    ha = 'center'

                plt.text(ops.nodeCoord(node_tag)[0]+offn_x,
                         ops.nodeCoord(node_tag)[1]+offn_y,
                         f'{node_tag}', va=va, ha=ha, color='blue')


def _plot_model_3d(node_labels, element_labels, offn, axis_off, az_el,
                   fig_wi_he, fig_lbrt):

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
    # print(f'\n-- nen: {nen} - (number of element nodes)')

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

        if offn == 0 or offn == 0.:
            _offset = 0.
        else:
            max_crd = np.amax([max_x_crd, max_y_crd, max_z_crd])
            print(f'max_x_crd: {max_x_crd}')
            print(f'max_y_crd: {max_y_crd}')
            print(f'max_z_crd: {max_z_crd}')
            print(f'max_crd: {max_crd}')
            _offset = 0.005 * max_crd

        # work-around fix because of aspect equal bug
        # _max_overall = 1.1*max_crd
        # _min_overall = -0.1*max_crd
        # ax.set_xlim(_min_overall, _max_overall)
        # ax.set_ylim(_min_overall, _max_overall)
        # ax.set_zlim(_min_overall, _max_overall)

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

            ax.plot(ex, ey, ez, 'bo-')

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

            # ax.plot(np.array([x_crd]),
            #         np.array([y_crd]),
            #         np.array([z_crd]), 'ro')

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
                    np.append(ez, ez[0]), 'bo-')

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

            # ax.plot(np.array([x_crd]),
            #         np.array([y_crd]),
            #         np.array([z_crd]), 'ro')

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
                    np.append(ez[0:4], ez[0]), 'bo-')
            ax.plot(np.append(ex[4:8], ex[4]),
                    np.append(ey[4:8], ey[4]),
                    np.append(ez[4:8], ez[4]), 'bo-')
            ax.plot(np.array([ex[0], ex[4]]),
                    np.array([ey[0], ey[4]]),
                    np.array([ez[0], ez[4]]), 'bo-')
            ax.plot(np.array([ex[1], ex[5]]),
                    np.array([ey[1], ey[5]]),
                    np.array([ez[1], ez[5]]), 'bo-')
            ax.plot(np.array([ex[2], ex[6]]),
                    np.array([ey[2], ey[6]]),
                    np.array([ez[2], ez[6]]), 'bo-')
            ax.plot(np.array([ex[3], ex[7]]),
                    np.array([ey[3], ey[7]]),
                    np.array([ez[3], ez[7]]), 'bo-')

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


def plot_model(node_labels=1, element_labels=1, offn=False, axis_off=0,
               az_el=az_el, fig_wi_he=fig_wi_he, fig_lbrt=fig_lbrt):

    # az_el - azimut, elevation used for 3d plots only

    node_tags = ops.getNodeTags()

    ndim = np.shape(ops.nodeCoord(node_tags[0]))[0]

    if ndim == 2:
        _plot_model_2d(node_labels, element_labels, offn, axis_off)
        if axis_off:
            plt.axis('off')

    elif ndim == 3:
        _plot_model_3d(node_labels, element_labels, offn, axis_off, az_el,
                       fig_wi_he, fig_lbrt)
        if axis_off:
            plt.axis('off')

    else:
        print(f'ndim = {ndim} not supported yet. Supported are 2d \
        and 3d models')

    # plt.show()  # call this from main py file for more control


def _plot_defo_mode_2d(modeNo, sfac, npt, unDefoFlag, fmtu, interpFlag,
                       endDispFlag, fmtc, fmte):

    ele_tags = ops.getEleTags()

    nen = np.shape(ops.eleNodes(ele_tags[0]))[0]

    # truss and beam/frame elements
    if nen == 2:

        # is there a better way to get ndf - number of dofs per node?
        # 2 - truss, 3 - frame
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

                # displacements: translations and/or rotations per element
                # rotations are neglected
                # eux = [ux1, ux2], edy = [uy1, uy2]
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
                    plt.plot(ex, ey, fmtu)

                plt.plot(edx, edy, fmtc)

        # beam/frame element
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
                    plt.plot(ex, ey, fmtu)

                # interpolated displacement field
                if interpFlag:
                    xcdi, ycdi = beam_defo_interp_2d(ex, ey, ed, sfac, npt)
                    plt.plot(xcdi, ycdi, fmtc)

                # translations of ends
                if endDispFlag:
                    xdi, ydi = beam_disp_ends(ex, ey, ed, sfac)
                    plt.plot(xdi, ydi, fmte)

        plt.axis('equal')
        # plt.show()  # call this from main py file for more control

    # 2d triangular (tri31) elements
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

            print(f'ed: {ed}')

            if unDefoFlag:
                plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]), fmtu)

            # xcdi, ycdi = beam_defo_interp_2d(ex, ey, ed, sfac, npt)
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
            print(f'ex:\n{ex}')
            print(f'x:\n{x}')
            print(f'ey:\n{ey}')
            print(f'y:\n{y}')
            plt.plot(np.append(x, x[0]), np.append(y, y[0]), 'b.-')

        plt.axis('equal')

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
                plt.plot(np.append(ex, ex[0]), np.append(ey, ey[0]), fmtu)

            # xcdi, ycdi = beam_defo_interp_2d(ex, ey, ed, sfac, npt)
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
        print(f'nen = {nen} not = 2, 3, 4, 8 ')
        print('elements not supported yet')


def _plot_defo_mode_3d(modeNo, sfac, npt, unDefoFlag, fmtu, interpFlag,
                       endDispFlag, fmtc, fmte, Eo, az_el, fig_wi_he,
                       fig_lbrt):

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

        # is there a better way to get ndf - number of dofs per node?
        # 2 - truss, 3 - frame
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

                eo = Eo[i, :]

                if unDefoFlag:
                    plt.plot(ex, ey, ez, fmtu)

                # interpolated displacement field
                if interpFlag:
                    xcd, ycd, zcd = beam_defo_interp_3d(ex, ey, ez, eo,
                                                        ed, sfac, npt)
                    ax.plot(xcd, ycd, zcd, fmtc)
                    ax.set_xlabel('X')
                    ax.set_ylabel('Y')
                    ax.set_zlabel('Z')

                # translations of ends
                if endDispFlag:
                    xd, yd, zd = beam_disp_ends3d(ex, ey, ez, ed, sfac)
                    ax.plot(xd, yd, zd, fmte)

        # # work-around fix because of aspect equal bug
        # xmin, xmax = ax.get_xlim()
        # ymin, ymax = ax.get_ylim()
        # zmin, zmax = ax.get_zlim()

        # min_overall = np.amax([np.abs(xmin), np.abs(ymin), np.abs(zmin)])
        # max_overall = np.amax([np.abs(xmax), np.abs(ymax), np.abs(zmax)])

        # minmax_overall = max(min_overall, max_overall)
        # print(f'min_overall:\n{min_overall}')
        # print(f'max_overall:\n{max_overall}')
        # print(f'minmax_overall:\n{minmax_overall}')
        # _max_overall = 1.1 * minmax_overall
        # _min_overall = -1.1 * minmax_overall
        # ax.set_xlim(_min_overall, _max_overall)
        # ax.set_ylim(_min_overall, _max_overall)
        # # ax.set_zlim(_min_overall, _max_overall)
        # ax.set_zlim(0.0, _max_overall)

    # plot: quad in 3d
    elif nen == 4:

        # is there a better way to get ndf - number of dofs per node?
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
                            fmtu)

                x = ex+sfac*ed[[0, 3, 6, 9]]
                y = ey+sfac*ed[[1, 4, 7, 10]]
                z = ez+sfac*ed[[2, 5, 8, 11]]
                ax.plot(np.append(x, x[0]),
                        np.append(y, y[0]),
                        np.append(z, z[0]),
                        'b.-')
                # ax.axis('equal')

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
                        np.append(ez[0:4], ez[0]), fmtu)
                ax.plot(np.append(ex[4:8], ex[4]),
                        np.append(ey[4:8], ey[4]),
                        np.append(ez[4:8], ez[4]), fmtu)
                ax.plot(np.array([ex[0], ex[4]]),
                        np.array([ey[0], ey[4]]),
                        np.array([ez[0], ez[4]]), fmtu)
                ax.plot(np.array([ex[1], ex[5]]),
                        np.array([ey[1], ey[5]]),
                        np.array([ez[1], ez[5]]), fmtu)
                ax.plot(np.array([ex[2], ex[6]]),
                        np.array([ey[2], ey[6]]),
                        np.array([ez[2], ez[6]]), fmtu)
                ax.plot(np.array([ex[3], ex[7]]),
                        np.array([ey[3], ey[7]]),
                        np.array([ez[3], ez[7]]), fmtu)

            x = ex+sfac*ed[[0, 3, 6, 9, 12, 15, 18, 21]]
            y = ey+sfac*ed[[1, 4, 7, 10, 13, 16, 19, 22]]
            z = ez+sfac*ed[[2, 5, 8, 11, 14, 17, 20, 23]]
            # print(f'x:\n{x}')
            # print(f'y:\n{y}')
            # print(f'z:\n{z}')
            ax.plot(np.append(x[:4], x[0]),
                    np.append(y[:4], y[0]),
                    np.append(z[:4], z[0]),
                    'b.-')
            ax.plot(np.append(x[4:8], x[4]),
                    np.append(y[4:8], y[4]),
                    np.append(z[4:8], z[4]),
                    'b.-')
            ax.plot(np.array([x[0], x[4]]),
                    np.array([y[0], y[4]]),
                    np.array([z[0], z[4]]), 'b.-')
            ax.plot(np.array([x[1], x[5]]),
                    np.array([y[1], y[5]]),
                    np.array([z[1], z[5]]), 'b.-')
            ax.plot(np.array([x[2], x[6]]),
                    np.array([y[2], y[6]]),
                    np.array([z[2], z[6]]), 'b.-')
            ax.plot(np.array([x[3], x[7]]),
                    np.array([y[3], y[7]]),
                    np.array([z[3], z[7]]), 'b.-')
            # ax.axis('equal')


# quantities are grouped per element
# a frame element has 2 nodes (start, end)
# ex =  [x1, x2],   ey  = [y1, y2]
# eux = [ux1, ux2], edy = [uy1, uy2]
# edx = [x1+ux1, x2+ux2], edy = [y1+uy1, y2+uy2] thus
# edx = [xd1, xd2],       edy = [yd1, yd2]
# ---------------------------------------------------------------------+
def plot_defo(sfac=False, npt=21, unDefoFlag=1, fmtu=fmtu, interpFlag=1,
              endDispFlag=1, fmtc=fmtc, fmte=fmte, Eo=0, az_el=az_el,
              fig_wi_he=fig_wi_he, fig_lbrt=fig_lbrt):

    node_tags = ops.getNodeTags()

    # calculate sfac
    min_x, min_y, min_z = np.inf, np.inf, np.inf
    max_x, max_y, max_z = -np.inf, -np.inf, -np.inf
    max_ux, max_uy, max_uz = -np.inf, -np.inf, -np.inf
    krel = 0.1

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
            sfac = krel * dlmax/edmax
            print(f'\n- scale factor automatically calculated; sfac: {sfac} ')
            if sfac > 1000.:
                print('\nWarning!!!\nsfac is quite large - perhaps try to specify \
sfac value yourself.')
                print('This usually happens when translational DOFs are \
too small\n\n')

        _plot_defo_mode_2d(0, sfac, npt, unDefoFlag, fmtu, interpFlag,
                           endDispFlag, fmtc, fmte)

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
            sfac = krel * dlmax/edmax
            print(f'\n- scale factor automatically calculated; sfac: {sfac} ')

        _plot_defo_mode_3d(0, sfac, npt, unDefoFlag, fmtu, interpFlag,
                           endDispFlag, fmtc, fmte, Eo, az_el, fig_wi_he,
                           fig_lbrt)

    else:
        print(f'ndim = ndim: {ndim} not supported yet. Supported are 2d \
        and 3d models')


# this fun is similar to plot_defo
def plot_mode(modeNo, sfac=False, npt=21, unDefoFlag=1, fmtu=fmtu,
              interpFlag=1, endDispFlag=1, fmtc=fmtc, fmte=fmte, Eo=0,
              az_el=az_el, fig_wi_he=fig_wi_he, fig_lbrt=fig_lbrt):

    node_tags = ops.getNodeTags()

    # calculate sfac
    min_x, min_y, min_z = np.inf, np.inf, np.inf
    max_x, max_y, max_z = -np.inf, -np.inf, -np.inf
    max_ux, max_uy, max_uz = -np.inf, -np.inf, -np.inf
    krel = 0.1

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
            sfac = krel * dlmax/edmax
            print(f'\n- scale factor automatically calculated; sfac: {sfac} ')

        _plot_defo_mode_2d(modeNo, sfac, npt, unDefoFlag, fmtu, interpFlag,
                           endDispFlag, fmtc, fmte)

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
            sfac = krel * dlmax/edmax
            print(f'\n- scale factor automatically calculated; sfac: {sfac} ')

        _plot_defo_mode_3d(modeNo, sfac, npt, unDefoFlag, fmtu, interpFlag,
                           endDispFlag, fmtc, fmte, Eo, az_el, fig_wi_he,
                           fig_lbrt)

    else:
        print(f'ndim = ndim: {ndim} not supported yet. Supported are 2d \
        and 3d models')


def beam_3d_gtrans(ex, ey, ez, eo):
    # projections of element Length to x, y and z axis in b vector
    b = np.array([ex[1]-ex[0], ey[1]-ey[0], ez[1]-ez[0]])

    L = np.sqrt(b @ b)
    n1 = b / L
    lc = np.sqrt(eo @ eo)
    n3 = eo / lc

    n2 = np.zeros(3)
    n2[0] = n3[1]*n1[2]-n3[2]*n1[1]
    n2[1] = -n1[2]*n3[0]+n1[0]*n3[2]
    n2[2] = n3[0]*n1[1]-n1[0]*n3[1]

    A = np.vstack((n1, n2, n3))
    Z = np.zeros((3, 3))

    G = np.block([[A, Z, Z, Z],
                  [Z, A, Z, Z],
                  [Z, Z, A, Z],
                  [Z, Z, Z, A]])
    return G, L


def beam_defo_interp_3d(ex, ey, ez, eo, d, sfac, npt=21):
    """
    Calculate the element deformation at npt points inside the element.
    Interpolate displacements inside element.
    """
    G, L = beam_3d_gtrans(ex, ey, ez, eo)
    dl = G @ d
    print(f'd:\n{d}')
    print(f'dl:\n{dl}')
    excd, eycd = beam_defo_interp_2d(np.array([0., L]),
                                     np.array([0., 0.]),
                                     np.array([dl[0], dl[1], dl[5], dl[6],
                                               dl[7], dl[11]]), sfac, npt)
    excd, ezcd = beam_defo_interp_2d(np.array([0., L]),
                                     np.array([0., 0.]),
                                     np.array([dl[0], dl[2], -dl[4], dl[6],
                                               dl[8], -dl[10]]), sfac, npt)
    xu = np.linspace(0., 1., num=npt)
    excd = excd - L*xu
    gd = np.transpose(G[0:3, 0:3]) @ np.vstack([excd, eycd, ezcd])
    excd = gd[0, :] + ex[0] + (ex[1]-ex[0])*xu
    eycd = gd[1, :] + ey[0] + (ey[1]-ey[0])*xu
    ezcd = gd[2, :] + ez[0] + (ez[1]-ez[0])*xu

    return excd, eycd, ezcd


# credit: based on https://github.com/CALFEM/calfem-matlab
# ported from beam2crd.m calfem - changed name
# he calculations are only for one element
# differences: Ex,Ey -> ex,ey;  Ed -> d
# ---------------------------------------------------------------------+
def beam_defo_interp_2d(ex, ey, d, sfac, npt=21):
    """
    Calculate the FE element deformation at npt numbers of points,
    inside the element. Interpolate displacements inside element.
    """

    # excd = np.zeros((1, npt))
    # eycd = np.zeros((1, npt))

    # projections of element Length to x, and y axis in b vector
    b = np.array([ex[1]-ex[0], ey[1]-ey[0]])
    L = np.sqrt(b @ b)
    n = b / L
    G = np.array([[n[0], n[1], 0., 0., 0., 0],
                  [-n[1], n[0], 0., 0., 0., 0],
                  [0., 0., 1, 0., 0., 0],
                  [0., 0., 0., n[0], n[1], 0],
                  [0., 0., 0., -n[1], n[0], 0],
                  [0., 0., 0., 0., 0., 1]])

    dl = G @ d
    xl = np.linspace(0., L, num=npt)
    one = np.ones(xl.shape)

    # shape function for rigid movement
    Cis = np.array([[-1, 1], [L, 0.]])/L

    # extract rigid (longitudinal) displacement
    ds = np.array([dl[0], dl[3]])

    ul1 = np.column_stack((xl, one))

    # longitudinal deformation (1)
    ul = ul1 @ Cis @ ds

    Cib = np.array([[12., 6.*L, -12., 6.*L],
                    [-6.*L, -4.*L**2., 6.*L, -2.*L**2],
                    [0., L**3., 0., 0.],
                    [L**3., 0., 0., 0.]])/L**3.

    # extract deformation: transverse displ and rotation
    db = np.array([dl[1], dl[2], dl[4], dl[5]])

    vl1 = np.column_stack((xl**3./6., xl**2./2., xl, one))

    # transverse deformation (2)
    vl = vl1 @ Cib @ db

    # matrix composed of two row vectors
    # 1-st vector longitudinal deformation (1)
    # 2-nd vector transverse deformation (2)
    cld = np.vstack((ul, vl))

    # print('-- combined row vectors ul and vl')

    A1 = np.array([[n[0], -n[1]], [n[1], n[0]]])

    cd = A1 @ cld

    A11 = A1[:, 0].reshape(-1, 1)
    # A11 = A1[:, 0].T

    # discretize (make in quasi continuous)
    # continuous x, y vectors, for example for L = 5, Lx = 4, Ly = 3
    # first  row = [0 dx 2dx ... 4-dx 4]
    # second row = [0 dy 2dy ... 3-dy 3]
    xyc1 = A11 @ xl.reshape(1, -1)

    # vert 2d array vector
    # shift xyc1 vector to the right (x) and up (y)
    xyc2 = np.array([[ex[0]], [ey[0]]])

    # continuous x, y vectors, for example for L = 5, Lx = 4, Ly = 3
    # shifted accordingly if the element does not start from the beginng
    # of the coordinate system

    # first  row = X + [0 dx 2dx ... 4-dx 4]
    # second row = Y + [0 dy 2dy ... 3-dy 3]
    xyc = xyc1 + xyc2

    # Continuous x, y displacement matrices (1 x 2)
    excd = xyc[0, :] + sfac*cd[0, :]
    eycd = xyc[1, :] + sfac*cd[1, :]

    return excd, eycd


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


# Read data
#
# check whether they are (1)counterclockwise and (2)form a convex
# quadrilateral in the y,z coord system
#
#  z          L*     *K
#  |
#  |        I*       *J
#  |
#  +-----y
#
# We will achieve this by calculating the outer products of
# the vectors IJ x IK and IK x IL. If both are positive,
# we have convex and counter-clockwise quadrangle.
# Since all vectors have no x-component, the outerproduct
# is always along the x-axis and it is calculated as
# a x b = | ya  za | * (unit x-vector)
#         | yb  zb |
# where ya,za are the vector coords (ya=ya2-ya1, za=za2-za1)
# def plot_section(fib_type, nIJ, nJK, Iy, Iz, Ky, Kz, Jy=0, Jz=0, Ly=0, Lz=0):
def plot_section(fib_sec_list, fillflag=1,
                 matcolor=['y', 'b', 'r', 'g', 'm', 'k']):
    """
    Plot fiber section.
    """

    fig, ax = plt.subplots()
    ax.set_xlabel('z')
    ax.set_ylabel('y')
    ax.grid(False)

    for item in fib_sec_list:
        if item[0] == 'section':
            secTag = item[2]
            print(f'\n- display fiber section for Tag: {secTag} using \
Matplotlib')

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
                    print(f'z, y:\n{zi, yi}')
                    bar = Circle((zi, yi), r, ec='k', fc='k', zorder=10)
                    ax.add_patch(bar)

        if item[0] == 'patch':
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
                print(f'Patch quad is non-convex or counter-clockwise defined or has at \
                least 3 colinear points in line')

            IJz = np.linspace(Iz, Jz, nIJ+1)
            IJy = np.linspace(Iy, Jy, nIJ+1)
            JKz = np.linspace(Jz, Kz, nJK+1)
            JKy = np.linspace(Jy, Ky, nJK+1)
            LKz = np.linspace(Lz, Kz, nIJ+1)
            LKy = np.linspace(Ly, Ky, nIJ+1)
            ILz = np.linspace(Iz, Lz, nJK+1)
            ILy = np.linspace(Iy, Ly, nJK+1)

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


def fib_section(fib_sec_list):
    """
    This function re-uses fib_sec_list to define fiber section in OpenSees

    fib_sec_list is a list of fiber section data. First sub-list also defines
    '-GJ' torsion stiffness.
    """
    for dat in fib_sec_list:
        if dat[0] == 'section':
            secTag = dat[2]
            ops.section('Fiber', secTag)

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


# credit: based on beam2s from https://github.com/CALFEM/calfem-matlab
def beam_sf_2d(ex, ey, E, A, I, d, nep=2,
               ele_load_data=['-beamUniform', 0., 0.]):
    """
    Calculate section forces (N, V, M) for a 2d elastic Euler-Bernoulli beam.

    Input:
    ex, ey - x, y element coordinates in global system
    E, A, I - modulus of elasticity, section area, moment of inertia
    d - nodal element displacements in global system
    nep - number of evaluation points, by default (2) at element ends
    ele_load_list - list of transverse and longitudinal element load
      syntax: [ele_load_type, Wy, Wx]
      For now only '-beamUniform' element load type is acceptable

    Output:
    s = [N V M]; shape: (nep,3)
        section forces at nep points along local x
    uv = [u v]; shape: (nep, 2)
         displacements at nep points along local x
    xl: coordinates of local x-axis; shape: (nep,)

    Use it with eldia_2d to draw N, V, M diagrams.

    TODO: add '-beamPoint' element load type
    """

    eload_type, qy, qx = ele_load_data[0], ele_load_data[1], ele_load_data[2]

    EA, EI = E*A, E*I

    b = np.array([ex[1]-ex[0], ey[1]-ey[0]])
    L = np.sqrt(b @ b)
    n = b / L

    C = np.array([[0.,      0.,   0., 1., 0., 0.],
                  [0.,      0.,   0., 0., 0., 1.],
                  [0.,      0.,   0., 0., 1., 0.],
                  [L,       0.,   0., 1., 0., 0.],
                  [0.,    L**3, L**2, 0.,  L, 1.],
                  [0., 3.*L**2, 2.*L, 0., 1., 0.]])

    G = np.array([[n[0],  n[1], 0.,    0.,   0., 0.],
                  [-n[1], n[0], 0.,    0.,   0., 0.],
                  [0.,      0., 1,     0.,   0., 0.],
                  [0.,      0., 0.,  n[0], n[1], 0.],
                  [0.,      0., 0., -n[1], n[0], 0.],
                  [0.,      0., 0.,    0.,   0., 1.]])

    # global to local element displacements
    dl = G @ d

    if eload_type == '-beamUniform':
        Q = np.array([0., 0., 0.,
                      -1.*qx*(L**2)/(2.*EA),
                      qy*(L**4)/(24.*EI),
                      qy*(L**3)/(6.*EI)])
    else:
        Q = np.array([0., 0., 0., 0., 0., 0.])

    Cinv = np.linalg.inv(C)
    dlmQ = dl - Q
    c = Cinv @ dlmQ

    a = np.array([c[0], c[3]])
    b = np.array([c[1], c[2], c[4], c[5]])

    xl = np.linspace(0., L, nep)
    zero = np.zeros(nep)
    one = np.ones(nep)

    u = np.column_stack((xl, one)) @ a - xl**2 * qx/(2*EA)

    du = np.column_stack((one, zero)) @ a - xl*qx/EA

    v = np.column_stack((xl**3, xl**2, xl, one)) @ b + xl**4 * qy/(24*EI)

    d2v = np.column_stack((6*xl, 2*one, zero, zero)) @ b + \
        xl**2 * qy/(2.*EI)

    d3v = np.column_stack((6*one, zero, zero, zero)) @ b + xl * qy/EI

    N = EA * du
    M = EI * d2v
    V = -EI * d3v
    uv = np.column_stack((u, v))
    s = np.column_stack((N, V, M))

    return (s, uv, xl, b, L, n)


# credit: based on beam3s from https://github.com/CALFEM/calfem-matlab
def beam_sf_3d(ex, ey, ez, eo, E, G, A, Iy, Iz, J, d, nep=2,
               ele_load_data=['-beamUniform', 0., 0., 0.]):
    """
    Calculate section forces (N, Vy, Vz, T, My, Mz) for a 3d elastic beam.

    Input:
    ex, ey, ez - x, y, z element coordinates in global system
    E, G, - modulus of elasticity, shear modulus
    A, Iy, Iz, J - section area, moment of inertia about y/z axis,
                   torsion constant
    d - nodal element displacements in global system
    nep - number of evaluation points, by default (2) at element ends
    ele_load_list - list of transverse and longitudinal element load
      syntax: [ele_load_type, Wy, Wz, Wx]
      For now only '-beamUniform' element load type is acceptable.

    Output:
    s = [N Vx Vy T My Mz]; shape: (nep,6)
        column vectors of section forces along local x-axis

    uvwfi = [u v w fi]; shape (nep,4)
        displacements at nep points along local x

    xl: coordinates of local x-axis; shape (nep,)

    TODO: add '-beamPoint' element load type
    """

    eload_type = ele_load_data[0]
    qy, qz, qx = ele_load_data[1], ele_load_data[2], ele_load_data[3]

    EA, EIy, EIz, GJ = E*A, E*Iy, E*Iz, G*J

    G, L = beam_3d_gtrans(ex, ey, ez, eo)
    print(f'L: {L}')
    print(f'G:\n{G}')

    C = np.array([[0., 1., 0., 0., 0., 0., 0., 0.,  0., 0., 0., 0.],
                  [0., 0., 0., 0., 0., 1., 0., 0.,  0., 0., 0., 0.],
                  [0., 0., 0., 0., 0., 0., 0., 0.,  0., 1., 0., 0.],
                  [0., 0., 0., 0., 0., 0., 0., 0.,  0., 0., 0., 1.],
                  [0., 0., 0., 0., 0., 0., 0., 0., -1., 0., 0., 0.],
                  [0., 0., 0., 0., 1., 0., 0., 0.,  0., 0., 0., 0.],
                  [L, 1.,  0., 0., 0., 0., 0., 0.,  0., 0., 0., 0.],
                  [0., 0., L**3, L**2, L, 1., 0., 0., 0., 0., 0., 0.],
                  [0., 0., 0., 0., 0., 0., L**3, L**2, L, 1., 0., 0.],
                  [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., L, 1.],
                  [0., 0., 0., 0., 0., 0., -3.*L**2, -2.*L, -1., 0., 0., 0.],
                  [0., 0., 3.*L**2, 2.*L, 1., 0., 0., 0., 0., 0., 0., 0.]])

    print(f'C: {C}')

    # global to local nodal element displacements
    dl = G @ d
    print(f'd: {d}')
    print(f'dl: {dl}')

    # -qw*(L**2)/(2.*GJ),
    if eload_type == '-beamUniform':
        Q = np.array([0., 0., 0., 0., 0., 0.,
                      -1.*qx*(L**2)/(2.*EA),
                      qy*(L**4)/(24.*EIz),
                      qz*(L**4)/(24.*EIy),
                      0.,  # no qw in OpenSees -qw*(L**2)/(2.*GJ)
                      qz*(L**3)/(6.*EIy),
                      qy*(L**3)/(6.*EIz)])
    else:
        Q = np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

    Cinv = np.linalg.inv(C)
    dlmQ = dl - Q
    c = Cinv @ dlmQ

    xl = np.linspace(0., L, nep)
    one = np.ones(nep)

    AA = np.zeros((nep, 12))
    AA[:, 0:2] = np.column_stack((xl, one))
    u = AA @ c - qx*xl**2/(2.*EA)

    AA = np.zeros((nep, 12))
    AA[:, 2:6] = np.column_stack((xl**3, xl**2, xl, one))
    v = AA @ c + qy*xl**4/(24.*EIz)

    AA = np.zeros((nep, 12))
    AA[:, 6:10] = np.column_stack((xl**3, xl**2, xl, one))
    w = AA @ c + qz*xl**4/(24.*EIy)

    AA = np.zeros((nep, 12))
    AA[:, 10:12] = np.column_stack((xl, one))
    fi = AA @ c  # (- qx*xl**2/(2.*EA))

    AA = np.zeros((nep, 12))
    AA[:, 0] = EA*one
    N = AA @ c - qx*xl

    AA = np.zeros((nep, 12))
    AA[:, 2] = -6.*EIz*one
    Vy = AA @ c - qy*xl

    AA = np.zeros((nep, 12))
    AA[:, 6] = -6.*EIy*one
    Vz = AA @ c - qz*xl

    AA = np.zeros((nep, 12))
    AA[:, 10] = GJ*one
    T = AA @ c  # (- qw*xl)

    AA = np.zeros((nep, 12))
    AA[:, 6:8] = np.column_stack((-6.*EIy*xl, -2.*EIy*one))
    My = AA @ c - 0.5*qy*xl**2

    AA = np.zeros((nep, 12))
    AA[:, 2:4] = np.column_stack((6.*EIz*xl, 2.*EIz*one))
    Mz = AA @ c + 0.5*qy*xl**2

    uvwfi = np.column_stack((u, v, w, fi))
    s = np.column_stack((N, Vy, Vz, T, My, Mz))

    # return (s, uvwfi, xl, b, L, n)
    return (s, uvwfi, xl)


def eldia_2d(ex, ey, s, sfac=1., fmtsf=fmtsf):
    """
    Draw section forces diagrams (N, V, M)
    """

    nep = s.shape[0]

    # FIXME in this form it only applies to one member
    # create a loop as in eldisp2
    # b = np.array([ex[i, 1]-ex[i, 0], ey[i, 1]-ey[i, 0]])
    b = np.array([ex[1]-ex[0], ey[1]-ey[0]])
    L = np.sqrt(b @ b)
    n = b / L

    # sfac = (0.2*L)/np.max(np.abs(s))
    xl = np.linspace(0., L, nep)

    s = s*sfac

    A = np.zeros((nep, 2))
    A[0, :] = [ex[0], ey[0]]

    A[1:, 0] = A[0, 0] + xl[1:] * n[0]
    A[1:, 1] = A[0, 1] + xl[1:] * n[1]

    B = np.copy(A)

    A[:, 0] = A[:, 0] + s * n[1]
    A[:, 1] = A[:, 1] - s * n[0]

    plt.axis('equal')

    # curve
    plt.plot(A[:, 0], A[:, 1], fmtsf,
             solid_capstyle='round', solid_joinstyle='round',
             dash_capstyle='butt', dash_joinstyle='round')

    # origin model
    plt.plot(ex, ey, 'k-', solid_capstyle='round', solid_joinstyle='round',
             dash_capstyle='butt', dash_joinstyle='round')

    # hatching
    for i in np.arange(nep):
        plt.plot([B[i, 0], A[i, 0]], [B[i, 1], A[i, 1]], fmtsf,
                 solid_capstyle='round', solid_joinstyle='round',
                 dash_capstyle='butt', dash_joinstyle='round')


# credit: eldia2 from https://github.com/CALFEM/calfem-matlab
def dia_sf(sf_type, Ep, Ew, sfac=1., nep=21, fmtsf=fmtsf):
    """
    Draw section forces diagrams (N, V, M)

    sf_type: string N, V or M
    """

    maxVal, minVal = -np.inf, np.inf
    ele_tags = ops.getEleTags()

    for ele_tag in ele_tags:

        if ele_tag in Ep:
            E, A, Iz = Ep[ele_tag]

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

        ed = np.array([ops.nodeDisp(nd1)[0],
                       ops.nodeDisp(nd1)[1],
                       ops.nodeDisp(nd1)[2],
                       ops.nodeDisp(nd2)[0],
                       ops.nodeDisp(nd2)[1],
                       ops.nodeDisp(nd2)[2]])

        s_all, uv, xl, b, L, n = beam_sf_2d(ex, ey, E, A, Iz, ed,
                                            nep, eload_data)

        if sf_type == 'N':
            s = s_all[:, 0]
        elif sf_type == 'V' or sf_type == 'T':
            s = s_all[:, 1]
        elif sf_type == 'M':
            s = s_all[:, 2]

        minVal = min(minVal, np.min(s))
        maxVal = max(maxVal, np.max(s))

        s = s*sfac

        AA = np.zeros((nep, 2))
        AA[0, :] = [ex[0], ey[0]]

        AA[1:, 0] = AA[0, 0] + xl[1:] * n[0]
        AA[1:, 1] = AA[0, 1] + xl[1:] * n[1]

        BB = np.copy(AA)

        AA[:, 0] = AA[:, 0] + s * n[1]
        AA[:, 1] = AA[:, 1] - s * n[0]

        plt.axis('equal')

        # curve
        plt.plot(AA[:, 0], AA[:, 1], fmtsf,
                 solid_capstyle='round', solid_joinstyle='round',
                 dash_capstyle='butt', dash_joinstyle='round')

        # origin model
        plt.plot(ex, ey, 'k-', solid_capstyle='round', solid_joinstyle='round',
                 dash_capstyle='butt', dash_joinstyle='round')

        # hatching
        for i in np.arange(nep):
            plt.plot([BB[i, 0], AA[i, 0]], [BB[i, 1], AA[i, 1]], fmtsf,
                     solid_capstyle='round', solid_joinstyle='round',
                     dash_capstyle='butt', dash_joinstyle='round')
    return minVal, maxVal
