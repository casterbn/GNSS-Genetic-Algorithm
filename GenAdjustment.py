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
MVC = np.loadtxt("MVC.txt", dtype = 'f')

class parameter:
    def __init__(self, A, LB, LO, MVC):
        self.A = A
        self.LB = LB
        self.LO = LO
        self.MVC = MVC
        
    def X_parameters(self):       
        print(self.A)
        
matrices = parameter(A, LB, LO, MVC)
matrices.X_parameters()