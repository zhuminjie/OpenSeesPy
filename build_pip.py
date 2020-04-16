import subprocess
import shutil
import os
import os.path
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def copy_library(so, pyd):

    # change to script's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # replace new libraries
    linux = './openseespy/opensees/linux/'
    win = './openseespy/opensees/win/'

    if os.path.exists(pyd):
        if os.path.exists(win+'opensees.pyd'):
            os.remove(win+'opensees.pyd')
        shutil.copy(pyd, win)

    if os.path.exists(so):
        if os.path.exists(linux+'opensees.so'):
            os.remove(linux+'opensees.so')
        shutil.copy(so, linux)

        # get dependent library for linux
        p = subprocess.run(
            ["ldd", so], capture_output=True)

        for line in p.stdout.decode('utf-8').split('\n'):
            i = line.find('/')
            j = line.find(' ', i)
            if i < 0 or j < 0 or i >= j:
                continue

            print('copying '+line[i:j]+' to '+linux+'lib/')
            shutil.copy(line[i:j], linux+'lib/')


def build_pip():

    # clean folders
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])

    # update tools
    subprocess.run(['python3.7', '-m', 'pip', 'install', '--upgrade',
                    'setuptools', 'wheel', 'twine'])

    # compile wheel
    subprocess.run(['python3.7', 'setup.py', 'bdist_wheel'])

def upload_pip():
    # upload
    subprocess.run(['python3.7', '-m', 'twine', 'upload', 'dist/*'])
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])
