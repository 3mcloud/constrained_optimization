import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_64(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2', 'x3']

        # # use constraints from the problem as the bounds - had to make up uppper bound
    
        x1_min =  1e-5
        x1_max = 500.0

        x2_min =  1e-5
        x2_max = 500.0

        x3_min =  1e-5
        x3_max = 500.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max), (x3_min, x3_max)]

        self.output_labels = ["objective", "constraint1"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '<=', constraint]]
        
        #best_x --> (108.7347175, 85.12613942, 204.3247078)

        self.best_val = -6299.842428

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        
        obj = self._Objective(x1, x2, x3)
        cons1 = self._Constraint1(x1, x2, x3)

        return [obj, cons1]

    def _Objective(self, x1, x2, x3):
        func = 5.0*x1 + 50000.0/x1 + 20.0*x2 + 72000/x2 + 10.0*x3 + 144000.0/x3
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x1, x2, x3):
        cons = 1 - 4.0/x1 - 32.0/x2 - 120.0/x3
        return -cons
