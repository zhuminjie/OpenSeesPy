import openseespy.opensees as ops

pid = ops.getPID()
np = ops.getNP()
ops.start()

ops.model('basic', '-ndm', 2, '-ndf', 2)

L = 48.0
H = 4.0

Lp = L / np
ndf = 2
meshsize = 0.05

ops.node(pid, Lp * pid, 0.0)
ops.node(pid + 1, Lp * (pid + 1), 0.0)
ops.node(np + pid + 2, Lp * (pid + 1), H)
ops.node(np + pid + 1, Lp * pid, H)

sid = 1
ops.setStartNodeTag(2 * np + 2 + pid * int(H / meshsize + 10))
ops.mesh('line', 3, 2, pid, np + pid + 1, sid, ndf, meshsize)
ops.setStartNodeTag(2 * np + 2 + (pid + 1) * int(H / meshsize + 10))
ops.mesh('line', 4, 2, pid + 1, np + pid + 2, sid, ndf, meshsize)

ops.setStartNodeTag(int(2 * L / meshsize + (np + 1) * H / meshsize * 2) +
                    pid * int(H * L / meshsize ** 2 * 2))
ops.mesh('line', 1, 2, pid, pid + 1, sid, ndf, meshsize)
ops.mesh('line', 2, 2, np + pid + 1, np + pid + 2, sid, ndf, meshsize)

ops.nDMaterial('ElasticIsotropic', 1, 3000.0, 0.3)

eleArgs = ['tri31', 1.0, 'PlaneStress', 1]

ops.mesh('quad', 5, 4, 1, 4, 2, 3, sid, ndf, meshsize, *eleArgs)


if pid == 0:
    ops.fix(pid, 1, 1)
    ops.fix(np+pid+1, 1, 1)
if pid == np-1:
    ops.timeSeries('Linear', 1)
    ops.pattern('Plain', 1, 1)
    ops.load(np + pid + 2, 0.0, -1.0)


ops.constraints('Transformation')
ops.numberer('ParallelPlain')
ops.system('Mumps')
ops.test('NormDispIncr', 1e-6, 6)
ops.algorithm('Newton')
ops.integrator('LoadControl', 1.0)
ops.analysis('Static')

ops.stop()
ops.start()
ops.analyze(1)

if pid == np-1:
    print('Node', pid+1, ops.nodeDisp(pid+1))


ops.stop()
