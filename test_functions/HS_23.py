import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_23(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        # use constraints as bounds

        x1_min = -50.0
        x1_max =  50.0

        x2_min = -50.0
        x2_max =  50.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1", "constraint2", "constraint3", "constraint4", "constraint5"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '>=', constraint], ['constraint2', '>=', constraint], ['constraint3', '>=', constraint], 
                                   ['constraint5', '>=', constraint], ['constraint5', '>=', constraint]]
        
        #best_x --> (1.0, 1.0)

        self.best_val = -2.0

    def evaluate(self, x):
        obj = self._Objective(x)
        cons1 = self._Constraint1(x)
        cons2 = self._Constraint2(x)
        cons3 = self._Constraint3(x)
        cons4 = self._Constraint4(x)
        cons5 = self._Constraint5(x)
        return [obj, cons1, cons2, cons3, cons4, cons5]

    def _Objective(self, x):
        func = x[0]**2 + x[1]**2
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x):
        cons = x[0] + x[1] - 1
        return cons

    def _Constraint2(self, x):
        cons = x[0]**2 + x[1]**2 - 1.0
        return cons

    def _Constraint3(self, x):
        cons = 9*x[0]**2 + x[1]**2 - 9.0
        return cons

    def _Constraint4(self, x):
        cons = x[0]**2 - x[1]
        return cons

    def _Constraint5(self, x):
        cons = x[1]**2 - x[0]
        return cons