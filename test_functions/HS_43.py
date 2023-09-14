import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_43(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2', 'x3', 'x4']

        # made up bounds based on the location of the solution
    
        x1_min = -5.0
        x1_max =  5.0

        x2_min = -5.0
        x2_max =  5.0

        x3_min = -5.0
        x3_max =  5.0

        x4_min = -5.0
        x4_max =  5.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max), (x3_min, x3_max), (x4_min, x4_max)]

        self.output_labels = ["objective", "constraint1", "constraint2", "constraint3"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '<=', constraint], ['constraint2', '<=', constraint], ['constraint3', '<=', constraint]]
        
        #best_x --> (0, 1, 2, -1)

        self.best_val = 44

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        x4 = x[3]
        
        obj = self._Objective(x1, x2, x3, x4)
        cons1 = self._Constraint1(x1, x2, x3, x4)
        cons2 = self._Constraint2(x1, x2, x3, x4)
        cons3 = self._Constraint3(x1, x2, x3, x4)
        
        return [obj, cons1, cons2, cons3]

    def _Objective(self, x1, x2, x3, x4):
        func = x1*x1 + x2*x2 + 2*x3*x3 + x4*x4 - 5.0*x1 - 5.0*x2 - 21.0*x3 + 7.0*x4  
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x1, x2, x3, x4):
        cons = 8.0 - x1*x1 - x2*x2 - x3*x3 - x4*x4 - x1 + x2 - x3 + x4  
        return -cons

    def _Constraint2(self, x1, x2, x3, x4):
        cons = 10.0 - x1*x1 - 2.0*x2*x2 - x3*x3 - 2.0*x4*x4 + x1 + x4
        return -cons

    def _Constraint3(self, x1, x2, x3, x4):
        cons = 5.0 - 2.0*x1*x1 - x2*x2 - x3*x3 - 2.0*x1 + x2 + x4
        return -cons
