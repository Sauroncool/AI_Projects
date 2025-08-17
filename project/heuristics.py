# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:20:53 2023

@author: Pranav Koppa
"""
import numpy as np

class n:
    x=12
    y=13

class g:
    x=100
    y=100

class s:
    x=0
    y=0
    
W=2 #scaling weight

#Manhattan grids
def heuristicM(n):
    delx=np.abs(n.x-g.x)
    dely=np.abs(n.y-g.y)
    return W*(delx+dely)

#Euclidean grids
def heuristicE(n):
    delx=np.abs(n.x-g.x)
    dely=np.abs(n.y-g.y)
    return W*np.sqrt(delx**2+dely**2)


#tiebreakers

d=0 #change to 1 to implement Euclidean model
#Nudging heuristic function upwards in case of a tie in f
def heuristicdiff(n,d):
    f=4/1000
    if(d):
        alp= heuristicE(n)*(1.0+f)
    else:
        alp= heuristicM(n)*(1.0+f)
    return alp
       

#lineup method
def crosscheck(n,g,s):
    f=0.001
    delxn=n.x-g.x
    delyn=n.y-g.y
    delxs=s.x-g.x
    delys=s.y-g.y
    cp=np.abs(delxn*delys-delxs*delyn)
    if(d):
        alp= heuristicE(n)+(f)*cp
    else:
        alp= heuristicM(n)+(f)*cp
    return alp

#precomputing estimates of exact heuristics

class lm1:
    x=22
    y=17.8

class lm2:
    x=45.6
    y=33.9


def newh(n1,n2):
   return heuristicE(n1,n2)  #can be defined as per wish

def precomp(n,g,lm1,lm2):
    return newh(n,lm1)+heuristicM(lm1,lm2)+newh(lm2,g)


#cost function variation
def linestart(n):
    return W*((n.x-s.x)**2+(n.y-s.y)**2)

def cost(n):
    return linestart(n)

def modcost(n):
    p=0.2 #keep it between 0 and 1 always
    return 1+p*(cost(n)-1)