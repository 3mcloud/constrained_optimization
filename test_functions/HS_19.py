import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_19(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        # use constraints to set bounds 

        x1_min =  13.0
        x1_max = 100.0

        x2_min =   0.0
        x2_max = 100.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1", "constraint2"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '>=', constraint], ['constraint2', '>=', constraint]]
        
        #best_x --> (14.095, 0.84296079)

        self.best_val = 6961.81381

    def evaluate(self, x):
        obj = self._Objective(x)
        cons1 = self._Constraint1(x)
        cons2 = self._Constraint2(x)
        return [obj, cons1, cons2]

    def _Objective(self, x):
        func = (x[0] - 10)**3 + (x[1] - 20)**3
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x):
        cons = (x[0] - 5)**2 + (x[1] -5)**2 - 100.0
        return cons

    def _Constraint2(self, x):
        cons = 82.81 - (x[1] - 5)**2 - (x[0] - 6)**2  
        return cons
