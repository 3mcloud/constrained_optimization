import numpy as np
from numpy import pi

from test_functions.HS_95 import HS_95

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_98(HS_95):
    
    def __init__(self):
        super(HS_98, self).__init__() # call initilizer from base class

        #best_x --> (0.2685649, 0.0, 0.0, 0.0, 0.28, 0.0134)

        self.best_val = -3.1358091

        # redefine b array 
        self._b = [32.97, 25.12, -124.08, -173.02]

