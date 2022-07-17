import openseespy.opensees as ops

pid = ops.getPID()
np = ops.getNP()
ops.start()
if np != 2:
    exit()

ops.model('basic', '-ndm', 2, '-ndf', 2)
ops.uniaxialMaterial('Elastic', 1, 3000.0)

if pid == 0:
    ops.node(1, 0.0, 0.0)
    ops.node(4, 72.0, 96.0)

    ops.fix(1, 1, 1)

    ops.element('Truss', 1, 1, 4, 10.0, 1)
    ops.timeSeries('Linear', 1)
    ops.pattern('Plain', 1, 1)
    ops.load(4, 100.0, -50.0)

else:
    ops.node(2, 144.0, 0.0)
    ops.node(3, 168.0, 0.0)
    ops.node(4, 72.0, 96.0)

    ops.fix(2, 1, 1)
    ops.fix(3, 1, 1)

    ops.element('Truss', 2, 2, 4, 5.0, 1)
    ops.element('Truss', 3, 3, 4, 5.0, 1)

ops.constraints('Transformation')
ops.numberer('ParallelPlain')
ops.system('Mumps')
ops.test('NormDispIncr', 1e-6, 6, 2)
ops.algorithm('Newton')
ops.integrator('LoadControl', 0.1)
ops.analysis('Static')

ops.analyze(10)

print('Node 4: ', [ops.nodeCoord(4), ops.nodeDisp(4)])

ops.loadConst('-time', 0.0)

if pid == 0:
    ops.pattern('Plain', 2, 1)
    ops.load(4, 1.0, 0.0)

ops.domainChange()
ops.integrator('ParallelDisplacementControl', 4, 1, 0.1)
ops.analyze(10)

print('Node 4: ', [ops.nodeCoord(4), ops.nodeDisp(4)])
ops.stop()