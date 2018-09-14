import setuptools

about = {}
with open('__about__.py') as fp:
    exec(fp.read(), about)

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OpenSeesPy",
    version=about['__version__'],
    author="Minjie Zhu",
    author_email="zhum@oregonstate.edu",
    description="A OpenSeesPy package",
    long_description=long_description,
    url="https://github.com/OpenSeesPy/OpenSeesPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows'
    ],
    python_requires='>=3.6',
)
