



You should include in your final project readme a description of the project, a list of all the files that you have created and instructions for use.

This readme is written in a language called markdown. This is not a programming language but a formatting langauge. There are symbols (syntax) used to indicate how to format the text. For example the pound symbol (i.e. the hashtag) is used to format a title; two of the same symbol format a heading, and three format a sub-heading.

Below is some example text in markdown however this alone is not sufficient for the final project. **Make sure you follow the directions on Canvas.**

Delete the instructions above this line and the line:

---------------------------------------------

# SIR Model and Applications

SIR Models are models that are used to track the percentages of the population that are susceptible, infected, and recovered during a pandemic. We use SIR models to predict how long an epidemic will last and what percent of the total population will be infected. We could also manipulte the graphs to determine the effect of what beta and sigma are. this codes primary function is to illustrate how beta and sigma affect the infected curve. it is also used to compare between two different simulations, eulers method and monte carlo method.

## Instructions

the steps of use for the functions are pretty straight forward. for both drivers, you have 4 variables in common that must be entered:
- p: thre population desired, for the monte carlo simulation the higher the population the longer the run time
- beta: it is set at 3/14 but it is there for the user to be able to change.
- sigma: it is set at 1/14 but it is there for the user to be able to change.
- stepsize: it is set at 14 but it is there for the user to be able to change. stepsize determines how mnay steps from 0-1 are taken and how many graphs can made, the default is 14 but if wanting to do more or less must go nto code and either add or subtract plt.plot line and add either B[#], Ys[#] or BC[#], YC[#] depedning on the number of stepsizes and wether it is monte carlo or not. would not recomend changing

specific variables to the Eulers method simulation:
- R: set to zero as default do not recomend changing
- t: set to zero as default do not recomend changing

specific variables to the Monte Carlo method simulation:
- days: it is recomended for the days to remain at 200, you would have to go intop the code and change the 200 value in the forloop for the function mcpeaks to the value of days desired.

The main variables that are encouraged to change are p, beta and sigma, since that is what we are truly focusing on, the effects of beta and sigma on the percentage of the population infected. if you want to change other variables, changing the code will be necesary in order for it to run properly.

## File List
the repository contains four files not including the README.md, the files are the following:
- SIR_simulation.py: This file contains the functions for the Euler's approach and is made up of 6 functions. For description of the functions go to the file and read the commented section above the specific function.
- driver_SIR.py: the Euler driver file calls the functions from the SIR_simulation.py file and creates 4 different graphs that can be changed by changing the variables. For description in the code and each graph go to the file and read the commented section above the specific code.
- MC_simulation.py: This file contains the functions for the Monte Carlo approach and is made up of 10 functions. For description of the functions go to the file and read the commented section above the specific function.
- driver_MonteCarlo.py: the Monte Carlo driver file calls the functions from the MC_simulation.py file and creates 5 different graphs that can be changed by changing the variables. For description in the code and each graph go to the file and read the commented section above the specific code.

## Enjoy the simulation!!!
