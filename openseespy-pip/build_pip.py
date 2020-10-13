import subprocess
import shutil
import os
import os.path
import sys
import glob


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


def copy_mac_library(so):

    mac = './openseespy/opensees/mac/'
    if os.path.exists(so):
        if os.path.exists(mac+'opensees.so'):
            os.remove(mac+'opensees.so')
        for f in glob.glob(mac+'lib/*.dylib'):
            os.remove(f)

        shutil.copy(so, mac)

        # get dependent library for linux
        p = subprocess.run(
            ["otool", "-L", so], capture_output=True)

        for line in p.stdout.decode('utf-8').split('\n'):
            i = line.find('/')
            j = line.find(' ', i)
            if i < 0 or j < 0 or i >= j:
                continue

            print('copying '+line[i:j]+' to '+mac+'lib/')
            shutil.copy(line[i:j], mac+'lib/')
            lib_name = line[i:j].split('/')
            lib_name = lib_name[-1]
            print('changing rpath from '+line[i:j]+' to lib/'+lib_name)
            subprocess.run(
                ['install_name_tool', '-change', line[i:j],
                    'lib/'+lib_name, mac+'opensees.so']
            )

        if os.path.exists(mac+'lib/Python'):
            os.remove(mac+'lib/Python')


def build_pip():

    print('==============================================================')
    print('Did you remember to update version number in opensees source?')
    print('\n\n\n\n\n')
    print('==============================================================')

    # clean folders
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])

    # update tools
    subprocess.run(['python3', '-m', 'pip', 'install', '--upgrade',
                    'setuptools', 'wheel', 'twine', 'pytest'])

    # compile wheel
    subprocess.run(['python3', 'setup.py', 'bdist_wheel'])


def upload_pip():
    # upload
    subprocess.run(['python3', '-m', 'twine', 'upload', 'dist/*'])


def clean_pip():
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])


def upload_pip_test():
    # upload
    subprocess.run(['python3', '-m', 'twine', 'upload',
                    '--repository', 'testpypi', 'dist/*'])


def install_pip_test():
    subprocess.run(['python3', '-m', 'pip', 'uninstall', '-y', 'openseespy'])
    subprocess.run(['python3', '-m', 'pip',  'install', '--pre', '--no-cache-dir', '--index-url',
                    'https://test.pypi.org/simple/', 'openseespy'])


def install_pip():
    subprocess.run(['python3', '-m', 'pip', 'uninstall', '-y', 'openseespy'])
    subprocess.run(['python3', '-m', 'pip', 'install',
                    '--pre', '--no-cache-dir', 'openseespy'])
