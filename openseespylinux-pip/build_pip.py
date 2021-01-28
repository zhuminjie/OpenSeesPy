import subprocess
import shutil
import os
import os.path
import sys
import glob


def copy_linux_library(so, copy_dep=True):

    # change to script's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # replace new libraries
    linux = './openseespylinux/'

    if os.path.exists(so):
        if os.path.exists(linux+'opensees.so'):
            os.remove(linux+'opensees.so')
        shutil.copy(so, linux)

        if copy_dep:
            # get dependent library for linux
            p = subprocess.run(
                ["ldd", so], capture_output=True)

            for line in p.stdout.decode('utf-8').split('\n'):
                i = line.find('/')
                j = line.find(' ', i)
                if i < 0 or j < 0 or i >= j:
                    continue

                find = False
                if line[i:j].find('gfortran') >= 0:
                    find = True
                elif line[i:j].find('blas') >= 0:
                    find = True
                elif line[i:j].find('stdc++') >= 0:
                    find = True
                elif line[i:j].find('gcc') >= 0:
                    find = True
                elif line[i:j].find('quadmath') >= 0:
                    find = True
                elif line[i:j].find('gomp') >= 0:
                    find = True
                elif line[i:j].find('mpi') >= 0:
                    find = True

                if find:
                    print('copying '+line[i:j]+' to '+linux+'lib/')
                    shutil.copy(line[i:j], linux+'lib/')

def build_pip(pyexe='python', use_zip=False):

    # clean folders
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespylinux.egg-info'])

    # update tools
    subprocess.run([pyexe, '-m', 'pip', 'install', '--upgrade',
                    'setuptools', 'wheel', 'twine', 'pytest'])

    # compile wheel
    if use_zip:
        subprocess.run([pyexe, 'setup.py', 'bdist', '--format=zip'])
    else:
        subprocess.run([pyexe, 'setup.py', 'bdist_wheel'])


def upload_pip(pyexe='python'):
    # upload
    subprocess.run([pyexe, '-m', 'twine', 'upload', 'dist/*'])


def clean_pip():
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespylinux.egg-info'])


def upload_pip_test(pyexe='python'):
    # upload
    subprocess.run([pyexe, '-m', 'twine', 'upload',
                    '--repository', 'testpypi', 'dist/*'])


def install_pip_test(pyexe='python'):
    subprocess.run([pyexe, '-m', 'pip', 'uninstall', '-y', 'openseespylinux'])
    subprocess.run([pyexe, '-m', 'pip',  'install', '--pre', '--no-cache-dir', '--index-url',
                    'https://test.pypi.org/simple/', 'openseespylinux'])


def install_pip(pyexe='python'):
    subprocess.run([pyexe, '-m', 'pip', 'uninstall', '-y', 'openseespylinux'])
    subprocess.run([pyexe, '-m', 'pip', 'install',
                    '--pre', '--no-cache-dir', 'openseespylinux'])

# commands:
#
# pyexe - python excutable
#
# build pip
# build_pip pyexe build so copy_dep/no_copy use_zip/no_zip
# so - path to opensees.so
# copy_dep - copy dependencies of opensees.os to lib/
# no_copy - do not copy dependencies of opensees.os to lib/
# use_zip - build the package to a zip file
# no_zip - build the package to a wheel file
# 
# upload to testpypi
# build_pip pyexe upload-test
# 
# upload to pypi
# build_pip pyexe upload
# 
# test package from testpypi
# build_pip pyexe test-test
# 
# test package from pypi
# build_pip pyexe test
#
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('build_pip pyexe cmd')
        exit()

    pyexe = sys.argv[1]

    if sys.argv[2] == 'build':
        if len(sys.argv) < 6:
            print('buld_pip pyexe build so copy_dep/no_copy use_zip/no_zip')
            exit()

        so = sys.argv[3]
        copy_dep = False
        if sys.argv[4] == 'copy_dep':
            copy_dep = True
        use_zip = False
        if sys.argv[5] == 'use_zip':
            use_zip = True

        copy_linux_library(so, copy_dep=copy_dep)
        build_pip(pyexe, use_zip=use_zip)

    elif sys.argv[2] == 'upload-test':

        if len(sys.argv) < 3:
            print('buld_pip pyexe upload-test')
            exit()
        upload_pip_test(pyexe)

    elif sys.argv[2] == 'upload':

        if len(sys.argv) < 3:
            print('buld_pip pyexe upload')
            exit()

        upload_pip(pyexe)

    elif sys.argv[2] == 'test-test':

        if len(sys.argv) < 3:
            print('buld_pip pyexe test-test')
            exit()

        install_pip_test(pyexe)
        subprocess.run(['pytest', '--pyargs', 'openseespylinux.test'])

    elif sys.argv[2] == 'test':

        if len(sys.argv) < 3:
            print('buld_pip pyexe test')
            exit()

        install_pip(pyexe)
        subprocess.run(['pytest', '--pyargs', 'openseespylinux.test'])
