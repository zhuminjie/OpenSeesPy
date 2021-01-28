import setuptools

about = {}
with open('openseespylinux/version.py') as fp:
    exec(fp.read(), about)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openseespylinux",
    version=about['version'],
    author="Minjie Zhu",
    author_email="zhum@oregonstate.edu",
    description="A OpenSeesPy Linux package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openseespy/openseespy",
    packages=setuptools.find_packages(),
    package_data={
        '': [
            'opensees.so',
            'LICENSE.md',
            '*.so',
            '*.dat',
            '*.at2',
            '*.so.*'],
    },
    license='LICENSE.md',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        'Operating System :: POSIX :: Linux'],
    platforms=["Linux"],
    python_requires='>=3.6',
    zip_safe=False)
