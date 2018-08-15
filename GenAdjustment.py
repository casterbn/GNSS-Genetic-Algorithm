# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 21:16:38 2018

@author: Eduardo Answer
"""

"""
This programm is an implementation of Genetic Algorithm applied to Geodetic
Networks Adjustment
"""

import matplotlib as plt
import math

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
P = np.linalg.inv(MVC)

class parameter:
    def __init__(self, A, L, P):
        self.A = A
        self.L = L        
        self.P = P
        
    def X_parameters(self):
        self.A = A
        self.L = L
        self.P = P
        X_1 = np.dot(A.transpose(), P)
        X_1 = np.dot(X_1, A)
        X_1 = np.linalg.inv(X_1)
        X_2 = np.dot(A.transpose(), P)
        X_2 = np.dot(X_2, L)
        X = np.dot(X_1, X_2)
        return X #parameters vector
    def residuals(self):
        self.A = A
        self.L = L
        x = self.X_parameters()
        V = np.dot(A, x)
        VR = np.subtract(V,L)
        return VR #residuals vector
    def square_residuals(self):
        v = self.residuals()
        v = v**2
        v = v.sum()
        return v
        
        
matrices = parameter(A, L, P)
x = matrices.X_parameters().copy()
v = matrices.residuals().copy()
s = matrices.square_residuals().copy()














