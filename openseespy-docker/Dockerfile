########################################################
## install centos packages
FROM centos:7 AS centos-packages
# 
RUN yum update -y && \
    yum install -y make gcc-c++ gcc-gfortran git \
    tcl tcl-devel boost-devel \
    blas-devel openssl-devel bzip2-devel libffi-devel curl wget && \
    cd /home && \
    curl -O https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz && \
    tar -xzf Python-3.8.7.tgz && \
    cd Python-3.8.7 && \
    ./configure --enable-optimizations && \
    make altinstall && \
    cd .. && \
    wget https://www.mpich.org/static/downloads/3.2/mpich-3.2.tar.gz && \
    tar -xf mpich-3.2.tar.gz && \
    mkdir /home/bin && \
    mkdir /home/lib && \
    mkdir /home/bin/mpich-install && \
    mkdir /home/lib/mpich-3.2 && \
    cd /home/lib/mpich-3.2 && \
    /home/mpich-3.2/configure \
    --prefix=/home/bin/mpich-install \
    --enable-fast=all \
    MPICHLIB_CFLAGS='-O3 -fPIC' \
    MPICHLIB_FFLAGS='-O3 -fPIC' \
    MPICHLIB_CXXFLAGS='-O3 -fPIC' \
    MPICHLIB_FCFLAGS='-O3 -fPIC' \
    --enable-shared=no && \
    make -j4 && \
    make install

########################################################

########################################################
# configure petsc
FROM centos-packages AS centos-petsc
RUN cd /home && \
    git clone -b release \
    https://gitlab.com/petsc/petsc.git petsc && \
    cd /home/petsc && \
    /usr/local/bin/python3.8 configure \
    --download-cmake \
    --with-mpi-dir=/home/bin/mpich-install --download-fblaslapack \
    --download-scalapack --download-mumps --download-metis \
    --download-parmetis --with-shared-libraries=0 \
    --with-debugging=0 \
    COPTFLAGS='-O3 -march=native -mtune=native -fPIC' \
    CXXOPTFLAGS='-O3 -march=native -mtune=native -fPIC' \
    FOPTFLAGS='-O3 -march=native -mtune=native -fPIC'
########################################################

########################################################
## get openseespy code
FROM centos-petsc AS centos-openseespy-code

WORKDIR /home
COPY opensees /home/opensees
COPY Makefile.def /home/opensees/

########################################################
## compile openseespy
FROM centos-openseespy-code AS centos-openseespy

WORKDIR /home/opensees
RUN make python -j4
########################################################

########################################################
## compile openseespy-pip
FROM centos-openseespy AS centos-pip

# Build openseespy package
WORKDIR /home
COPY openseespylinux-pip /home/openseespylinux-pip

WORKDIR /home/openseespylinux-pip
RUN python3.8 build_pip.py python3.8 build \
    ../opensees/SRC/interpreter/opensees.so \
    copy_dep \
    no_zip

ENTRYPOINT [ "python3.8", "build_pip.py", "python3.8"]
CMD [ "upload-test" ]
########################################################

########################################################
FROM centos-pip  AS centos-pip-bash

ENTRYPOINT [ "bash"]
########################################################

########################################################
## compile petsc        exit()

#     git clone -b release \
#     https://gitlab.com/petsc/petsc.git petsc && \
#     cd /home/petsc && \
#     ./configure --with-cc=gcc-4.8 --with-cxx=g++-4.8 --with-fc=gfortran-4.8 --download-cmake --download-mpich --download-fblaslapack --download-scalapack --download-mumps --download-metis --download-parmetis --with-shared-libraries=0 --with-debugging=0 COPTFLAGS='-O3 -march=native -mtune=native -fPIC' CXXOPTFLAGS='-O3 -march=native -mtune=native -fPIC' FOPTFLAGS='-O3 -march=native -mtune=native -fPIC'
########################################################


########################################################
## compile openseespy
# FROM ubuntu-petsc AS ubuntu-openseespy

# ENV DEBIAN_FRONTEND=noninteractive

# WORKDIR /home
# COPY opensees /home/opensees
# COPY Makefile.def /home/opensees/

# RUN mkdir /home/bin && \
#     mkdir /home/lib

# WORKDIR /home/opensees
# RUN make python -j
########################################################

########################################################
## compile openseespy-pip
# FROM ubuntu-openseespy AS ubuntu-pip

# # Build openseespy package
# WORKDIR /home
# COPY openseespy-pip /home/openseespy-pip
# RUN apt-get -y install apt-utils  python3.8-distutils curl && \
#     curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
#     python3.8 get-pip.py

# copy windows version
# COPY opensees.pyd /home/bin/

# copy mac version
# COPY opensees.so /home/bin/

# WORKDIR /home/openseespy-pip
# RUN python3.8 build_pip.py build \
#     ../opensees/SRC/interpreter/opensees.so \
#     /home/bin/opensees.pyd \
#     /home/bin/opensees.so \
#     copy_dep \
#     python3.8 no_zip
########################################################

#######################################################
# test centos
FROM centos:7.5.1804  AS test-centos-7.5.1804
RUN yum update -y && \
    yum -y install python3 python3-pip && \
    python3 -m pip install pytest

WORKDIR /home
COPY openseespy-pip /home/openseespy-pip

WORKDIR /home/openseespy-pip

ENTRYPOINT [ "python3", "build_pip.py", "python3"]
CMD [ "test-test" ]
#######################################################

#######################################################
# test centos
FROM centos:7  AS test-centos-7
RUN yum update -y
RUN yum -y install python3 python3-pip && \
    python3 -m pip install pytest

WORKDIR /home
ENV test=test
COPY openseespy-pip /home/openseespy-pip

WORKDIR /home/openseespy-pip

ENTRYPOINT [ "python3", "build_pip.py", "python3"]
CMD [ "test-test" ]
#######################################################

#######################################################
# test centos
FROM centos:8  AS test-centos-8
RUN yum update -y
RUN yum -y install python3.8 python3-pip && \
    python3.8 -m pip install pytest

WORKDIR /home
COPY openseespy-pip /home/openseespy-pip

WORKDIR /home/openseespy-pip

ENTRYPOINT [ "python3.8", "build_pip.py", "python3.8"]
CMD [ "test-test" ]
#######################################################

#######################################################
# test ubuntu
FROM ubuntu:16.04  AS test-ubuntu-16.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get -y install python3.5 python3-pip

WORKDIR /home
COPY openseespy-pip /home/openseespy-pip

WORKDIR /home/openseespy-pip

ENTRYPOINT [ "bash"]
# CMD [ "python3.5", "build_pip.py", "python3.5"]
#######################################################

#######################################################
# test ubuntu
FROM ubuntu:18.04  AS test-ubuntu-18.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get -y install python3.8 python3-pip && \
    python3.8 -m pip install --upgrade pip && \
    python3.8 -m pip install pytest

WORKDIR /home
COPY openseespy-pip /home/openseespy-pip

WORKDIR /home/openseespy-pip

ENTRYPOINT [ "python3.8", "build_pip.py", "python3.8"]
CMD [ "test-test" ]
#######################################################

#######################################################
# test ubuntu
FROM ubuntu:20.04  AS test-ubuntu-20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get -y install python3.8 python3-pip && \
    python3.8 -m pip install --upgrade pip && \
    python3.8 -m pip install pytest

WORKDIR /home
COPY openseespy-pip /home/openseespy-pip

WORKDIR /home/openseespy-pip

ENTRYPOINT [ "python3.8", "build_pip.py", "python3.8"]
CMD [ "test-test" ]
#######################################################

#######################################################
# test debian
FROM debian  AS test-debian
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get -y install python3 python3-pip && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install pytest

WORKDIR /home
ENV test=test
COPY openseespy-pip /home/openseespy-pip

WORKDIR /home/openseespy-pip

ENTRYPOINT [ "python3", "build_pip.py", "python3"]
CMD [ "test-test" ]
#######################################################

#######################################################
# test fedora
FROM fedora  AS test-fedora
RUN yum update -y
RUN yum -y install python3 python3-pip && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install pytest

WORKDIR /home
ENV test=test
COPY openseespy-pip /home/openseespy-pip

WORKDIR /home/openseespy-pip

ENTRYPOINT [ "python3", "build_pip.py", "python3"]
CMD [ "test-test" ]
#######################################################

#######################################################
# install openseespy
FROM ubuntu:18.04  AS ubuntu-install
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get -y install python3.8 python3-pip
WORKDIR /home
COPY --from=2 /home/openseespy-pip/dist/openseespy-*.whl /home/
COPY --from=0 /home/petsc/arch-linux-c-opt/bin/mpiexec* /usr/local/bin/
COPY --from=0 /home/petsc/arch-linux-c-opt/bin/hydra_* /usr/local/bin/
COPY hello.py /home/
RUN python3.8 -m pip install openseespy-*.whl
RUN rm -f openseespy-*.whl
WORKDIR /
CMD python3.8
#######################################################

#######################################################
# openseespy
FROM ubuntu-install AS ubuntu-notebook
RUN python3.8 -m pip install notebook
WORKDIR /
CMD jupyter notebook --ip=0.0.0.0 --no-browser --allow-root
#######################################################


# #######################################################
# # opensees tcl serial
# FROM ubuntu:18.04 AS opensees-serial
# RUN apt-get update -y
# RUN apt-get -y install libgfortran4 libgomp1 libblas3 libtcl8.6
# RUN mkdir /app
# WORKDIR /app
# COPY --from=0 /home/bin/openseesmp /app/openseesmp
# COPY --from=0 /home/petsc/arch-linux2-c-opt/bin/mpiexec* /app/
# COPY --from=0 /home/petsc/arch-linux2-c-opt/bin/hydra_* /app/
# WORKDIR /home
# CMD /app/openseesmp
# #######################################################

# #######################################################
# # opensees tcl parallel
# FROM ubuntu:18.04 AS opensees-parallel
# RUN apt-get update -y
# RUN apt-get -y install libgfortran4 libgomp1 libblas3 libtcl8.6
# RUN mkdir /app
# WORKDIR /app
# ENV np=1
# ENV script=hello.tcl
# COPY --from=0 /home/bin/openseesmp /app/openseesmp
# COPY --from=0 /home/petsc/arch-linux2-c-opt/bin/mpiexec* /app/
# COPY --from=0 /home/petsc/arch-linux2-c-opt/bin/hydra_* /app/
# COPY ${script} /home
# WORKDIR /home
# CMD /app/mpiexec -np $np /app/openseesmp $script
# #######################################################