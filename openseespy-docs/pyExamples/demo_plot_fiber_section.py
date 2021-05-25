import openseespy.opensees as ops
import openseespy.postprocessing.ops_vis as opsv
# import opensees as ops  # local compilation
# import ops_vis as opsv  # local

import matplotlib.pyplot as plt

ops.wipe()
ops.model('basic', '-ndm', 2, '-ndf', 3)  # frame 2D

# 1. rotated steel shape

fib_sec_1 = [['section', 'Fiber', 1, '-GJ', 1.0e6],
             ['patch', 'quad', 1, 4, 1,  0.032, 0.317, -0.311, 0.067, -0.266, 0.005, 0.077, 0.254],
             ['patch', 'quad', 1, 1, 4,  -0.075, 0.144, -0.114, 0.116, 0.075, -0.144, 0.114, -0.116],
             ['patch', 'quad', 1, 4, 1,  0.266, -0.005,  -0.077, -0.254,  -0.032, -0.317,  0.311, -0.067]
             ]

# fib_sec_1 list can be used both for plotting and OpenSees commands defining
# the actual fiber section in the OpenSees domain. Normally you would have to
# use regular section('Fiber', ...), fiber(), layer(), patch() commands with
# the same data to define the fiber section. However do not use both
# ways in the same model.

# opsv.fib_sec_list_to_cmds(fib_sec_1)

# 2. RC section

Bcol = 0.711
Hcol = Bcol

c = 0.076  # cover

y1col = Hcol/2.0
z1col = Bcol/2.0

y2col = 0.5*(Hcol-2*c)/3.0

nFibZ = 1
nFib = 20
nFibCover, nFibCore = 2, 16
As9 = 0.0006446

fib_sec_2 = [['section', 'Fiber', 3, '-GJ', 1.0e6],
             ['patch', 'rect', 2, nFibCore, nFibZ, c-y1col, c-z1col, y1col-c, z1col-c],
             ['patch', 'rect', 3, nFib, nFibZ, -y1col, -z1col, y1col, c-z1col],
             ['patch', 'rect', 3, nFib, nFibZ, -y1col, z1col-c, y1col, z1col],
             ['patch', 'rect', 3, nFibCover, nFibZ, -y1col, c-z1col, c-y1col, z1col-c],
             ['patch', 'rect', 3, nFibCover, nFibZ, y1col-c, c-z1col, y1col, z1col-c],
             ['layer', 'straight', 4, 4, As9, y1col-c, z1col-c, y1col-c, c-z1col],
             ['layer', 'straight', 4, 2, As9, y2col, z1col-c, y2col, c-z1col],
             ['layer', 'straight', 4, 2, As9, -y2col, z1col-c, -y2col, c-z1col],
             ['layer', 'straight', 4, 4, As9, c-y1col, z1col-c, c-y1col, c-z1col]]


# opsv.fib_sec_list_to_cmds(fib_sec_2)

matcolor = ['r', 'lightgrey', 'gold', 'w', 'w', 'w']
opsv.plot_fiber_section(fib_sec_1, matcolor=matcolor)
plt.axis('equal')
# plt.savefig('fibsec_wshape.png')

matcolor = ['r', 'lightgrey', 'gold', 'w', 'w', 'w']
opsv.plot_fiber_section(fib_sec_2, matcolor=matcolor)
plt.axis('equal')
# plt.savefig('fibsec_rc.png')

# circular cross-section
nc1, nr1 = 8, 3
nc2, nr2 = 8, 2
ri1, re1 = 0.1, 0.2
ri2, re2 = 0.2, 0.25
a_beg, a_end = 0., 360.
rbar3 = 0.225
a_beg2, a_end2 = 0., 360.

fib_sec_3 = [['section', 'Fiber', 1, '-GJ', 1.0e6],
             ['patch', 'circ', 2, nc1, nr1, 0., 0., ri1, re1, a_beg, a_end],
             ['patch', 'circ', 3, nc2, nr2, 0., 0., ri2, re2, a_beg, a_end],
             ['layer', 'circ', 4, 6, As9, 0., 0., rbar3, a_beg2, a_end2],
             ]


matcolor = ['r', 'lightgrey', 'gold', 'w', 'w', 'w']
opsv.plot_fiber_section(fib_sec_3, matcolor=matcolor)
plt.axis('equal')
# plt.savefig('fibsec_circ.png')

plt.show()
