#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:50:56 2020

@author: Joshuabalbi
"""
#Import statements-------------------------------------------------------------
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import SIR_simulation 

#variables---------------------------------------------------------------------
#some variables carry over from one graph to the other   

#this is the variables for simulation SIR model
I,S=infected_ratio(100000)
R=0
t=0
beta =3/14
sigma=1/14
list_S=(iterate_SIR(S, I, R, t, beta, sigma)[0::4])
list_I=(iterate_SIR(S, I, R, t, beta, sigma)[1::4])
list_R=(iterate_SIR(S, I, R, t, beta, sigma)[2::4])
list_t=(iterate_SIR(S, I, R, t, beta, sigma)[3::4])

#this is the variable for the infected curves.
B=(B_list(14))  
Ys=(Y_list(14)) 

#these are the variables for the Monte Carlo peak graph
Stepsize=14
s=Stepsize
x = np.linspace(1/s, 1, s)
y = np.linspace(1/s, 1, s)
X, Y = np.meshgrid(x,y)
peak_vectorized = np.vectorize(peak)
Z = peak_vectorized(X, Y)

#code--------------------------------------------------------------------------

#this code makes a graph of the Simulation SIR Model with a set population 
#beta and sigma that the user can change based on his or her need
plt.plot(list_t,list_S, label= "suseptible")
plt.plot(list_t,list_I, label= "infected")
plt.plot(list_t,list_R, label= "recovered")
plt.legend(loc= "upper right")
plt.xlabel('days')
plt.ylabel('population')
plt.title('Basic SIR graph simulation')
plt.show()

#this is a set of infected curves that has beta as a variable and sigma 
#as a constant
plt.plot(list_t,B[0], label= "infected 1")
plt.plot(list_t,B[1], label= "infected 2")
plt.plot(list_t,B[2], label= "infected 3")
plt.plot(list_t,B[3], label= "infected 4")
plt.plot(list_t,B[4], label= "infected 5")
plt.plot(list_t,B[5], label= "infected 6")
plt.plot(list_t,B[6], label= "infected 7")
plt.plot(list_t,B[7], label= "infected 8")
plt.plot(list_t,B[8], label= "infected 9")
plt.plot(list_t,B[9], label= "infected 10")
plt.plot(list_t,B[10], label= "infected 11")
plt.plot(list_t,B[11], label= "infected 12")
plt.plot(list_t,B[12], label= "infected 13")
plt.plot(list_t,B[13], label= "infected 14")
plt.legend(loc= "upper right")
plt.xlabel('days')
plt.ylabel('population')
plt.title('infected curve changing beta')
plt.show()

#this is a set of infected curves that has sigma as a variable and beta 
#as a constant
plt.plot(list_t,Ys[0], label= "infected 1")
plt.plot(list_t,Ys[1], label= "infected 2")
plt.plot(list_t,Ys[2], label= "infected 3")
plt.plot(list_t,Ys[3], label= "infected 4")
plt.plot(list_t,Ys[4], label= "infected 5")
plt.plot(list_t,Ys[5], label= "infected 6")
plt.plot(list_t,Ys[6], label= "infected 7")
plt.plot(list_t,Ys[7], label= "infected 8")
plt.plot(list_t,Ys[8], label= "infected 9")
plt.plot(list_t,Ys[9], label= "infected 10")
plt.plot(list_t,Ys[10], label= "infected 11")
plt.plot(list_t,Ys[11], label= "infected 12")
plt.plot(list_t,Ys[12], label= "infected 13")
plt.plot(list_t,Ys[13], label= "infected 14")
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
