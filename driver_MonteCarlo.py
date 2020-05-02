#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:59:58 2020

@author: Joshuabalbi
"""
#Import statements-------------------------------------------------------------
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from MC_simulation import *

#variables---------------------------------------------------------------------
#some variables carry over from one graph to the other   

#this is the variables for Monte Carlo SIR model
#p value used in actual report is 100,000 but in order for it to run qukcker
#1,000 recomended
p=100
beta=3/14
sigma=1/14
days=200
S_list,I_list,R_list,T_list =iterate_MC(p,beta,sigma,days)
Slist=convert(S_list,p)
Ilist=convert(I_list,p)
Rlist=convert(R_list,p)

#this is the variable to find the infected curves of the same graph 
#iterated ten times through with both variables as constants
Inflist = infcurve(p,beta,sigma, days)

#this is the variable for the infected curves changing one variable and 
#leaving the other one constant.
Stepsize=14
s=Stepsize
BC = B_listC(s,p, days)
YC = Y_listC(s,p, days)

#these are the variables for the Monte Carlo peak graph
print("starting peaks 3d curve")
x = np.linspace(1/s, 1, s)
y = np.linspace(1/s, 1, s)
X, Y = np.meshgrid(x,y)
mcpeak_vectorized = np.vectorize(mcpeak)
Z = mcpeak_vectorized(X, Y, p, days)

#code--------------------------------------------------------------------------
#this code makes a graph of the Monte Carlo SIR Model with a set population 
#beta and sigma that the user can change based on his or her need
plt.plot(T_list,Slist, label= "suseptible")
plt.plot(T_list,Ilist, label= "infected")
plt.plot(T_list,Rlist, label= "recovered")
plt.legend(loc= "upper right")
plt.xlabel('days')
plt.ylabel('population')
plt.title('Basic SIR graph monte carlo')
plt.show()


#this code just repeats the same graph n amount of times and illustrates 
#the difference in the curves
plt.plot(T_list,Inflist[0], label= "infected 1")
plt.plot(T_list,Inflist[1], label= "infected 2")
plt.plot(T_list,Inflist[2], label= "infected 3")
plt.plot(T_list,Inflist[3], label= "infected 4")
plt.plot(T_list,Inflist[4], label= "infected 5")
plt.plot(T_list,Inflist[5], label= "infected 6")
plt.plot(T_list,Inflist[6], label= "infected 7")
plt.plot(T_list,Inflist[7], label= "infected 8")
plt.plot(T_list,Inflist[8], label= "infected 9")
plt.plot(T_list,Inflist[9], label= "infected 10")
plt.legend(loc= "upper right")
plt.xlabel('days')
plt.ylabel('population')
plt.title('infected curve variation')
plt.show()

#this is a set of infected curves that has beta as a variable and sigma 
#as a constant
plt.plot(T_list,BC[0], label= "infected 1")
plt.plot(T_list,BC[1], label= "infected 2")
plt.plot(T_list,BC[2], label= "infected 3")
plt.plot(T_list,BC[3], label= "infected 4")
plt.plot(T_list,BC[4], label= "infected 5")
plt.plot(T_list,BC[5], label= "infected 6")
plt.plot(T_list,BC[6], label= "infected 7")
plt.plot(T_list,BC[7], label= "infected 8")
plt.plot(T_list,BC[8], label= "infected 9")
plt.plot(T_list,BC[9], label= "infected 10")
plt.plot(T_list,BC[10], label= "infected 11")
plt.plot(T_list,BC[11], label= "infected 12")
plt.plot(T_list,BC[12], label= "infected 13")
plt.plot(T_list,BC[13], label= "infected 14")
plt.legend(loc= "upper right")
plt.xlabel('days')
plt.ylabel('population')
plt.title('infected curve changing beta')
plt.show()

#this is a set of infected curves that has sigma as a variable and beta 
#as a constant
plt.plot(T_list,YC[0], label= "infected 1")
plt.plot(T_list,YC[1], label= "infected 2")
plt.plot(T_list,YC[2], label= "infected 3")
plt.plot(T_list,YC[3], label= "infected 4")
plt.plot(T_list,YC[4], label= "infected 5")
plt.plot(T_list,YC[5], label= "infected 6")
plt.plot(T_list,YC[6], label= "infected 7")
plt.plot(T_list,YC[7], label= "infected 8")
plt.plot(T_list,YC[8], label= "infected 9")
plt.plot(T_list,YC[9], label= "infected 10")
plt.plot(T_list,YC[10], label= "infected 11")
plt.plot(T_list,YC[11], label= "infected 12")
plt.plot(T_list,YC[12], label= "infected 13")
plt.plot(T_list,YC[13], label= "infected 14")
plt.legend(loc= "upper right")
plt.xlabel('days')
plt.ylabel('population')
plt.title('infected curve changing sigma')
plt.show()

#this set of code allows us to 3d plot every point combination of different
#betas and sigmas and their peaks it uses the function mcpeaks and its 
#results X,Y,Z to accurately plot the peaks of every combination
fig = plt.figure(figsize=(10,5))
ax = plt.axes(projection="3d")
ax.plot_surface(Y, X, Z)
ax.set(xlabel="Sigma",ylabel="Beta",zlabel="population",title="infected peaks")
plt.show()
