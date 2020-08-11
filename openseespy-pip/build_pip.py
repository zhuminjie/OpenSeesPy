import subprocess
import shutil
import os
import os.path
import sys


def copy_library(so, pyd, pyd37):

    # change to script's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # replace new libraries
    linux = './openseespy/opensees/linux/'
    win = './openseespy/opensees/win/py38/'
    win37 = './openseespy/opensees/win/py37/'

    if os.path.exists(pyd):
        if os.path.exists(win+'opensees.pyd'):
            os.remove(win+'opensees.pyd')
        shutil.copy(pyd, win)

    if os.path.exists(pyd37):
        if os.path.exists(win37+'opensees.pyd'):
            os.remove(win37+'opensees.pyd')
        shutil.copy(pyd37, win37+'opensees.pyd')

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
    subprocess.run(['python', '-m', 'pip', 'install', '--upgrade',
                    'setuptools', 'wheel', 'twine', 'pytest'])

    # compile wheel
    subprocess.run(['python', 'setup.py', 'bdist_wheel'])


def upload_pip():
    # upload
    subprocess.run(['python', '-m', 'twine', 'upload', 'dist/*'])


def clean_pip():
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])


def upload_pip_test():
    # upload
    subprocess.run(['python', '-m', 'twine', 'upload',
                    '--repository', 'testpypi', 'dist/*'])


def install_pip_test():
    subprocess.run(['python', '-m', 'pip', 'uninstall', '-y', 'openseespy'])
    subprocess.run(['python', '-m', 'pip',  'install', '--pre', '--no-cache-dir', '--index-url',
                    'https://test.pypi.org/simple/', 'openseespy'])


def install_pip():
    subprocess.run(['python', '-m', 'pip', 'uninstall', '-y', 'openseespy'])
    subprocess.run(['python', '-m', 'pip', 'install',
                    '--pre', '--no-cache-dir', 'openseespy'])
