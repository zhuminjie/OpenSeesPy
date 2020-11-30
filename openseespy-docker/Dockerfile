FROM ubuntu:18.04 AS compile

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get -y install make gcc g++ gfortran git tcl8.6 tcl8.6-dev libboost-all-dev libblas-dev python3.8 python3.8-dev python3-pip


WORKDIR /home

RUN git clone https://github.com/OpenSees/OpenSees.git openseespy && \
    git clone -b release https://gitlab.com/petsc/petsc.git petsc && \
    mkdir /home/bin && \
    mkdir /home/lib

COPY Makefile.def /home/openseespy/

WORKDIR /home/petsc
RUN ./configure --download-cmake --download-mpich --download-fblaslapack --download-scalapack --download-mumps --download-metis --download-parmetis --with-shared-libraries=0 --with-debugging=0 COPTFLAGS='-O3 -march=native -mtune=native -fPIC' CXXOPTFLAGS='-O3 -march=native -mtune=native -fPIC' FOPTFLAGS='-O3 -march=native -mtune=native -fPIC'

WORKDIR /home/openseespy
RUN make -j python

## Build openseespy package
COPY openseespy-pip /home/openseespy-pip/

WORKDIR /home/openseespy-pip
RUN python3.8 build_pip.py build \
    ../openseespy/SRC/interpreter/opensees.so \
    copy_dep \
    python3.8


#######################################################
# openseespy
FROM ubuntu:18.04  AS openseespy
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get -y install python3.8 python3-pip
WORKDIR /home
COPY --from=0 /home/openseespy-pip/dist/openseespy-*.whl /home/
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
FROM openseespy AS openseespy-notebook
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