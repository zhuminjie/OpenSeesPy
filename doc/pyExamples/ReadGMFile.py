"""
author : JAWAD FAYAZ (email: jfayaz@uci.edu) (website: https://jfayaz.github.io) 

------------------------------ Instructions ---------------------------------------------
 
This is an associated file to generation of RotD(50 and 100) Spectra of bi-directional GM

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

def ReadGMFile():
    with open (inFile, "r") as myfile:
        data = myfile.read().splitlines()
        sp = data[3].split(' ')
        NumPts = int(sp[2].split(',')[0])
        dt = float(sp[4])
        hdlines = 4 
        
        for k in range(0,hdlines):
            del data [0]
        
       
        data = list(filter(str.strip, data)) 
        gm = np.array(list(map(float, data)))
        gmXY[i+1] = gm
        
        
        del data
        del gm
        
        return dt,NumPts,gmXY