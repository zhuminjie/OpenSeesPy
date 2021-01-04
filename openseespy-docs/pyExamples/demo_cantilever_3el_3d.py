import openseespy.opensees as ops
import openseespy.postprocessing.ops_vis as opsv
# import opensees as ops  # local compilation
# import ops_vis as opsv  # local

import matplotlib.pyplot as plt

ops.wipe()

ops.model('basic', '-ndm', 3, '-ndf', 6)

b = 0.2
h = 0.4

A, Iz, Iy, J = 0.04, 0.0010667, 0.0002667, 0.01172

E = 25.0e6
G = 9615384.6

# Lx, Ly, Lz = 4., 3., 5.
Lx, Ly, Lz = 4., 4., 4.

ops.node(1, 0., 0., 0.)
ops.node(2, 0., 0., Lz)
ops.node(3, Lx, 0., Lz)
ops.node(4, Lx, Ly, Lz)

ops.fix(1, 1, 1, 1, 1, 1, 1)

lmass = 200.

ops.mass(2, lmass, lmass, lmass, 0.001, 0.001, 0.001)
ops.mass(3, lmass, lmass, lmass, 0.001, 0.001, 0.001)
ops.mass(4, lmass, lmass, lmass, 0.001, 0.001, 0.001)

gTTagz = 1
gTTagx = 2
gTTagy = 3

coordTransf = 'Linear'
ops.geomTransf(coordTransf, gTTagz, 0., -1., 0.)
ops.geomTransf(coordTransf, gTTagx, 0., -1., 0.)
ops.geomTransf(coordTransf, gTTagy, 1., 0., 0.)

ops.element('elasticBeamColumn', 1, 1, 2, A, E, G, J, Iy, Iz, gTTagz)
ops.element('elasticBeamColumn', 2, 2, 3, A, E, G, J, Iy, Iz, gTTagx)
ops.element('elasticBeamColumn', 3, 3, 4, A, E, G, J, Iy, Iz, gTTagy)

Ew = {}

Px = -4.e1
Py = -2.5e1
Pz = -3.e1

ops.timeSeries('Constant', 1)
ops.pattern('Plain', 1, 1)
ops.load(4, Px, Py, Pz, 0., 0., 0.)

ops.constraints('Transformation')
ops.numberer('RCM')
ops.system('BandGeneral')
ops.test('NormDispIncr', 1.0e-6, 6, 2)
ops.algorithm('Linear')
ops.integrator('LoadControl', 1)
ops.analysis('Static')
ops.analyze(1)


opsv.plot_model()

sfac = 2.0e0

# fig_wi_he = 22., 14.
fig_wi_he = 30., 20.

# - 1
nep = 9
opsv.plot_defo(sfac, nep, fmt_interp='b-', az_el=(-68., 39.),
               fig_wi_he=fig_wi_he, endDispFlag=0)

plt.title('3d 3-element cantilever beam')

# - 2
opsv.plot_defo(sfac, 19, fmt_interp='b-', az_el=(6., 30.),
               fig_wi_he=fig_wi_he)

plt.title('3d 3-element cantilever beam')

# - 3
nfreq = 6
eigValues = ops.eigen(nfreq)

modeNo = 6

sfac = 2.0e1
opsv.plot_mode_shape(modeNo, sfac, 19, fmt_interp='b-', az_el=(106., 46.),
                     fig_wi_he=fig_wi_he)
plt.title(f'Mode {modeNo}')

sfacN = 1.e-2
sfacVy = 5.e-2
sfacVz = 1.e-2
sfacMy = 1.e-2
sfacMz = 1.e-2
sfacT = 1.e-2

# plt.figure()
minY, maxY = opsv.section_force_diagram_3d('N', Ew, sfacN)
plt.title(f'Axial force N, max = {maxY:.2f}, min = {minY:.2f}')

minY, maxY = opsv.section_force_diagram_3d('Vy', Ew, sfacVy)
plt.title(f'Transverse force Vy, max = {maxY:.2f}, min = {minY:.2f}')

minY, maxY = opsv.section_force_diagram_3d('Vz', Ew, sfacVz)
plt.title(f'Transverse force Vz, max = {maxY:.2f}, min = {minY:.2f}')

minY, maxY = opsv.section_force_diagram_3d('My', Ew, sfacMy)
plt.title(f'Bending moments My, max = {maxY:.2f}, min = {minY:.2f}')

minY, maxY = opsv.section_force_diagram_3d('Mz', Ew, sfacMz)
plt.title(f'Bending moments Mz, max = {maxY:.2f}, min = {minY:.2f}')

minY, maxY = opsv.section_force_diagram_3d('T', Ew, sfacT)
plt.title(f'Torsional moment T, max = {maxY:.2f}, min = {minY:.2f}')

# just for demonstration,
# the section data below does not match the data in OpenSees model above
# For now it can be source of inconsistency because OpenSees has
# not got functions to return section dimensions.
# A workaround is to have own Python helper functions to reuse data
# specified once
ele_shapes = {1: ['circ', [h]],
              2: ['rect', [b, h]],
              3: ['I', [b, h, b/10., h/6.]]}
opsv.plot_extruded_shapes_3d(ele_shapes, fig_wi_he=fig_wi_he)

plt.show()

exit()
