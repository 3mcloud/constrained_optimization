import numpy as np
from numpy import pi

from test_functions.HS_95 import HS_95

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_96(HS_95):
    
    def __init__(self):
        super(HS_96, self).__init__() # call initilizer from base class

        # redefine b array 
        self._b = [4.97, -1.88, -69.08, -118.02]

        # solution is the same as #95
