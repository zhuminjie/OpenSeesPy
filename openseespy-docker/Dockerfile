########################################################
## install centos packages
FROM centos:7 AS centos-packages

RUN yum update -y && \
    yum install -y make gcc-c++ gcc-gfortran git \
    tcl tcl-devel boost-devel mpich-3.2 mpich-3.2-devel \
    blas-devel openssl-devel bzip2-devel libffi-devel curl && \
    curl -O https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz && \
    tar -xzf Python-3.8.7.tgz && \
    cd Python-3.8.7 && \
    ./configure --enable-optimizations && \
    make altinstall
########################################################

########################################################
# configure petsc
FROM centos-packages AS centos-petsc
RUN cd /home && \
    git clone -b release \
    https://gitlab.com/petsc/petsc.git petsc && \
    cd /home/petsc && \
    /usr/local/bin/python3.8 configure \
    --with-mpi-dir=/usr/lib64/mpich-3.2 \
    --download-cmake --download-fblaslapack \
    --download-scalapack --download-mumps --download-metis \
    --download-parmetis --with-shared-libraries=0 \
    --with-debugging=0 \
    COPTFLAGS='-O3 -march=native -mtune=native -fPIC' \
    CXXOPTFLAGS='-O3 -march=native -mtune=native -fPIC' \
    FOPTFLAGS='-O3 -march=native -mtune=native -fPIC'
########################################################

########################################################
## compile openseespy
FROM centos-petsc AS centos-openseespy

WORKDIR /home
COPY opensees /home/opensees
COPY Makefile.def /home/opensees/

RUN mkdir /home/bin && \
    mkdir /home/lib

WORKDIR /home/opensees
RUN make python -j
########################################################

########################################################
## compile openseespy-pip
FROM centos-openseespy AS centos-pip

# Build openseespy package
WORKDIR /home
COPY openseespy-pip /home/openseespy-pip

# copy windows version
COPY opensees.pyd /home/bin/

# copy mac version
COPY opensees.so /home/bin/

WORKDIR /home/openseespy-pip
RUN python3.8 build_pip.py build \
    ../opensees/SRC/interpreter/opensees.so \
    /home/bin/opensees.pyd \
    /home/bin/opensees.so \
    copy_dep \
    python3.8 no_zip
########################################################

########################################################
## compile petsc
# FROM ubuntu:16.04 AS ubuntu-petsc

# ENV DEBIAN_FRONTEND=noninteractive
# RUN apt-get update -y && \
#     apt-get -y install software-properties-common && \
#     add-apt-repository ppa:deadsnakes/ppa && \
#     apt-get update -y && \
#     apt-get -y install make gcc-4.8 g++-4.8 gfortran-4.8 git \
#     tcl8.6 tcl8.6-dev libboost-all-dev libblas-dev \
#     python3.8 python3.8-dev && \
#     cd /home && \
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
RUN python3 build_pip.py test-test python3
#######################################################

#######################################################
# test centos
FROM centos:7  AS test-centos-7
RUN yum update -y
RUN yum -y install python3 python3-pip && \
    python3 -m pip install pytest

WORKDIR /home
COPY openseespy-pip /home/openseespy-pip

WORKDIR /home/openseespy-pip
RUN python3 build_pip.py test-test python3
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
RUN python3.8 build_pip.py test-test python3.8
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
RUN python3.8 build_pip.py test-test python3.8
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
RUN python3.8 build_pip.py test-test python3.8
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
COPY openseespy-pip /home/openseespy-pip

WORKDIR /home/openseespy-pip
RUN python3 build_pip.py test-test python3
#######################################################

#######################################################
# test fedora
FROM fedora  AS test-fedora
RUN yum update -y
RUN yum -y install python3 python3-pip && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install pytest

WORKDIR /home
COPY openseespy-pip /home/openseespy-pip

WORKDIR /home/openseespy-pip
RUN python3 build_pip.py test-test python3
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