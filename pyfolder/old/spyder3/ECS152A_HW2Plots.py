# -*- coding: utf-8 -*-
"""
Spyder Editor

press cmd+I to get info about functions before the close parenthesis
OR type lib.func?
"""
#%%
#HW2 Problem 3
import matplotlib.pyplot as plt
import numpy as np

def stdDevN(rho):
    return np.sqrt(rho/((1-rho)**2))

def meanN(rho):
    return rho/(1-rho)

rhos = np.arange(0.1,1.0,0.1)
means = [meanN(r) for r in rhos]
stds = [stdDevN(r) for r in rhos]
plt.errorbar(rhos,means,yerr=stds)
plt.xlim([0,1]), plt.xlabel("Rho"), plt.ylabel("Mean & Std Dev of Pkts in Sys")
plt.show()

#%%
#HW2 Problem 4
from math import factorial

def choose(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def f(rho):
    return sum([choose(4,k)*rho**k*(1-rho)**(4-k) for k in range(2,5)])
"""can use scipy.misc.comb(4,k) instead without defining..."""

print('P_conj =',f(0.4))

