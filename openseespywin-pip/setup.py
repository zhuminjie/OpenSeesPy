import setuptools

about = {}
with open('openseespywin/version.py') as fp:
    exec(fp.read(), about)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openseespywin",
    version=about['version'],
    author="Minjie Zhu",
    author_email="zhum@oregonstate.edu",
    description="A OpenSeesPy Windows package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openseespy/openseespy",
    packages=setuptools.find_packages(),
    package_data={
        '': [
            'opensees.pyd',
            'LICENSE.md',
            '*.dat',
            '*.at2',],
    },
    license='LICENSE.md',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        'Operating System :: Microsoft :: Windows'],
    platforms=["Windows"],
    python_requires='=3.9',
    zip_safe=False)
