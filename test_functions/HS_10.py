import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_10(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        # make up bounds

        x1_min = -10.0 
        x1_max =  10.0

        x2_min = -10.0
        x2_max =  10.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '>=', constraint]]
        
        #best_x --> (0.0, 1.0)

        self.best_val = 1.0

    def evaluate(self, x):
        obj = self._Objective(x)
        cons1 = self._Constraint1(x)

        return [obj, cons1]

    def _Objective(self, x):
        func = x[0] - x[1]
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x):
        cons = -3.0*x[0]**2 + 2.0*x[0]*x[1] - x[1]**2 + 1.0
        return cons
