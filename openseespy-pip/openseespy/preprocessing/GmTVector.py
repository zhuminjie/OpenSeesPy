"""

Created on Various Days 

@author: Bijan SayyafZadeh (B.sayyaf@yahoo.com) (LinkedIn : https://www.linkedin.com/in/bijan-sayyafzadeh-6027aa7a/)

"""

def VecProduct(V1,V2):
  #Calculate Vectors External Products
  x=(V1[1]*V2[2]-V1[2]*V2[1])
  y=(-V1[0]*V2[2]+V1[2]*V2[0])
  z=(V1[0]*V2[1]-V2[0]*V1[1])
  return x,y,z

def DotPrdct(V1,V2):
    #Calculate vectors internal products    
    return V1[0]*V2[0]+V1[1]*V2[1]+V1[2]*V2[2]

def Nrmlz(V,a):
    #Normilize of vector V size equal to scalar  a
    A=(V[0]**2+V[1]**2+V[2]**2)**0.5
    V=V[0]/A*a,V[1]/A*a,V[2]/A*a
    return V

def VecSize(V):
    'Return a vector size'
    return (V[0]**2+V[1]**2+V[2]**2)**0.5

def GmTVector(FirstNode,SecondNode,Theta,VerticalDOF=3):
    
    '''
    
     @author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)
    
    -----------------------------------------------------------------------
    Parameters:
    -----------------------------------------------------------------------
    FirstNode : Opensees 3D node as a list with 3 elements
        
    SecondNode : Opensees 3D node as a list with 3 elements

    Theta (Deg) : An scalar value that shows the cross section rotation angle. Rotation Direction is according right hand rule!
    
    VerticalDOF : Shows the Vertical Direction that is considered by user 
                  For example if I considered nodes coordinate as x,y,z and 
                  z is my vertical Dof so I have to enter 3
                  if y is my verticalDOF then I have to enter 2
                  if x is my vertical DOF then I have to enter 1
                  
    -------------------------------------------------------------------------
    Description:
    -------------------------------------------------------------------------
    Non_Columns:
        For any Elements except columns, when you look from the Nodei (First node of element)
        to the Nodej(Second node of the element) The main local axis of the element is considered 
        To THE LEFT SIDE OF THE MENTIONED DIRECTION.
                
    
    Columns:
        For columns the cross section main axis is considered in 1st horizontal coordinate direction. 
        
        
        
                           _____________
                           |            |
                           |            |
                           |            |
                           |   <------  |  The Main local axis of cross section.
                           |            |
                           |____________|
        

    -------------------------------------------------------------------------
    Function Returns:
    -------------------------------------------------------------------------
    GeomTrans : return a list with 3 elements that are 3 scalar values 
        using this function you will have the local Geometric transforemation of the element
        
    -------------------------------------------------------------------------
    Usage Example:
    -------------------------------------------------------------------------    
    Nodei=[5, 6, 3]
    Nodej=[8, 9, 5]
    Theta=0
    GTR=GmTVector(Nodei,Nodej,Theta,VerticalDOF=3)
    #GTR is the Geometric Transformation Vector of the element with Nodei and Nodej as its end Nodes
    
    a=GmTVector([0,0,0],[10,0,0],0) ----> a=[0.0, 1.0, 0]
    a=GmTVector([10,0,0],[0,0,0],0) ----> a=[0.0, -1.0, 0]
    a=GmTVector([0,0,0],[10,0,0],90) ----> a=[0.0, 0, -1.0]
    
    a=GmTVector([0,0,0],[0,10,0],0) ----> a=[-1.0, 0.0, 0]
    a=GmTVector([0,10,0],[0,0,0],0) ----> a=[1.0, 0.0, 0]
    a=GmTVector([0,0,0],[0,10,0],90) ----> a=[0, 0.0, -1.0]
    
    a=GmTVector([0,0,0],[0,0,10],0) ----> a=[-1.0, 0, 0.0]
    a=GmTVector([0,0,10],[0,0,0],0) ----> a=[1.0, 0, 0.0]
    '''
    
    # Convert nodeTag to Node coordinate IF USER ENTER NODE TAG
    import openseespy.opensees as ops
    if type(FirstNode)==int:
      FirstNode=ops.nodeCoord(FirstNode)
    
    if type(SecondNode)==int:
      SecondNode=ops.nodeCoord(SecondNode)
    
    
    
    
    # First, if Vertical Direction is not the 3rd vector I change the input values and move the 
    # vertical dof to the end 
    
    if VerticalDOF==3:
       pass
    elif VerticalDOF==2:
       FirstNode[1], FirstNode[2]=FirstNode[2], FirstNode[1]
       SecondNode[1], SecondNode[2]=SecondNode[2], SecondNode[1]
    elif VerticalDOF==1:
       FirstNode[0], FirstNode[2]=FirstNode[2], FirstNode[0]
       SecondNode[0], SecondNode[2]=SecondNode[2], SecondNode[0]       
    else:
       return "Wrong Value for Vertical DOF"
        
       
    #First node and second node are List by 3 elements and theta is the rotation angle
    #--------------------------Finding main Vectors -------------------
    import math
    
    #Initial Data
    x1, y1, z1=FirstNode[0],FirstNode[1],FirstNode[2]
    x2, y2, z2=SecondNode[0],SecondNode[1],SecondNode[2]
    theta=Theta-180

    
    #V1 is the Main element
    V1=[(x2-x1),(y2-y1),(z2-z1)]
    
    #V2 is a vector that is located in Perpendicular plane
    z2=z2+0.1
    
    if (x1==x2 and y1==y2): #Columns Condition
        z2=z2-0.1
        V1=[(x2-x1),(y2-y1),abs(z2-z1)]
        if z2<z1:
            theta=-theta
            
        z2=z1
        y2=y1-0.1

        
       
    V2=[(x2-x1),(y2-y1),(z2-z1)]
     #VN is the vector that is normal to the perpendicular page of V1 that is that z local axis of section
    VN=VecProduct(V1,V2)

     
     #---------------------- Rotating -----------------------------
    theta=theta*float(math.pi)/180
    
    c=math.cos(theta)
    s=math.sin(theta)
     
    #VR is rotated vector of VN around V1 (Main Vector) REF:https://en.wikipedia.org/wiki/Rotation_matrix
    ux,uy,uz=V1[0]/VecSize(V1),V1[1]/VecSize(V1),V1[2]/VecSize(V1)
    VR=[
         (c+ux**2*(1-c))*VN[0]+(ux*uy*(1-c)-uz*s)*VN[1]+(ux*uz*(1-c)+uy*s)*VN[2],
         (uy*ux*(1-c)+uz*s)*VN[0]+(c+uy**2*(1-c))*VN[1]+(uy*uz*(1-c)-ux*s)*VN[2],
         (uz*ux*(1-c)-uy*s)*VN[0]+(uz*uy*(1-c)+ux*s)*VN[1]+(c+uz**2*(1-c))*VN[2]
         ]
     
    VR=Nrmlz(VR,1)
    VN=Nrmlz(VN,1)
     
     
     #--------------- Calculation Of Geometric Transform ---------------------
     
    VRsize=VecSize(VR)

     
    GeomTrans=[VR[0]/VRsize,VR[1]/VRsize,VR[2]/VRsize]
    
    
    # Becaus at the first of the code I changes the vertical DOF location, Finally
    # I have to move it back to its initial location    
    if VerticalDOF==3:
       pass
    elif VerticalDOF==2:
       GeomTrans[1], GeomTrans[2]=GeomTrans[2], GeomTrans[1]
    elif VerticalDOF==1:
       GeomTrans[0], GeomTrans[2]=GeomTrans[2], GeomTrans[0]

    
    
    
    return GeomTrans
