import setuptools

about = {}
with open('openseespy/version.py') as fp:
    exec(fp.read(), about)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openseespy",
    version=about['version'],
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
        'openseespywin>=3.3.0.1; platform_system=="Windows"',
        'openseespylinux>=3.3.0.1; platform_system=="Linux"',
        'openseespymac>=3.3.0.1; platform_system=="Darwin"',
    ],
    python_requires='>=3.6',
    zip_safe=False)
