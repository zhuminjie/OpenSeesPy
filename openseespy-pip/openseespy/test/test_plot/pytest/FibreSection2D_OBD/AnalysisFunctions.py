

import openseespy.opensees as op

N = 1
kN = 1000*N
m = 1

def BasicAnalysisLoop(ok, nn):
    if ok != 0:
        print("Trying 10 times smaller timestep at load factor", nn)
        op.integrator("LoadControl", .1)
        ok = op.analyze(1)
        
    if ok != 0:
        print("Trying 100 times smaller timestep at load factor", nn)
        op.integrator("LoadControl", .01)
        ok = op.analyze(1)
        
    if ok != 0:
        print("Trying 200 interations at load factor", nn)
        op.test('NormDispIncr', 1.*10**-11, 200)
        ok = op.analyze(1)
                    
    if ok != 0:
        print("Trying ModifiedNewton at load factor", nn)
        op.algorithm("ModifiedNewton")
        op.integrator("LoadControl", 1)
        ok = op.analyze(1)
        
    op.algorithm("Newton")
    op.integrator("LoadControl", 1)
    op.test('NormDispIncr', 1.*10**-11, 50)
    
    return ok




def PushoverLcF(Nsteps):
    
    ControlNode = 4
    ControlNodeDof = 1
    dForce = 1.*kN
    
    # Define time series
    #  timeSeries('Constant', tag, '-factor', factor=1.0)
    op.timeSeries('Constant',1)
    op.timeSeries('Linear', 2)
    
    
    # define loads
    op.pattern('Plain',1 , 2)
    op.load(ControlNode, dForce, 0., 0.)
    
    
    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    op.integrator("LoadControl", 1.0)
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")

    # Create Test
    op.test('NormDispIncr', 1.*10**-11, 50)
    
    # Run Analysis
    
    op.record()
    ok = op.analyze(Nsteps)


def PushoverLcD(dispMax):
    
    ControlNode = 4
    ControlNodeDof = 1
    du = 0.00001*m
    
    # Define time series
    #  timeSeries('Constant', tag, '-factor', factor=1.0)
    op.timeSeries('Constant',1)
    op.timeSeries('Linear', 2)
    
    
    # define loads
    op.pattern('Plain',1 , 2)
    op.sp(ControlNode, ControlNodeDof, du)
    
    
    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    op.integrator("LoadControl", 1)
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")

    # Create Test
    op.test('NormDispIncr', 1.*10**-8, 50)
    
    # Run Analysis
    
    op.record()
    # ok = op.analyze(Nsteps)
    
    nn = 0
    while(op.nodeDisp(ControlNode, ControlNodeDof) < dispMax  ):       
    
        ok = op.analyze(1)
        
        if ok != 0:
            ok = BasicAnalysisLoop(ok, nn)
            
        if ok != 0:
            print("Analysis failed at load factor:", nn)
            break
        
        nn =+ 1
        

        
    print()
    print("# Analysis Complete #")
    
    
    
def PushoverDcF(Nsteps):
    
    ControlNode = 4
    ControlNodeDof = 1
    dForce = 1.*kN
    du = 0.00001*m
    
    # Define time series
    #  timeSeries('Constant', tag, '-factor', factor=1.0)
    op.timeSeries('Constant',1)
    op.timeSeries('Linear', 2)
    
    
    # define loads
    op.pattern('Plain',1 , 2)
    op.load(ControlNode, dForce, 0., 0.)
    
    
    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    op.integrator("DisplacementControl", ControlNode, ControlNodeDof, du)
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")

    # Create Test
    op.test('NormDispIncr', 1.*10**-11, 50)
    
    # Run Analysis
    
    op.record()
    
    ok = op.analyze(Nsteps)
