import setuptools

about = {}
with open('openseespy/version.py') as fp:
  exec(fp.read(), about)

with open("README.md", "r") as fh:
  long_description = fh.read()

version = about['version']

setuptools.setup(
    name="openseespy",
    version=version,
    author="Minjie Zhu",
    author_email="zhum@oregonstate.edu",
    description="A OpenSeesPy package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openseespy/openseespy",
    packages=setuptools.find_packages(),
    package_data={
        '': ['LICENSE.md',
             '*.dat',
             '*.at2', ],
    },
    license='LICENSE.md',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        "Operating System :: MacOS :: MacOS X"],
    platforms=[
        "Linux",
        'Windows',
        'Mac'],
    install_requires=[
        f'openseespywin>={version}; platform_system=="Windows"',
        f'openseespylinux>={version}; platform_system=="Linux"',
        f'openseespymac>={version}; platform_system=="Darwin"',
    ],
    python_requires='=3.8',
    zip_safe=False)
