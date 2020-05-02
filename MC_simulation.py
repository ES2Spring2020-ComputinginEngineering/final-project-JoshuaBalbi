#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:00:39 2020

@author: Joshuabalbi
"""
#Import statements-------------------------------------------------------------
import numpy as np
import random as random
import pandas as pd

#functions---------------------------------------------------------------------

#array_length takes the total amount of people and makes a table with 
#columns named susceptible, infected, recovered. the susceptible cloumn
#has 1 going down through it and the other two have zeros.
def array_length(p):
    d = pd.DataFrame(1, index=np.arange(p), columns=["Susceptible"])
    e = pd.DataFrame(0, index=np.arange(p), columns=["infected"])
    f = pd.DataFrame(0, index=np.arange(p), columns=["recovered"])
    h = pd.concat([d,e,f], axis = 1, join= "inner")
    return h

#radnom infected radnomly chooses a number from 0 to p-1 in order to get
#a random person that got infected.
def random_infection(p):
    I=random.randint(0,p-1)
    return I 

#simple returns a pandas array size p X 3 that has all susceptible labeled 
#as one except for one which is labeled 0 and where it is labelled zero 
#infected is labeled 1
def simple(p):
    h=array_length(p)
    I=random_infection(p)
    h.at[I,"Susceptible"] = 0
    h.at[I,"infected"] = 1
    return h

#what update does is it gets updates the pandas array and changes the 
#suceptible who get randomly infected to infected and the infected that
#randomly reover to recovered with ones and zeros. it takes four parameters
#h being the original simple function returning an array. p is tbe population
#b and y are beta and sigma respectively.
def update(h,p,b,y):
    T= h['infected'].sum()
    I=[]
    J=[]
    q=[]
    for i in range(0,T):
        if b > random.uniform(0,1):
            q.append(random_infection(p))
    for i in q:
        if h["Susceptible"][i]==1:
            I.append(i)
    for i in I:
        h.at[i,"Susceptible"] = 0
        h.at[i,"infected"] = 1
    K=h[h["infected"]==1].index
    for i in K:
        if y > random.uniform(0,1):
            J.append(i)
    for i in J:
        h.at[i,"infected"] = 0
        h.at[i,"recovered"] = 1
    return h

#iterate function takes the same parameters as update with an exception of the 
#m or the amount of days that you want the update function to iterate. the 
#iterate function updates the function  and then takes the sum of each array 
#and appends each array length tp its respected new list of lengths
def iterate_MC(p,b,y,m):
    h=simple(p)
    S_list=[h['Susceptible'].sum()]
    I_list=[h['infected'].sum()]
    R_list=[h['recovered'].sum()]
    T_list=[0]
    for j in range(0,m):
        H=update(h,p,b,y)
        s=H['Susceptible'].sum()
        i=H['infected'].sum()
        r=H['recovered'].sum()
        S_list.append(s)
        I_list.append(i)
        R_list.append(r)
        T_list.append(j+1)
        h=H
    return S_list,I_list,R_list,T_list

#convert is a simple function that converts a list into integers ranging from
#0 to 1 this is used in order to compare the graphs from monte carlo to the 
#graphs in the simulated SIR Model   
def convert(lst,p): 
    C=[]
    for i in lst:
        C.append(i/p)
    return C

#what the function does it just repeats the function iterate n amount of times
#and then retunrs a list of lists containing the infected curve and it is used
#to notice the variation of the monte carlo simulation
def infcurve(p,b,y):
    Inflist=[]
    for i in range(0,10):
        S_list,I_list,R_list,T_list =iterate_MC(p,b,y,200)
        C=convert(I_list,p)
        Inflist.append(C)
    return Inflist

#this list is a b amount of lists in a list. it has two parameters b and p
#b is the amount of beta you want ranging from 0-1 with a stepsize of 1/b. 
#it uses the function iterate with every beta in a forloop and prints out 
#every infection curve in the range of 0-1. sigma is constant
def B_listC(b,p):
    BC=[]
    for i in range(0,b):
        S_list,I_list,R_list,T_list=iterate_MC(p,i+1/14,1/14,200)
        B=[]
        for j in I_list:
            B.append(j/p)
        BC.append(B)
    return BC

#this list is a y amount of lists in a list. it has two parameters y and p
#y is the amount of sigma you want ranging from 0-1 with a stepsize of 1/y. 
#it uses the function iterate with every sigma in a forloop and prints out 
#every infection curve in the range of 0-1. beta is constant
def Y_listC(y,p):
    YC=[]
    for i in range(0,y):
        S_list,I_list,R_list,T_list=iterate_MC(p,14/14,i+1/14,200)
        Y=[]
        for j in I_list:
            Y.append(j/p)
        YC.append(Y)
    return YC  

#mc peaks is used in order to find the maximum of each infected graph
#we use np.meshgrid and 3d graph in matplotlib in order to run every
#combination of beta and sigma possible.
def mcpeak(x, y):
    S_list,I_list,R_list,T_list=iterate_MC(100000,x,y,200)
    Ilist=convert(I_list,100000)
    return max(Ilist)

