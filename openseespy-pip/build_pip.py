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
    linux = './openseespy/opensees/linux/'

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
                if line[i:j].find('gfortran') < 0:
                    continue
                if line[i:j].find('blas') < 0:
                    continue;

                print('copying '+line[i:j]+' to '+linux+'lib/')
                shutil.copy(line[i:j], linux+'lib/')

def copy_win_library(pyd):
    win = './openseespy/opensees/win/'
    if os.path.exists(pyd):
        if os.path.exists(win+'opensees.pyd'):
            os.remove(win+'opensees.pyd')
        shutil.copy(pyd, win)

def copy_mac_library(so):

    mac = './openseespy/opensees/mac/'
    if os.path.exists(so):
        if os.path.exists(mac+'opensees.so'):
            os.remove(mac+'opensees.so')
        # for f in glob.glob(mac+'lib/*.dylib'):
        #     os.remove(f)

        shutil.copy(so, mac)

        # get dependent library for linux
        # p = subprocess.run(
        #     ["otool", "-L", so], capture_output=True)

        # for line in p.stdout.decode('utf-8').split('\n'):
        #     i = line.find('/')
        #     j = line.find(' ', i)
        #     if i < 0 or j < 0 or i >= j:
        #         continue

        #     print('copying '+line[i:j]+' to '+mac+'lib/')
        #     shutil.copy(line[i:j], mac+'lib/')
        #     lib_name = line[i:j].split('/')
        #     lib_name = lib_name[-1]
        #     if lib_name == 'Python':
        #         continue
        #     print('changing rpath from '+line[i:j]+' to lib/'+lib_name)
        #     subprocess.run(
        #         ['install_name_tool', '-change', line[i:j],
        #             '@loader_path/lib/'+lib_name, mac+'opensees.so']
        #     )

        # if os.path.exists(mac+'lib/Python'):
        #     os.remove(mac+'lib/Python')


def build_pip(pyexe='python', use_zip=False):

    # clean folders
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])

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
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])


def upload_pip_test(pyexe='python'):
    # upload
    subprocess.run([pyexe, '-m', 'twine', 'upload',
                    '--repository', 'testpypi', 'dist/*'])


def install_pip_test(pyexe='python'):
    subprocess.run([pyexe, '-m', 'pip', 'uninstall', '-y', 'openseespy'])
    subprocess.run([pyexe, '-m', 'pip',  'install', '--pre', '--no-cache-dir', '--index-url',
                    'https://test.pypi.org/simple/', 'openseespy'])


def install_pip(pyexe='python'):
    subprocess.run([pyexe, '-m', 'pip', 'uninstall', '-y', 'openseespy'])
    subprocess.run([pyexe, '-m', 'pip', 'install',
                    '--pre', '--no-cache-dir', 'openseespy'])


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('build_pip upload-test/build')
        exit()

    if sys.argv[1] == 'build':
        if len(sys.argv) < 8:
            print('buld_pip build so pyd macso copy_dep/no_copy pyexe use_zip/no_zip')
            exit()

        so = sys.argv[2]
        pyd = sys.argv[3]
        macso = sys.argv[4]
        copy_dep = False
        if sys.argv[5] == 'copy_dep':
            copy_dep = True
        pyexe = sys.argv[6]
        use_zip = False
        if sys.argv[7] == 'use_zip':
            use_zip = True

        copy_linux_library(so, copy_dep=copy_dep)
        copy_win_library(pyd)
        copy_mac_library(macso)
        build_pip(pyexe, use_zip=use_zip)

    elif sys.argv[1] == 'upload-test':

        if len(sys.argv) < 3:
            print('buld_pip upload-test pyexe')
            exit()

        pyexe = sys.argv[2]
        upload_pip_test(pyexe)

    elif sys.argv[1] == 'upload':

        if len(sys.argv) < 3:
            print('buld_pip upload pyexe')
            exit()

        pyexe = sys.argv[2]
        upload_pip(pyexe)

    elif sys.argv[1] == 'test-test':

        if len(sys.argv) < 3:
            print('buld_pip upload pyexe')
            exit()

        pyexe = sys.argv[2]
        install_pip_test(pyexe)
        subprocess.run(['pytest', '--pyargs', 'openseespy.test'])

    elif sys.argv[1] == 'test':

        if len(sys.argv) < 3:
            print('buld_pip upload pyexe')
            exit()

        pyexe = sys.argv[2]
        install_pip(pyexe)
        subprocess.run(['pytest', '--pyargs', 'openseespy.test'])