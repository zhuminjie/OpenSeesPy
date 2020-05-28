FROM ubuntu:18.04 AS development

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get -y install make gcc g++ gfortran git tcl8.6 tcl8.6-dev libboost-all-dev python3.7 python3.7-dev libblas-dev python3-pip


WORKDIR /home

RUN git clone https://github.com/OpenSees/OpenSees.git openseespy
RUN git clone -b maint https://gitlab.com/petsc/petsc.git petsc
RUN mkdir /home/bin
RUN mkdir /home/lib


COPY Makefile.def /home/openseespy/

WORKDIR /home/petsc
RUN ./configure --download-cmake --download-mpich --download-fblaslapack --download-scalapack --download-mumps --download-metis --download-parmetis --with-shared-libraries=0 --with-debugging=0 COPTFLAGS='-O3 -march=native -mtune=native -fPIC' CXXOPTFLAGS='-O3 -march=native -mtune=native -fPIC' FOPTFLAGS='-O3 -march=native -mtune=native -fPIC'

WORKDIR /home/openseespy
RUN make -j

WORKDIR /home/openseespy/SRC/interpreter
RUN make -j

WORKDIR /home
RUN git clone https://github.com/OpenSeesPy-pip/openseespy-pip.git

WORKDIR /home/openseespy-pip
RUN python3.7 build_pip.py


#######################################################
# openseespy
FROM python:3.7-slim AS openseespy
RUN apt-get update -y
RUN apt-get -y install libquadmath0
RUN mkdir /app
WORKDIR /app
COPY --from=0 /home/openseespy-pip/dist/openseespy-3.1.5.12-py3-none-any.whl /app/
COPY --from=0 /home/petsc/arch-linux2-c-opt/bin/mpiexec* /app/
COPY --from=0 /home/petsc/arch-linux2-c-opt/bin/hydra_* /app/
RUN python3.7 -m pip install openseespy-3.1.5.12-py3-none-any.whl
RUN rm -f openseespy-3.1.5.12-py3-none-any.whl
WORKDIR /home
CMD python3.7
#######################################################

#######################################################
# openseespy
FROM openseespy AS openseespy-notebook
RUN python3.7 -m pip install notebook
WORKDIR /home
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