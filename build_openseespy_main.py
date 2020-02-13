import subprocess
import shutil
import os
import os.path
import sys

# user-set directories
openseessrc = '/data2/Minjie/projects/openseespy'
binary = openseessrc + '/SRC/interpreter/openseespy'
pythoninstall = '/scratch/bin/openseespy'
pythonsrc = '/scratch/bin/Python-3.7.6'
pypidir = '/data2/Minjie/projects/openseespypip'

if os.path.exists(binary):
    os.remove(binary)

# compile python
setup = True
if not os.path.exists(pythoninstall):
    setup = False
    os.chdir(pythonsrc)
    # compile
    if not os.path.exists(pythonsrc+'/libpython3.7m.so'):
        os.environ['LDFLAGS'] = '-Wl,--rpath=../lib'
        os.environ['CXX'] = '/usr/bin/g++'
        subprocess.run(['./configure', '--prefix='+pythoninstall, '--enable-shared',
                        '--with-ensurepip=yes', '--with-system-expat', '--with-system-ffi', '--enable-optimizations'])
        subprocess.run(['make', '-j12'])

    # install
    subprocess.run(['make', 'install'])

# compile openseespy binary
os.chdir(openseessrc)
subprocess.run(['make', 'pythonmain'])

# copy to python install
shutil.copy(binary, pythoninstall+'/bin')

# setup openseespy binary
if not setup:
    os.chdir(pythoninstall+'/bin')
    for program in ['2to3-3.7', 'easy_install-3.7', 'idle3.7', 'pip3', 'pip3.7', 'pydoc3.7', 'pyvenv-3.7']:
        print('Setting up', program)
        with open('./'+program, 'r') as f:
            data = f.read()
        with open('./'+program, 'w') as f:
            f.write(data.replace('python3.7', 'openseespy'))
    for program in ['python3', 'python3.7', 'python3.7m']:
        os.remove('./'+program)

    # install packages
    subprocess.run(['./openseespy', '-m', 'pip', 'install', 'notebook'])
    subprocess.run(['./openseespy', '-m', 'pip', 'install', 'numpy'])
    subprocess.run(['./openseespy', '-m', 'pip', 'install', 'matplotlib'])

    # install openseespy
    os.mkdir(pythoninstall+'/lib/python3.7/site-packages/openseespy')
    os.chdir(pythoninstall+'/lib/python3.7/site-packages/openseespy')
    shutil.copy(pypidir+'/openseespy/version.py', '.')
    shutil.copy(pypidir+'/openseespy/__init__.py', '.')
    os.mkdir('opensees')
    os.chdir('opensees')
    with open('__init__.py', 'w') as f:
        f.write('from opensees import *')
    os.chdir('..')
    os.mkdir('postprocessing')
    os.chdir('postprocessing')
    shutil.copy(pypidir+'/openseespy/postprocessing/Get_Rendering.py', '.')
    shutil.copy(pypidir+'/openseespy/postprocessing/__init__.py', '.')

# get all libraries
os.chdir(pythoninstall+'/bin')
p = subprocess.run(["ldd", binary], capture_output=True)

for line in p.stdout.decode('utf-8').split('\n'):
    i = line.find('/')
    j = line.find(' ', i)
    if i < 0 or j < 0 or i >= j:
        continue
    if line.find('libpython') >= 0:
        continue

    print('copying '+line[i:j]+' ....')
    shutil.copy(line[i:j], pythoninstall+'/lib')
