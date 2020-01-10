import os
import os.path
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('../openseespy/opensees/linux')

from opensees import *

exec(open('Truss.py','r').read())
exec(open('MomentCurvature.py','r').read())
exec(open('RCFramePushover.py','r').read())
exec(open('ElasticFrame.py','r').read())
exec(open('DynAnal_BeamWithQuadElements.py','r').read())
exec(open('Ex1a.Canti2D.EQ.modif.py','r').read())
exec(open('EigenAnal_twoStoreyShearFrame7.py','r').read())
exec(open('EigenAnal_twoStoreyFrame1.py','r').read())
exec(open('sdofTransient.py','r').read())
exec(open('PlanarTruss.py','r').read())
exec(open('PlanarTruss.Extra.py','r').read())
exec(open('PortalFrame2d.py','r').read())
exec(open('EigenFrame.py','r').read())
exec(open('EigenFrame.Extra.py','r').read())
exec(open('AISC25.py','r').read())
exec(open('PlanarShearWall.py','r').read())
exec(open('PinchedCylinder.py','r').read())


print("================================================================")
print("Done with testing examples.")
print("================================================================")