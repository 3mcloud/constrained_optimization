import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_65(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2', 'x3']

        # # use constraints from the problem as the bounds
    
        x1_min =  -4.5
        x1_max =   4.5

        x2_min =  -4.5
        x2_max =   4.5

        x3_min =  -5.0
        x3_max =   5.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max), (x3_min, x3_max)]

        self.output_labels = ["objective", "constraint1"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '<=', constraint]]
        
        #best_x --> (3.650461821, 3.65046168, 4.6204170507)

        self.best_val = -0.9535288567

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        
        obj = self._Objective(x1, x2, x3)
        cons1 = self._Constraint1(x1, x2, x3)

        return [obj, cons1]

    def _Objective(self, x1, x2, x3):
        func = (x1 - x2)**2 + (x1 + x2 - 10.0)**2/9.0 + (x3 - 5.0)**2
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x1, x2, x3):
        cons = 48.0 - x1*x1 - x2*x2 - x3*x3
        return -cons
