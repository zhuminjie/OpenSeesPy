import setuptools

about = {}
with open('openseespy/version.py') as fp:
    exec(fp.read(), about)

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openseespy",
    version=about['version'],
    author="Minjie Zhu",
    author_email="zhum@oregonstate.edu",
    description="A OpenSeesPy package",
    long_description=long_description,
    url="https://github.com/openseespy/openseespy",
    packages=setuptools.find_packages(),
    package_data={
        '': ['opensees.so','opensees.pyd','LICENSE.rst','*.so','*.dll','*.so.*'],
    },
    license = 'LICENSE.rst',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows'
    ],
    platforms = ["Linux",'Windows'],
    python_requires='>=3.6',
    zip_safe=False
)
