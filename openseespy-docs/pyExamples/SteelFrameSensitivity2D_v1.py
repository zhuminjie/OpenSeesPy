"""
The source code is developed by Marin Grubišić https://github.com/mgrubisic from University of Osijek, Croatia.
The numerical model with the associated analysis was described in detail by Prof. Michael Scott in the Portwood Digital blog https://portwooddigital.com/2021/01/03/sensitivity-training/.
Run the source code in your favorite Python program and should see following plot.
"""

import time
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import openseespy.postprocessing.Get_Rendering as opsplt
import openseespy.opensees as ops
import openseespy.postprocessing.ops_vis as opsv

print(f"\nOpenSees " + ops.version() + " | Python " + sys.version)

# +---------------------------------------------+
# |                   Units                     |
# +---------------------------------------------+

inch = 1.0  # define basic units
kip = 1.0
sec = 1.0

ft = 12*inch
lb = kip/1000
ksi = kip/inch**2
psf = lb/ft**2

# +---------------------------------------------+
# |           Define some functions             |
# +---------------------------------------------+


def run_gravity_analysis(steps=10):
    """
    Run gravity analysis (in 10 steps)
    """
    ops.wipeAnalysis()
    ops.system("BandGeneral")
    ops.numberer("RCM")
    ops.constraints("Transformation")
    ops.test("NormDispIncr", 1.0E-12, 10, 3)
    ops.algorithm("Newton")  # KrylovNewton
    ops.integrator("LoadControl", 1/steps)
    ops.analysis("Static")
    ops.analyze(steps)
    print("\n==> Gravity Analysis Completed!\n")
    # Set the gravity loads to be constant & reset the time in the domain
    ops.loadConst("-time", 0.0)
    ops.wipeAnalysis()


def run_sensitivity_pushover_analysis(ctrlNode, baseNodes, dof, Dincr, max_disp, SensParam, IOflag=False):
    """
    Run pushover analysis with sensitivity
    """
    ops.wipeAnalysis()
    start_time = time.time()
    ops.loadConst("-time", 0.0)

    print("==> ... Running Pushover Analysis ...\n")

    testType = "NormDispIncr"  # EnergyIncr
    tolInit = 1.0e-8
    iterInit = 10  # Set the initial Max Number of Iterations
    algorithmType = "Newton"  # Set the algorithm type

    ops.system("BandGeneral")
    ops.constraints("Transformation")
    ops.numberer("RCM")
    ops.test(testType, tolInit, iterInit)
    ops.algorithm(algorithmType)
    # Change the integration scheme to be displacement control
    #                                     node      dof  init Jd min max
    ops.integrator("DisplacementControl", ctrlNode, dof, Dincr)
    ops.analysis("Static")
    ops.sensitivityAlgorithm("-computeAtEachStep")

    if IOflag:
        print(f"Single Pushover: Push node {ctrlNode} to {max_disp} inches.\n")

    # Set some parameters
    tCurrent = ops.getTime()
    currentStep = 1

    outputs = {
        "time": [],
        "rel_disp": [],
        "force": []
    }

    for sens in SensParam:
        outputs[f"sensLambda_{sens}"] = []

    nodeList = []
    for node in baseNodes:
        nodeList.append(f"- ops.nodeReaction({node}, dof) ")

    nodeList = "".join(nodeList)
    currentDisp = ops.nodeDisp(ctrlNode, dof)
    ok = 0

    while ok == 0 and currentDisp < max_disp:
        ops.reactions()
        ok = ops.analyze(1)
        tCurrent = ops.getTime()
        currentDisp = ops.nodeDisp(ctrlNode, dof)

        if IOflag:
            print(
                f"Current displacement ==> {ops.nodeDisp(ctrlNode, dof):.3f} inches")

        # if the analysis fails try initial tangent iteration
        if ok != 0:
            print("\n==> Trying relaxed convergence...")
            ops.test(testType, tolInit/0.01, iterInit*50)
            ok = ops.analyze(1)
            if ok == 0:
                print("==> that worked ... back to default analysis...\n")
            ops.test(testType, tolInit, iterInit)

        if ok != 0:
            print("\n==> Trying Newton with initial then current...")
            ops.test(testType, tolInit/0.01, iterInit*50)
            ops.algorithm("Newton", "-initialThenCurrent")
            ok = ops.analyze(1)
            if ok == 0:
                print("==> that worked ... back to default analysis...\n")
            ops.algorithm(algorithmType)
            ops.test(testType, tolInit, iterInit)

        if ok != 0:
            print("\n==> Trying ModifiedNewton with initial...")
            ops.test(testType, tolInit/0.01, iterInit*50)
            ops.algorithm("ModifiedNewton", "-initial")
            ok = ops.analyze(1)
            if ok == 0:
                print("==> that worked ... back to default analysis...\n")
            ops.algorithm(algorithmType)
            ops.test(testType, tolInit, iterInit)

        currentStep += 1
        tCurrent = ops.getTime()

        outputs["time"].append(tCurrent)
        outputs["rel_disp"].append(ops.nodeDisp(ctrlNode, dof))
        outputs["force"].append(eval(nodeList))

        for sens in SensParam:
            # sensLambda(patternTag, paramTag)
            outputs[f"sensLambda_{sens}"].append(ops.sensLambda(1, sens))

    # Print a message to indicate if analysis completed succesfully or not
    if ok == 0:
        print("==> Pushover Analysis Completed SUCCESSFULLY!\n")
    else:
        print("==> Pushover Analysis Completed FAILED!\n")

    print(
        f"Pushover elapsed time is {(time.time() - start_time):.3f} seconds.\n")

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
ops.node(1, 0.0, 0.0)  # Ground Level
ops.node(2, 30*ft, 0.0)
ops.node(3, 0.0, 15*ft)  # 1st Floor Level
ops.node(4, 30*ft, 15*ft)
ops.node(5, 0.0, 2*15*ft)  # 2nd Floor Level
ops.node(6, 30*ft, 2*15*ft)

# Fix supports at base of columns
# -------------------------------
ops.fix(1, 1, 1, 1)
ops.fix(2, 1, 1, 1)

# Define material
# ---------------
matTag = 1

Fy = 50.0*ksi       # Yield stress
Es = 29000.0*ksi    # Modulus of Elasticity of Steel
b = 1/100		    # 1% Strain hardening ratio

# Sensitivity-ready steel materials: Hardening, Steel01, SteelMP, BoucWen, SteelBRB, StainlessECThermal, SteelECThermal, ...
ops.uniaxialMaterial("Steel01", matTag, Fy, Es, b)
# ops.uniaxialMaterial("SteelMP", matTag, Fy, Es, b)

# Define sections
# ---------------
# Sections defined with "canned" models ("WFSection2d"), otherwise use a FiberSection object (ops.section("Fiber",...))
colSecTag, beamSecTag = 1, 2
WSection = {  # d, tw, bf, tf
    "W18x76": [18.2*inch, 0.425*inch, 11.04*inch, 0.68*inch],
    "W14X90": [14.02*inch, 0.44*inch, 14.52*inch, 0.71*inch],
}

ColSectType1 = "W14X90"
BeamSectType2 = "W18x76"

ops.section("WFSection2d", colSecTag, matTag,
            WSection[ColSectType1][0], WSection[ColSectType1][1],
            WSection[ColSectType1][2], WSection[ColSectType1][3], 20, 4)  # Column section
ops.section("WFSection2d", beamSecTag, matTag,
            WSection[BeamSectType2][0], WSection[BeamSectType2][1],
            WSection[BeamSectType2][2], WSection[BeamSectType2][3], 20, 4)  # Beam section

# Define elements
# ---------------
colTransTag, beamTransTag = 1, 2
# Linear, PDelta, Corotational
ops.geomTransf("Corotational", colTransTag)
ops.geomTransf("Linear", beamTransTag)

colIntTag, beamIntTag = 1, 2

nip = 5
# Lobatto, Legendre, NewtonCotes, Radau, Trapezoidal, CompositeSimpson
ops.beamIntegration("Lobatto", colIntTag, colSecTag, nip),
ops.beamIntegration("Lobatto", beamIntTag, beamSecTag, nip)

# Column elements
ops.element("forceBeamColumn", 10, 1, 3, colTransTag, colIntTag, "-mass", 0.0)
ops.element("forceBeamColumn", 11, 3, 5, colTransTag, colIntTag, "-mass", 0.0)
ops.element("forceBeamColumn", 12, 2, 4, colTransTag, colIntTag, "-mass", 0.0)
ops.element("forceBeamColumn", 13, 4, 6, colTransTag, colIntTag, "-mass", 0.0)

# Beam elements
ops.element("forceBeamColumn", 14, 3, 4,
            beamTransTag, beamIntTag, "-mass", 0.0)
ops.element("forceBeamColumn", 15, 5, 6,
            beamTransTag, beamIntTag, "-mass", 0.0)

# Create a Plain load pattern with a Linear TimeSeries
# ----------------------------------------------------
ops.timeSeries("Linear", 1)
ops.pattern("Plain", 1, 1)

# +---------------------------------------------+
# |       Define Sensitivity Parameters         |
# +---------------------------------------------+

# /// Each parameter must be unique in the FE domain, and all parameter tags MUST be numbered sequentially starting from 1! ///
ops.parameter(1)  # Blank parameters
ops.parameter(2)
ops.parameter(3)
for ele in [10, 11, 12, 13]:  # Only column elements
    ops.addToParameter(1, "element", ele, "E")
    # Check the sensitivity parameter name in *.cpp files ("sigmaY" or "fy", somewhere also "Fy")
    ops.addToParameter(2, "element", ele, "fy")
    ops.addToParameter(3, "element", ele, "b")


# Run analysis with 10 steps
# -------------------------
run_gravity_analysis(steps=10)

# +---------------------------------------------+
# |    Define nodal loads & Run the analysis    |
# +---------------------------------------------+

# Create nodal loads at nodes 3 & 5
#       nd  FX   FY   MZ
ops.load(3, 1/3, 0.0, 0.0)
ops.load(5, 2/3, 0.0, 0.0)

max_disp = 20*inch
pushover_output = run_sensitivity_pushover_analysis(
    ctrlNode=5, baseNodes=[1, 2], dof=1, Dincr=1/25*inch, max_disp=max_disp, SensParam=[1, 2, 3], IOflag=False)

# +---------------------------------------------+
# |               Plot results                  |
# +---------------------------------------------+

rows, columns = 6, 1
grid = plt.GridSpec(rows, columns, wspace=0.25, hspace=0.25)
plt.figure(figsize=(10, 10))


def plot_params():
    plt.rc("axes", axisbelow=True)
    plt.xlim(xmin=0.0, xmax=max_disp)
    plt.tick_params(direction="in", length=5, colors="k", width=0.75)
    plt.grid(True, color="silver", linestyle="solid",
             linewidth=0.75, alpha=0.75)


# Subplot #1
# ----------
plt.subplot(grid[0]), plot_params()
plt.plot(np.array(pushover_output["rel_disp"]), np.array(
    pushover_output["force"]), "-k", linewidth=2.0, label="$U$")
plt.plot(np.array(pushover_output["rel_disp"]), np.array(
    pushover_output["force"]) + np.array(pushover_output["sensLambda_1"]) * Es, "--k", linewidth=1.5, label="$U + (\partial V_b/\partial E)E$")
plt.plot(np.array(pushover_output["rel_disp"]), np.array(
    pushover_output["force"]) - np.array(pushover_output["sensLambda_1"]) * Es, "-.k", linewidth=1.5, label="$U - (\partial V_b/\partial E)E$")
plt.ylabel(r"$V_b$ [kip]")
plt.title(r"Displacement Control", fontsize=14)
plt.legend(fontsize=9)

# Subplot #2
# ----------
plt.subplot(grid[1]), plot_params()
plt.plot(np.array(pushover_output["rel_disp"]), np.array(
    pushover_output["force"]), "-k", linewidth=2.0, label="$U$")
plt.plot(np.array(pushover_output["rel_disp"]), np.array(
    pushover_output["force"]) + np.array(pushover_output["sensLambda_2"]) * Fy, "--k", linewidth=1.5, label="$U + (\partial V_b/\partial F_y)F_y$")
plt.plot(np.array(pushover_output["rel_disp"]), np.array(
    pushover_output["force"]) - np.array(pushover_output["sensLambda_2"]) * Fy, "-.k", linewidth=1.5, label="$U - (\partial V_b/\partial F_y)F_y$")
plt.ylabel(r"Base Shear, $V_b$ [kip]")
plt.legend(fontsize=9)

# Subplot #3
# ----------
plt.subplot(grid[2]), plot_params()
plt.plot(np.array(pushover_output["rel_disp"]), np.array(
    pushover_output["force"]), "-k", linewidth=2.0, label="$U$")
plt.plot(np.array(pushover_output["rel_disp"]), np.array(
    pushover_output["force"]) + np.array(pushover_output["sensLambda_3"]) * b, "--k", linewidth=1.5, label="$U + (\partial V_b/\partial b)b$")
plt.plot(np.array(pushover_output["rel_disp"]), np.array(
    pushover_output["force"]) - np.array(pushover_output["sensLambda_3"]) * b, "-.k", linewidth=1.5, label="$U - (\partial V_b/\partial b)b$")
plt.ylabel(r"$V_b$ [kip]")
plt.legend(fontsize=9)

# Subplot #4
# ----------
plt.subplot(grid[3]), plot_params()
plt.plot(np.array(pushover_output["rel_disp"]), np.array(pushover_output["sensLambda_1"]) * Es, "-.k", linewidth=2.0,
         label=f"DDM")
plt.ylabel(r"$(\partial V_b/\partial E)E$ [kip]")
plt.legend()

# Subplot #5
# ----------
plt.subplot(grid[4]), plot_params()
plt.plot(np.array(pushover_output["rel_disp"]), np.array(pushover_output["sensLambda_2"]) * Fy, "-.k", linewidth=2.0,
         label=f"DDM")
plt.ylabel(r"$(\partial V_b/\partial F_y)F_y$ [kip]")
plt.legend()

# Subplot #6
# ----------
plt.subplot(grid[5]), plot_params()
plt.plot(np.array(pushover_output["rel_disp"]), np.array(pushover_output["sensLambda_3"]) * b, "-.k", linewidth=2.0,
         label=f"DDM")
plt.xlabel(r"Roof Displacement, $U$ [in]")
plt.ylabel(r"$(\partial V_b/\partial b)b$ [kip]")
plt.legend()

# Save figure
# -----------
plt.savefig("SteelFrameSensitivity2D_v1.png", bbox_inches="tight",
            pad_inches=0.05, dpi=300, format="png")
plt.show()
