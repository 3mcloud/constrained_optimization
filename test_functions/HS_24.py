import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_24(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        # use constraints as bounds - made up upper bounds

        x1_min =  0.0
        x1_max =  6.0

        x2_min =  0.0
        x2_max =  6.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1", "constraint2", "constraint3"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '>=', constraint], ['constraint2', '>=', constraint], ['constraint3', '>=', constraint]]
        
        #best_x --> (3.0, np.sqrt(3.0))

        self.best_val = 1.0

    def evaluate(self, x):
        obj = self._Objective(x)
        cons1 = self._Constraint1(x)
        cons2 = self._Constraint2(x)
        cons3 = self._Constraint3(x)
        return [obj, cons1, cons2, cons3]

    def _Objective(self, x):
        func = ((x[0] - 3)**2 - 9) * x[1]**3 / (27*np.sqrt(3))
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x):
        cons = x[0]/np.sqrt(3) - x[1]
        return cons

    def _Constraint2(self, x):
        cons = x[0] + np.sqrt(3)*x[1]
        return cons

    def _Constraint3(self, x):
        cons = -x[0] - np.sqrt(3)*x[1] + 6
        return cons
