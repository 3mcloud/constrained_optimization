import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_31(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2', 'x3']

        # use constraints from the problem as the bounds

        x1_min = -10.0 
        x1_max =  10.0

        x2_min =  1.0
        x2_max =  10.0

        x3_min = -10.0
        x3_max =   1.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max), (x3_min, x3_max)]

        self.output_labels = ["objective", "constraint1"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '>=', constraint]]
        
        #best_x --> (1/np.sqrt(3), 1/np.sqrt(3), 0.0)

        self.best_val = -6.0

    def evaluate(self, x):

        obj = self._Objective(x)
        cons1 = self._Constraint1(x)

        return [obj, cons1]

    def _Objective(self, x):
        func = 9.0*x[0]*x[0] + x[1]*x[1] + 9.0*x[2]*x[2]
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x):
        cons = x[0]*x[1] - 1.0
        return cons
