# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 21:16:38 2018

@author: Eduardo Answer <eduardonzinga111@hotmail.com>
"""

"""
This programm is an implementation of Genetic Algorithm applied to Geodetic
Networks Adjustment
"""

import matplotlib as plt
import math
import pandas as pd
try:
    import numpy as np
except ImportError:
    print("Numpy is not installed")
from numpy import random

A = np.loadtxt("A.txt", dtype = 'f')
LB = np.loadtxt("LB.txt", dtype  = 'f')
LO = np.loadtxt("LO.txt", dtype = 'f')
MVC = np.loadtxt("MVC.txt", dtype = 'float64')
L = LB - LO
L[0] = L[0] + 2
L[5] = L[5] + 3
P = np.linalg.inv(MVC)
w = []
c = 1

class parameter:
    def __init__(self, A, L, P):
        self.A = A
        self.L = L        
        self.P = P
        
    def X_parameters(self):
        self.A = A
        self.L = L
        self.P = P
        X_1 = np.dot(np.dot(A.transpose(), P), A)
        X_1 = np.linalg.inv(X_1)
        X_2 = np.dot(np.dot(A.transpose(), P), L)
        X = np.dot(X_1, X_2)
        return X #parameters vector
    def residuals(self):
        self.A = A
        self.L = L
        x = self.X_parameters()
        V = np.dot(A, x)
        V = np.subtract(V,L)
        return V #residuals vector
    def LMS(self):
        v = self.residuals().copy()
        vlms = self.residuals()
        vlms = np.mean(vlms**2)
        std = c*np.sqrt(vlms)
        for n in v:
            if np.abs(n/std)<=2.5:
                w.append(1)
            elif np.abs(n/std)>2.5:
                w.append(0) 
        v = v**2
        result = np.dot(w,v)
                    
        return vlms, w, result
    def LTS(self):
        vlts = self.residuals()
        vlts = vlts**2
        vlts = np.sort(vlts)
        order = vlts.copy()
        vlts = np.sum(vlts)
        return vlts, order
    
        
        
matrices = parameter(A, L, P)
x = matrices.X_parameters()
v = matrices.residuals()
lms, p, result = matrices.LMS()
lts, order = matrices.LTS()

print(f'LMS: {lms}')
print(f'LTS: {lts}')














