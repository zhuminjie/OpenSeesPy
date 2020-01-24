import subprocess
import shutil
import os
import os.path
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# replace new libraries
linux = './openseespy/opensees/linux/'
win = './openseespy/opensees/win/'
so = '../openseespy/SRC/interpreter/opensees.so'
pyd = '../openseespy/Win64/bin/opensees.pyd'

if os.path.exists(linux+'opensees.so'):
    os.remove(linux+'opensees.so')
if os.path.exists(win+'opensees.pyd'):
    os.remove(win+'opensees.pyd')

shutil.copy(so, linux)
if os.path.exists(pyd):
    shutil.copy(pyd, win)

# get fortran library
p = subprocess.run(
    ["ldd", so], capture_output=True)

for line in p.stdout.decode('utf-8').split('\n'):
    i = line.find('/')
    j = line.find(' ', i)
    if i < 0 or j < 0 or i >= j:
        continue

    if line[i:j].find('fortran') > 0 or line[i:j].find('blas') > 0:
        print('copying '+line[i:j]+' ....')
        shutil.copy(line[i:j], linux+'lib/')

# clean folders
subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])

# update tools
subprocess.run(['python3.7', '-m', 'pip', 'install', '--upgrade', 'setuptools', 'wheel', 'twine'])

# compile wheel
subprocess.run(['python3.7', 'setup.py', 'bdist_wheel'])

# test
sys.path.append('openseespy/opensees/linux')

from opensees import *

os.chdir('tests')
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
os.chdir('..')


print("================================================================")
print("Done with testing examples.")
print("================================================================")

# upload
if os.path.exists(pyd):
    subprocess.run(['python3.7', '-m', 'twine', 'upload', 'dist/*'])
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])

