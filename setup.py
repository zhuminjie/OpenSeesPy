import setuptools

about = {}
with open('openseespy/__about__.py') as fp:
    exec(fp.read(), about)

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openseespy",
    version=about['__version__'],
    author="Minjie Zhu",
    author_email="zhum@oregonstate.edu",
    description="A OpenSeesPy package",
    long_description=long_description,
    url="https://github.com/openseespy/openseespy",
    packages=setuptools.find_packages(),
    package_data={
        'openseespy': ['opensees.so','opensees.pyd','LICENSE.rst'],
    },
    license = 'LICENSE.rst',
    classifiers=[
        "Programming Language :: Python :: 3",
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows'
    ],
    python_requires='>=3.6',
    py_modules=['opensees'],
    zip_safe=False
)
