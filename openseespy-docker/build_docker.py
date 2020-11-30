import subprocess
import shutil
import os
import os.path
import sys


def build_docker(dry_run=True, push=False):

    # change to script's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # openseespy-pip
    if os.path.exists('openseespy-pip'):
        print('removing openseespy-pip')
        shutil.rmtree('openseespy-pip')

    shutil.copytree('../openseespy-pip', 'openseespy-pip')

    # version
    about = {}
    with open('openseespy-pip/openseespy/version.py') as fp:
        exec(fp.read(), about)
    version = about['version']

    # tag
    tag_compile = f'compile:{version}'
    tag_openseespy = f'zhuminjie/openseespy:{version}'
    tag_notebook = f'zhuminjie/openseespy:{version}-notebook'
    if not dry_run:
        subprocess.run(['docker',
                        'build', '--target', 'compile',
                        '-t', tag_compile, '.'])
        subprocess.run(['docker',
                        'build', '--target', 'openseespy',
                        '-t', tag_openseespy, '.'])
        subprocess.run(['docker',
                        'build', '--target',
                        'openseespy_notebook',
                        '-t', tag_notebook, '.'])

        if push:
            subprocess.run(['docker', 'login'])
            subprocess.run(['docker', 'image',
                            'push', tag_openseespy])
            subprocess.run(['docker', 'image',
                            'push', tag_notebook])
    else:
        print(f'docker build --target compile -t {tag_compile} .')
        print(f'docker build --target openseespy -t {tag_openseespy} .')
        print(f'docker build --target openseespy_notebook -t {tag_notebook} .')

        if push:
            print(f'docker login')
            print(f'docker image push {tag_openseespy}')
            print(f'docker image push {tag_notebook'})


if __name__ == "__main__":
    dry_run = False
    push = False
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == '-dry-run':
            dry_run = True
        elif sys.argv[i] == '-push':
            push = True
    build_docker(dry_run, push)
