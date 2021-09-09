"""
The source code is developed by Marin Grubišić https://github.com/mgrubisic from University of Osijek, Croatia.
The numerical model with the associated analysis was described in detail by Prof. Michael Scott within OpenSees Days 2011 https://opensees.berkeley.edu/OpenSees/workshops/OpenSeesDays2011/B5_MHS.pdf.
Run the source code in your favorite Python program and should see following plot.
"""

import time
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import openseespy.opensees as ops
import openseespy.preprocessing.DiscretizeMember as dm

print(f"\nOpenSees " + ops.version() + " | Python " + sys.version)

# +---------------------------------------------+
# |                   Units                     |
# +---------------------------------------------+

m, kN, sec = 1.0, 1.0, 1.0  # meter for length, kilonewton for force, second for time

# Angle
rad = 1.0
deg = np.pi/180.0*rad

# Length, Area, Volume, Second moment of area
m2, m3, m4 = m**2, m**3, m**4
cm, cm2, cm3, cm4 = m*1E-2, m*1E-4, m*1E-6, m*1E-8
mm, mm2, mm3, mm4 = m*1E-3, m*1E-6, m*1E-9, m*1E-12
inch = 0.0254*m
ft = 0.3048*m

# Force
N = kN*1E-3
g = 9.80665*m/(sec**2)

# Mass
kg = N*sec**2/m
ton = kg*1E3
lbs = 0.45359237*kg
kip = 453.59237*kg

# Pressure
Pa, kPa, MPa, GPa = N/m**2, 1E3*N/m**2, 1E6*N/m**2, 1E9*N/m**2
pcf = lbs/(ft**3)
ksi = kip/(inch**2)
psi = ksi/1E3

Inf = 1.0E10  # a really large number
Null = 1/Inf  # a really small number

LunitTXT = "m"  # (Length) define basic-unit text for output
FunitTXT = "kN"  # (Force) define basic-unit text for output
TunitTXT = "sec"  # (Time) define basic-unit text for output

# Units Check
# print(f"K/M: {1.0*N/m/kg}")


# +---------------------------------------------+
# |           Define some functions             |
# +---------------------------------------------+


def run_sensitivity_analysis(ctrlNode, dof, baseNode, SensParam, steps=500, IOflag=False):
    """
    Run load-control sensitivity analysis
    """
    ops.wipeAnalysis()
    start_time = time.time()

    print("\n==> ... Running Load-Control Sensitivity Analysis ...\n")

    ops.system("BandGeneral")
    ops.numberer("RCM")
    ops.constraints("Transformation")
    ops.test("NormDispIncr", 1.0E-12, 10, 3)
    ops.algorithm("Newton")  # KrylovNewton
    ops.integrator("LoadControl", 1/steps)
    ops.analysis("Static")
    ops.sensitivityAlgorithm("-computeAtEachStep")

    outputs = {
        "time": [],
        "disp": [],
        "force": []
    }

    for sens in SensParam:
        outputs[f"sensDisp_{sens}"] = []

    for i in range(steps):
        ops.reactions()
        if IOflag:
            print(
                f"Single Cycle Response: Step #{i}, Node #{ctrlNode}: {ops.nodeDisp(ctrlNode, dof):.3f} {LunitTXT} / {-ops.nodeReaction(baseNode, dof):.2f} {FunitTXT}.")
        ops.analyze(1)
        tCurrent = ops.getTime()

        outputs["time"].append(tCurrent)
        outputs["disp"].append(ops.nodeDisp(ctrlNode, dof))
        outputs["force"].append(-ops.nodeReaction(baseNode, dof))

        for sens in SensParam:
            # sensDisp(patternTag, paramTag)
            outputs[f"sensDisp_{sens}"].append(
                ops.sensNodeDisp(ctrlNode, dof, sens))

    print("==> Sensitvity Analysis Completed!\n")
    print(
        f"Analysis elapsed time is {(time.time() - start_time):.3f} seconds.\n")

    return outputs


# +---------------------------------------------+
# |               Define model                  |
# +---------------------------------------------+

# Create ModelBuilder
# -------------------
ops.wipe()
ops.model("basic", "-ndm", 2, "-ndf", 3)

# Create nodes
# ------------
L = 5*m
ops.node(1, 0.0, 0.0)  # Fixed end
ops.node(2, L, 0.0)  # Free end


# Fixed support
# -------------
ops.fix(1, 1, 1, 1)

# Define material
# ---------------
matTag = 1
Fy = 410*MPa  # Yield stress
Es = 200*GPa  # Modulus of Elasticity of Steel
b = 2/100     # 2% Strain hardening ratio
Hkin = b/(1-b)*Es

# Sensitivity-ready steel materials: Hardening, Steel01, SteelMP, BoucWen, SteelBRB, StainlessECThermal, SteelECThermal, ...
# Hardening Sensitivity Params: sigmaY/fy/Fy, E, H_kin/Hkin, H_iso/Hiso
ops.uniaxialMaterial("Hardening", matTag, Es, Fy, 0, Hkin)

# ops.uniaxialMaterial("Steel01", matTag, Fy, Es, b) # Sensitivity Params: sigmaY/fy/Fy, E, b, a1, a2, a3, a4
# ops.uniaxialMaterial("SteelMP", matTag, Fy, Es, b) # Sensitivity Params: sigmaY/fy, E, b

# Define sections
# ---------------
# Sections defined with "canned" models ("WFSection2d"), otherwise use a FiberSection object (ops.section("Fiber",...))
beamSecTag = 1
beamWidth, beamDepth = 10*cm, 50*cm
ops.section("WFSection2d", beamSecTag, matTag, beamDepth,
            beamWidth, beamWidth, 0, 20, 0)  # Beam section


# Define elements
# ---------------
beamTransTag, beamIntTag = 1, 1
# Linear, PDelta, Corotational
ops.geomTransf("Corotational", beamTransTag)

nip = 5
# Lobatto, Legendre, NewtonCotes, Radau, Trapezoidal, CompositeSimpson
ops.beamIntegration("Legendre", beamIntTag, beamSecTag, nip)

# Beam elements
numEle, nodeTagStart = 5, 10

eleType = "dispBeamColumn"
dm.DiscretizeMember(1, 2, numEle, eleType, beamIntTag,
                    beamTransTag, nodeTagStart, 1)

# Create a Plain load pattern with a Sine/Trig TimeSeries
# -------------------------------------------------------
#                 tag, tStart, tEnd, period
ops.timeSeries("Trig", 1, 0.0, 1.0, 1.0)  # "Trig" or "Triangle"
ops.pattern("Plain", 1, 1)

# +---------------------------------------------+
# |       Define Sensitivity Parameters         |
# +---------------------------------------------+

# /// Each parameter must be unique in the FE domain, and all parameter tags MUST be numbered sequentially starting from 1! ///
ops.parameter(1)  # Blank parameters
ops.parameter(2)
ops.parameter(3)
ops.parameter(4)
for ele in range(1, numEle+1):  # Only column elements
    ops.addToParameter(1, "element", ele, "E")  # E
    # Check the sensitivity parameter names in *.cpp files ("sigmaY" or "fy" or "Fy")
    # https://github.com/OpenSees/OpenSees/blob/master/SRC/material/uniaxial/HardeningMaterial.cpp
    ops.addToParameter(2, "element", ele, "Fy")  # sigmaY/fy/Fy
    ops.addToParameter(3, "element", ele, "Hkin")  # H_kin/Hkin, b
    ops.addToParameter(4, "element", ele, "d")  # d

ops.parameter(5, 'node', 2, 'coord', 1)

ParamSym = ["E", "F_y", "H_{kin}", "d", "L"]
ParamVars = [Es, Fy, Hkin, beamDepth, L]


# +---------------------------------------------+
# |    Define nodal loads & Run the analysis    |
# +---------------------------------------------+

# Create nodal loads at nodes 3 & 5
#       nd  FX   FY       MZ
ops.load(2, 0.0, 1710*kN, 0.0)

# Run analysis with 500 steps
# -------------------------
outputs = run_sensitivity_analysis(
    ctrlNode=2, dof=2, baseNode=1, SensParam=ops.getParamTags(), steps=500, IOflag=False)


# +---------------------------------------------+
# |               Plot results                  |
# +---------------------------------------------+

rows, columns = 6, 2
grid = plt.GridSpec(rows, columns, wspace=0.25, hspace=0.25)
plt.figure(figsize=(10, 12))


def plot_params():
    plt.rc("axes", axisbelow=True)
    plt.tick_params(direction="in", length=5, colors="k", width=0.75)
    plt.grid(True, color="silver", linestyle="solid",
             linewidth=0.75, alpha=0.75)


# Subplot #1
# ----------
plt.subplot(grid[0]), plot_params()
plt.plot(np.array(outputs["time"]), np.array(
    outputs["force"]), "-k", linewidth=1.5)
plt.ylabel(r"Load, $P$ [kN]")

# Subplot #2
# ----------
plt.subplot(grid[1]), plot_params()
plt.plot(np.array(outputs["disp"]), np.array(
    outputs["force"]), "-k", linewidth=2.0, label="$U$")
plt.ylabel(r"Load, $P$ [kN]"), plt.legend(fontsize=9)

i, j = 2, 0
for p in ParamVars:
    # Subplot #i
    # ----------
    plt.subplot(grid[i]), plot_params()
    plt.plot(np.array(outputs["time"]), np.array(
        outputs[f"sensDisp_{j+1}"])*p, "-.k", linewidth=1.5, label=f"DDM")
    plt.ylabel(f"$(\partial U/\partial {ParamSym[j]}){ParamSym[j]}$ [m]")
    plt.legend(fontsize=9)
    if j == 4:
        plt.xlabel(r"Time, $t$")

    # Subplot #ii
    # -----------
    plt.subplot(grid[i+1]), plot_params()
    plt.plot(np.array(outputs["disp"]), np.array(
        outputs["force"]), "-k", linewidth=2.0, label="$U$")
    plt.plot(np.array(outputs["disp"]) + np.array(outputs[f"sensDisp_{j+1}"]) * 0.1*p, np.array(
        outputs["force"]), "--k", linewidth=1.5, label=f"$U + (\partial U/\partial {ParamSym[j]})0.1{ParamSym[j]}$")
    plt.plot(np.array(outputs["disp"]) - np.array(outputs[f"sensDisp_{j+1}"]) * 0.1*p, np.array(
        outputs["force"]), "-.k", linewidth=1.5, label=f"$U - (\partial U/\partial {ParamSym[j]})0.1{ParamSym[j]}$")
    plt.ylabel(r"Load, $P$ [kN]")
    plt.legend(fontsize=9)
    if j == 4:
        plt.xlabel(r"Displacement, $U$ [m]")
    i += 2
    j += 1


# Save figure
# -----------
plt.savefig("CantileverSensitivity2D_v1.png", bbox_inches="tight",
            pad_inches=0.05, dpi=300, format="png")
plt.show()
