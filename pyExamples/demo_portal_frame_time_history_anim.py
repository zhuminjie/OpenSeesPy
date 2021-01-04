import openseespy.opensees as ops
import openseespy.postprocessing.ops_vis as opsv
# import opensees as ops  # local compilation
# import ops_vis as opsv  # local

import numpy as np
import matplotlib.pyplot as plt

# input_parameters = (3.8, 50., 100.)
# input_parameters = (53.5767, 50., 100.)
input_parameters = (20.8, 300., 8.)
# input_parameters = (70.0, 500., 2.)

pf, sfac_a, tkt = input_parameters

ops.wipe()
ops.model('basic', '-ndm', 2, '-ndf', 3)  # frame 2D

colL, girL = 4., 6.

Acol, Agir = 0.06, 0.06
IzCol, IzGir = 0.0002, 0.0002

E = 3.2e10
rho = 2400.
muCol = rho * Acol
muGir = rho * Agir
massCol = ['-mass', muCol, '-cMass']
massGir = ['-mass', muGir, '-cMass']

ops.node(0, 0.0, 0.0)
ops.node(1, 0.0, 2.0)
ops.node(2, 0.0, 4.0)
ops.node(3, 3.0, 4.0)
ops.node(4, 6.0, 4.0)
ops.node(5, 6.0, 2.0)
ops.node(6, 6.0, 0.0)

ops.fix(0, 1, 1, 1)
ops.fix(6, 1, 1, 0)

gTTag = 1
ops.geomTransf('Linear', gTTag)

# 1st column
ops.element('elasticBeamColumn', 1, 0, 1, Acol, E, IzCol, gTTag, *massCol)
ops.element('elasticBeamColumn', 2, 1, 2, Acol, E, IzCol, gTTag, *massCol)
# girder
ops.element('elasticBeamColumn', 3, 2, 3, Agir, E, IzGir, gTTag, *massGir)
ops.element('elasticBeamColumn', 4, 3, 4, Agir, E, IzGir, gTTag, *massGir)
# 2nd column
ops.element('elasticBeamColumn', 5, 4, 5, Acol, E, IzCol, gTTag, *massCol)
ops.element('elasticBeamColumn', 6, 5, 6, Acol, E, IzCol, gTTag, *massCol)

t0 = 0.
tk = 1.
Tp = 1/pf
P0 = 15000.
dt = 0.002
n_steps = int((tk-t0)/dt)

tsTag = 1
ops.timeSeries('Trig', tsTag, t0, tk, Tp, '-factor', P0)

patTag = 1
ops.pattern('Plain', patTag, tsTag)
ops.load(1, 1., 0., 0.)

ops.constraints('Transformation')
ops.numberer('RCM')
ops.test('NormDispIncr', 1.0e-6, 10, 1)
ops.algorithm('Linear')
ops.system('ProfileSPD')
ops.integrator('Newmark', 0.5, 0.25)
ops.analysis('Transient')

el_tags = ops.getEleTags()

nels = len(el_tags)

Eds = np.zeros((n_steps, nels, 6))
timeV = np.zeros(n_steps)

# transient analysis loop and collecting the data
for step in range(n_steps):
    ops.analyze(1, dt)
    timeV[step] = ops.getTime()
    # collect disp for element nodes
    for el_i, ele_tag in enumerate(el_tags):
        nd1, nd2 = ops.eleNodes(ele_tag)
        Eds[step, el_i, :] = [ops.nodeDisp(nd1)[0],
                              ops.nodeDisp(nd1)[1],
                              ops.nodeDisp(nd1)[2],
                              ops.nodeDisp(nd2)[0],
                              ops.nodeDisp(nd2)[1],
                              ops.nodeDisp(nd2)[2]]

# 1. animate the deformed shape
anim = opsv.anim_defo(Eds, timeV, sfac_a, interpFlag=1, xlim=[-1, 7],
                      ylim=[-1, 5], fig_wi_he=(30., 22.))

plt.show()

# 2. after closing the window, animate the specified mode shape
eigVals = ops.eigen(5)

modeNo = 2  # specify which mode to animate
f_modeNo = np.sqrt(eigVals[modeNo-1])/(2*np.pi)  # i-th natural frequency

anim = opsv.anim_mode(modeNo, interpFlag=1, xlim=[-1, 7], ylim=[-1, 5],
                      fig_wi_he=(30., 22.))
plt.title(f'Mode {modeNo}, f_{modeNo}: {f_modeNo:.3f} Hz')

plt.show()
