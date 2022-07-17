import openseespy.opensees as ops
import openseespy.postprocessing.ops_vis as opsv
# import opensees as ops  # local compilation
# import ops_vis as opsv  # local

import matplotlib.pyplot as plt

ops.wipe()
ops.model('basic', '-ndm', 2, '-ndf', 2)
ops.node(1, 0., 0.)
ops.node(2, 0., 1.)
ops.node(3, 0., 2.)
ops.node(4, 0., 3.)
ops.node(5, 0., 4.)
ops.node(6, 1., 0.)
ops.node(7, 1., 1.)
ops.node(8, 1., 2.)
ops.node(9, 1., 3.)
ops.node(10, 1., 4.)
ops.node(11, 2., 0.)
ops.node(12, 2., 1.)
ops.node(13, 2., 2.)
ops.node(14, 2., 3.)
ops.node(15, 2., 4.)
ops.node(16, 3., 0.)
ops.node(17, 3., 1.)
ops.node(18, 3., 2.)
ops.node(19, 3., 3.)
ops.node(20, 3., 4.)
ops.node(21, 4., 0.)
ops.node(22, 4., 1.)
ops.node(23, 4., 2.)
ops.node(24, 4., 3.)
ops.node(25, 4., 4.)

ops.nDMaterial('ElasticIsotropic', 1, 1000, 0.3)

ops.element('quad', 1, 1, 6, 7, 2, 1, 'PlaneStress', 1)
ops.element('quad', 2, 2, 7, 8, 3, 1, 'PlaneStress', 1)
ops.element('quad', 3, 3, 8, 9, 4, 1, 'PlaneStress', 1)
ops.element('quad', 4, 4, 9, 10, 5, 1, 'PlaneStress', 1)
ops.element('quad', 5, 6, 11, 12, 7, 1, 'PlaneStress', 1)
ops.element('quad', 6, 7, 12, 13, 8, 1, 'PlaneStress', 1)
ops.element('quad', 7, 8, 13, 14, 9, 1, 'PlaneStress', 1)
ops.element('quad', 8, 9, 14, 15, 10, 1, 'PlaneStress', 1)
ops.element('quad', 9, 11, 16, 17, 12, 1, 'PlaneStress', 1)
ops.element('quad', 10, 12, 17, 18, 13, 1, 'PlaneStress', 1)
ops.element('quad', 11, 13, 18, 19, 14, 1, 'PlaneStress', 1)
ops.element('quad', 12, 14, 19, 20, 15, 1, 'PlaneStress', 1)
ops.element('quad', 13, 16, 21, 22, 17, 1, 'PlaneStress', 1)
ops.element('quad', 14, 17, 22, 23, 18, 1, 'PlaneStress', 1)
ops.element('quad', 15, 18, 23, 24, 19, 1, 'PlaneStress', 1)
ops.element('quad', 16, 19, 24, 25, 20, 1, 'PlaneStress', 1)

ops.fix(1, 1, 1)
ops.fix(6, 1, 1)
ops.fix(11, 1, 1)
ops.fix(16, 1, 1)
ops.fix(21, 1, 1)

ops.equalDOF(2, 22, 1, 2)
ops.equalDOF(3, 23, 1, 2)
ops.equalDOF(4, 24, 1, 2)
ops.equalDOF(5, 25, 1, 2)

ops.timeSeries('Linear', 1)
ops.pattern('Plain', 1, 1)
ops.load(15, 0., -1.)

ops.analysis('Static')
ops.analyze(1)

# - plot model
plt.figure()
opsv.plot_model()
plt.axis('equal')

# - plot deformation
plt.figure()
opsv.plot_defo()
# opsv.plot_defo(sfac, unDefoFlag=1, fmt_undefo='g:')
plt.axis('equal')

# get values at OpenSees nodes
sig_out = opsv.sig_out_per_node()
print(f'sig_out:\n{sig_out}')

# - visu stress map

# !!! select from sig_out: e.g. vmises
# j, jstr = 0, 'sxx'
# j, jstr = 1, 'syy'
# j, jstr = 2, 'sxy'
j, jstr = 3, 'vmis'
# j, jstr = 4, 's1'
# j, jstr = 5, 's2'
# j, jstr = 6, 'alfa'

nds_val = sig_out[:, j]
# print(f'nds_val:\n{nds_val}')

plt.figure()
opsv.plot_stress_2d(nds_val)

plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title(f'{jstr}')

# plt.savefig(f'quads_4x4_{jstr}.png')

# for educational purposes show values at integration points and
# nodes which can finally be averaged at nodes
eles_ips_crd, eles_nds_crd, nds_crd, quads_conn = opsv.quad_crds_node_to_ip()

print(f'\neles_ips_crd:\n{eles_ips_crd}')
print(f'\neles_nds_crd:\n{eles_nds_crd}')
print(f'\nnds_crd:\n{nds_crd}')
print(f'\nquads_conn:\n{quads_conn}')

eles_ips_sig_out, eles_nds_sig_out = opsv.sig_out_per_ele_quad()

print(f'\neles_ips_sig_out:\n{eles_ips_sig_out}')
print(f'\neles_nds_sig_out:\n{eles_nds_sig_out}')

sig_out_indx = j  # same as j, jstr

fig = plt.figure(figsize=(22./2.54, 18./2.54))  # centimeter to inch conversion
fig.subplots_adjust(left=.08, bottom=.08, right=.985, top=.94)
opsv.plot_mesh_with_ips_2d(nds_crd, eles_ips_crd, eles_nds_crd, quads_conn,
                           eles_ips_sig_out, eles_nds_sig_out, sig_out_indx)

plt.xlabel('x [m]')
plt.ylabel('y [m]')

# plt.savefig(f'quads_4x4_{jstr}_ips_nds_vals.png')

plt.show()

exit()
