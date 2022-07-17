import os
import os.path
import openseespy.opensees as ops

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def test_RCFrameGravity():
    ops.wipe()
    exec(open('RCFrameGravity.py','r').read())

    u3 = ops.nodeDisp(3, 2)
    u4 = ops.nodeDisp(4, 2)

    assert abs(u3+0.0183736)<1e-6 and abs(u4+0.0183736)<1e-6
