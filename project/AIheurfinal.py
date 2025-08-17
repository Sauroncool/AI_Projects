
import numpy as np
coordsNow='23.2334,89.1244'
avgV=30
scaleV=100
coordsGoal='34.124,100.111'
coordsStart='23.2365,89.1256'
coordLandmark='33.45554,45.98889'  #loop to keep changing
def numbify (coords):
    i = 0
    flag = 0
    lat = ''
    long = ''
    for ch in coords:
        if (ch == ','):
            flag += 1
        if (flag == 0):
            long += coords[i]
        elif (ch != ','):
            lat += coords[i]
        i += 1
    lati = float(lat)
    longi = float(long)
    return([lati,longi])


class n:
    nloc=numbify(coordsNow)
    x=nloc[0]
    y=nloc[1]

class g:
    gloc=numbify(coordsGoal)
    x=gloc[0]
    y=gloc[1]

class s:
    sloc=numbify(coordsStart)
    x=sloc[0]
    y=sloc[1]

W=avgV/scaleV #scaling weight

#Manhattan grids
def heuristicMan(n):
    delx=np.abs(n.x-g.x)
    dely=np.abs(n.y-g.y)
    return W*np.sqrt((delx^2+dely^2))

class lm1:
    lloc=numbify(coordLandmark)
    x=lloc[0]
    y=lloc[1]


class lm2:
    lloc=numbify(coordLandmark)
    x=lloc[0]
    y=lloc[1]



def heuristic(n,g,lm1,lm2):
    return (heuristicMan(n,lm1)+heuristicMan(lm1,lm2)+heuristicMan(lm2,g))*W


#tiebreaker lineup method
def tiebreak(n1,n2):
    return np.minimum(crosscheck(n1,g,s)+cost(n1),crosscheck(n2,g,s)+cost(n2))
def crosscheck(n,g,s):
    f=0.001*W
    delxn=n.x-g.x
    delyn=n.y-g.y
    delxs=s.x-g.x
    delys=s.y-g.y
    cp=np.abs(delxn*delys-delxs*delyn)
    alp= heuristic(n)+(f)*cp
    return alp






#cost function variation
def linestart(n):
    return W*np.sqrt(((n.x-s.x)**2+(n.y-s.y)**2))

def cost(n):
    return linestart(n)

