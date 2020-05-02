#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:14:23 2020

@author: Joshuabalbi
"""
#Import statements-------------------------------------------------------------
import numpy as np

#functions---------------------------------------------------------------------

#this function takes 6 parameters: S= # of susceptible I= # of infected
#R= # of recovered t = initial time B= beta and S = sigma. B and S will be
#explained in the variables section. this function just gets the change in 
#S I and R and outputs the new S I and R values adding on time which has a 
#stepsize of one
def change_graph(S, I, R, t, B, y):
    Si = -B*S*I
    Sf = S+Si
    Ii = B*Sf*I-y*I
    If = I+Ii
    Ri = y*If
    Rf = R+Ri
    Tf = t + 1
    return Sf, If, Rf, Tf

#the itetare function takes the same parameters are change_graph and what it 
#is basically doing is iterating change_graph function  200 times in order to 
#attain a curve from all of the values attained.
def iterate_SIR(S, I, R, t, B, y):
    G=[S, I, R, t]
    for i in range(0, 200):
        S1, I1, R1, T1= change_graph(S, I, R, t, B, y)
        G+=S1, I1, R1, T1
        S, I, R, t = S1, I1, R1, T1
    return G

#the infected ratio function is used in order to attain a susceptible 
#and a infected value from 0 to 1 using ratios of the whole population 
#over one infected
def infected_ratio(p):
    I=1/p
    S=(p-1)/p
    return I,S

#this list is a b amount of lists in a list. it has two parameters b and p
#b is the amount of beta you want ranging from 0-1 with a stepsize of 1/b. 
#it uses the function iterate with every beta in a forloop and prints out 
#every infection curve in the range of 0-1. sigma is constant
def B_list(b):
    B=[]
    for i in range(0,b):
        list_I=(iterate_SIR(S, I, R, t, (i+1)/b, 1/b)[1::4])
        B.append(list_I)
    return B

#this list is a y amount of lists in a list. it has two parameters y and p
#y is the amount of sigma you want ranging from 0-1 with a stepsize of 1/y. 
#it uses the function iterate with every sigma in a forloop and prints out 
#every infection curve in the range of 0-1. beta is constant
def Y_list(y):
    Y=[]
    for i in range(0,y):
        list_I=(iterate_SIR(S, I, R, t, 14/14, (i+1)/y)[1::4])
        Y.append(list_I)
    return Y

#peaks is used in order to find the maximum of each infected graph.
#we use np.meshgrid and 3d graph in matplotlib in order to run every
#combination of beta and sigma possible.
def peak(x, y):
    return max(iterate_SIR(S, I, R, t, x, y)[1::4])
