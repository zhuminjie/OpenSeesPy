from math import asin, sqrt, tan
#  PDelta Effects 

# REFERENCES:
# R.C.Kaehler, D.W.White, Y.D.Kim, "Frame Design Using Web-Tapered Members", AISC 2011

print("===============================================================")
print("AISC - Design Guide 25 - Frame Design Using Web-Tapered Members")

H = 10.0
L = 196.0
PI = 2.0*asin(1.0)

ok = 0
counter = 0

print("Prismatic Beam Benchmark Problems\n")
print("    - Case 1 (Single Curvature)     - elasticBeamColumn")
print("------+--------+-------------------------+-------------------------")
print("      |        |     Tip Displacement    |      Base Moment        ")
print("------+--------+--------+---------+------+---------+--------+------")
formatString = '{:>5s}|{:>8s}|{:>8s}|{:>9s}|{:>6s}|{:>9s}|{:>8s}|{:>6s}'
print(formatString.format('numEle', 'alpha', 'Exact', 'OpenSees', '%Error', 'Exact', 'OpenSees', '%Error'))
print("------+--------+--------+---------+------+---------+--------+------")

for numEle in [1,2,4,10]:
    for alpha in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.67]:
        wipe()
        model('Basic', '-ndm', 2)
        
        E = 29500.0
        A = 51.7
        I = 2150.0
        
        Pel = PI*PI*E*I/(L*L)
        Pcr = Pel/4.0
        Pr = Pcr
        
        dY = L/numEle
        for i in range(numEle+1):
            node( i +1, 0., i * dY)

        
        geomTransf('PDelta', 1)
        section( 'Elastic', 1, E, A, I)
        eleTag = 1
        iNode = 1
        jNode = 2
        for i in range(numEle):
            element( 'elasticBeamColumn', eleTag, iNode, jNode, A, E, I, 1)
            eleTag += 1
            iNode += 1
            jNode += 1
        
        fix( 1, 1, 1, 1)
        
        u = PI/2.0*sqrt(alpha * Pr/Pel)
        
        if u != 0:
            resU = (H*L*L*L/(3.0*E*I)) * (3.0*(tan(2.0*u)-2.0*u)/(8.0*u*u*u))
            resM = H*L*(tan(2.*u)/(2.*u))
        else:
            resU = (H*L*L*L/(3.0*E*I))
            resM = H*L
        
        timeSeries( 'Linear', 1)
        pattern( 'Plain', 1, 1 )
        load( numEle+1, H, -alpha*Pr, 0.)
        
        
        constraints('Plain')
        system( 'ProfileSPD')
        numberer( 'Plain')
        integrator( 'LoadControl', 1.0)
        test( 'NormDispIncr', 1.0e-12, 6, 0)
        algorithm( 'Newton')
        analysis( 'Static')
        analyze(1)
        
        delta = nodeDisp(numEle + 1, 1)
        forces = eleResponse( 1, 'forces')
        moment = forces[2]
        formatString = '{:>6.0f}|{:>8.2f}|{:>8.4f}|{:>9.4f}|{:>6.1f}|{:>9.2f}|{:>8.2f}|{:>6.1f}'
        print(formatString.format(numEle, alpha, resU, delta, 100*(resU-delta)/delta, resM, moment, 100*(resM-moment)/moment))
    
    print("------+--------+--------+---------+------+---------+--------+------")


# test on last one
if abs(100*(resU-delta)/delta) > 0.5 or abs(100*(resM-moment)/moment) > 0.5:
    ok = 1
    print(abs(100*(resU-delta)/delta), ' > 0.5 || ', abs(100*(resM-moment)/moment), ' > 0.5')


print("Prismatic Beam Benchmark Problems\n")
print("    - Case 1 (Single Curvature) - forceBeamColumnCBDI element")
print("------+--------+-------------------------+-------------------------")
print("      |        |     Tip Displacement    |      Base Moment        ")
print("------+--------+--------+---------+------+---------+--------+------")
formatString = '{:>5s}|{:>8s}|{:>8s}|{:>9s}|{:>6s}|{:>9s}|{:>8s}|{:>6s}'
print(formatString.format('numEle', 'alpha', 'Exact', 'OpenSees', '%Error', 'Exact', 'OpenSees', '%Error'))
print("------+--------+--------+---------+------+---------+--------+------")

for numEle in [1]:
    for alpha in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.67]:
        wipe()
        model( 'Basic', '-ndm', 2)
        
        E = 29500.0
        A = 51.7
        I = 2150.0
        
        Pel = PI*PI*E*I/(L*L)
        Pcr = Pel/4.0
        Pr = Pcr
        
        dY = L/numEle
        for i in range(numEle+1):
            node( i +1, 0., i * dY)

        
        geomTransf( 'PDelta', 1)
        integTag = 1
        beamIntegration( 'Legendre', integTag, 1, 4)
        section( 'Elastic', 1, E, A, I)
        eleTag = 1
        iNode = 1
        jNode = 2
        for i in range(numEle):
            element( 'forceBeamColumnCBDI', eleTag, iNode, jNode, 1, integTag)
            eleTag += 1
            iNode += 1
            jNode += 1

        
        fix( 1, 1, 1, 1)
        
        u = PI/2.0*sqrt(alpha * Pr/Pel)
        
        if u != 0:
            resU = (H*L*L*L/(3.0*E*I)) * (3.0*(tan(2.0*u)-2.0*u)/(8.0*u*u*u))
            resM = H*L*(tan(2.*u)/(2.*u))
        else:
            resU = (H*L*L*L/(3.0*E*I))
            resM = H*L

        
        timeSeries( 'Linear', 1)
        pattern( 'Plain', 1, 1) 
        load( numEle+1, H, -alpha*Pr, 0.)
        
        constraints('Plain')
        system( 'ProfileSPD')
        numberer( 'Plain')
        integrator( 'LoadControl', 1.0)
        test( 'NormDispIncr', 1.0e-12, 6, 0)
        algorithm( 'Newton')
        analysis( 'Static')
        analyze(1)
        
        delta = nodeDisp( numEle + 1, 1)
        forces = eleResponse(1,'forces')
        moment = forces[2]

        formatString = '{:>6.0f}|{:>8.2f}|{:>8.4f}|{:>9.4f}|{:>6.1f}|{:>9.2f}|{:>8.2f}|{:>6.1f}'
        print(formatString.format(numEle, alpha, resU, delta, 100*(resU-delta)/delta, resM, moment, 100*(resM-moment)/moment))

    print("------+--------+--------+---------+------+---------+--------+------")



# test on last one
if abs(100*(resU-delta)/delta) > 0.5 or abs(100*(resM-moment)/moment) > 0.5:
    ok = 1
    print(abs(100*(resU-delta)/delta), ' > 0.5 || ', abs(100*(resM-moment)/moment), ' > 0.5')
    


print("\n\n    - Case 2 (Double Curvature)  - elasticBeamColumn")
print("------+--------+-------------------------+-------------------------")
print("      |        |     Tip Displacement    |      Base Moment        ")
print("------+--------+--------+---------+------+---------+--------+------")
formatString = '{:>5s}|{:>8s}|{:>8s}|{:>9s}|{:>6s}|{:>9s}|{:>8s}|{:>6s}'
print(formatString.format('numEle', 'alpha', 'Exact', 'OpenSees', '%Error', 'Exact', 'OpenSees', '%Error'))
print("------+--------+--------+---------+------+---------+--------+------")

for numEle in [1,2,10]:
    for alpha in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.67]:
        wipe()
        model( 'Basic', '-ndm', 2)
        
        E = 29500.0
        A = 51.7
        I = 2150.0
        
        Pel = PI*PI*E*I/(L*L)
        Pcr = Pel/4.0
        Pr = Pcr
        
        dY = L/numEle
        for i in range(numEle+1):
            node( i +1, 0., i * dY)
        
        geomTransf( 'PDelta', 1)
        integTag = 1
        beamIntegration( 'Legendre', integTag, 1, 4)
        section( 'Elastic', 1, E, A, I)
        eleTag = 1
        iNode = 1
        jNode = 2
        for i in range(numEle):
            element( 'forceBeamColumnCBDI', eleTag, iNode, jNode, 1, integTag)
            eleTag += 1
            iNode += 1
            jNode += 1

        
        fix( 1, 1, 1 ,1)
        fix( numEle+1, 0, 0, 1)
        
        u = PI/2.0*sqrt(alpha * Pr/Pel)
        
        if u != 0:
            resU = (H*L*L*L/(12.0*E*I)) * (3.0*(tan(u)-u)/(u*u*u))
            resM = H*L/2.0*(tan(u)/(u))
        else:
            resU = (H*L*L*L/(12.0*E*I))
            resM = H*L/2.0

        
        timeSeries( 'Linear', 1)
        pattern( 'Plain', 1, 1) 
        load( numEle+1, H, -alpha*Pr, 0.)
        
        constraints('Plain')
        system( 'ProfileSPD')
        numberer( 'Plain')
        integrator( 'LoadControl', 1.0)
        test( 'NormDispIncr', 1.0e-12, 6, 0)
        algorithm( 'Newton')
        analysis( 'Static')
        analyze(1)
        
        delta = nodeDisp( numEle + 1, 1)
        forces = eleResponse(1,'forces')
        moment = forces[2]

        formatString = '{:>6.0f}|{:>8.2f}|{:>8.4f}|{:>9.4f}|{:>6.1f}|{:>9.2f}|{:>8.2f}|{:>6.1f}'
        print(formatString.format(numEle, alpha, resU, delta, 100*(resU-delta)/delta, resM, moment, 100*(resM-moment)/moment))

    print("------+--------+--------+---------+------+---------+--------+------")


# test on last one
if abs(100*(resU-delta)/delta) > 0.5 or abs(100*(resM-moment)/moment) > 0.5:
    ok = 1
    print(abs(100*(resU-delta)/delta), ' > 0.5 || ', abs(100*(resM-moment)/moment), ' > 0.5')


if ok == 0:
    print("PASSED Verification Test AISC25.python \n\n")
else:
    print("FAILED Verification Test AISC25.python \n\n")

