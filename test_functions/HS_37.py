import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_37(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2', 'x3']

        # use constraints from the problem as the bounds

        x1_min = 0.0 
        x1_max = 42.0

        x2_min = 0.0
        x2_max = 42.0

        x3_min = 0.0
        x3_max = 42.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max), (x3_min, x3_max)]

        self.output_labels = ["objective", "constraint1", "constraint2"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '<=', constraint], ['constraint2', '<=', constraint]]
        
        #best_x --> (24, 12, 12)

        self.best_val = 3456

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        
        obj = self._Objective(x1, x2, x3)
        cons1 = self._Constraint1(x1, x2, x3)
        cons2 = self._Constraint2(x1, x2, x3)

        return [obj, cons1, cons2]

    def _Objective(self, x1, x2, x3):
        func = -x1*x2*x3
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x1, x2, x3):
        cons = 2.0*x3 + 2.0*x2 + x1 - 72.0
        return cons

    def _Constraint2(self, x1, x2, x3):
        cons = -x1 - 2.0*x2 - 2.0*x3
        return cons
