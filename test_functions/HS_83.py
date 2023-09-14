import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_83(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2', 'x3', 'x4', 'x5']

        # # use constraints from the problem as the bounds
    
        x1_min =  78.0
        x1_max = 102.0

        x2_min = 33.0
        x2_max = 45.0

        x3_min = 27.0
        x3_max = 45.0

        x4_min = 27.0
        x4_max = 45.0

        x5_min = 27.0
        x5_max = 45.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max), (x3_min, x3_max), (x4_min, x4_max), (x5_min, x5_max)]

        self.output_labels = ["objective", "constraint1", "constraint2", "constraint3", "constraint4", "constraint5", "constraint6"]
        self.objective = self.output_labels[0]
        cons_lo = 0.0
        cons4hi = 92.0
        cons5hi = 20.0
        cons6hi =  5.0
        self.output_constraints = [['constraint1', '>=', cons_lo], ['constraint2', '>=', cons_lo], ['constraint3', '>=', cons_lo], 
                                   ['constraint4', '<=', cons4hi], ['constraint5', '<=', cons5hi], ['constraint6', '<=', cons6hi]]
        
        #best_x --> (78.0, 33.0, 29.99526, 45.0, 36.77581)

        self.best_val = 30665.53867

        self._a = [85.334407, 0.0056858, 0.0006262, 0.0022053, 80.51249, 0.0071317, 0.0029955, 0.0021813, 9.300961, 0.0047026, 0.0012547, 0.0019085]

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        x4 = x[3]
        x5 = x[4]        
        
        obj = self._Objective(x1, x2, x3, x4, x5)
        cons1 = self._Constraint1(x1, x2, x3, x4, x5)
        cons2 = self._Constraint2(x1, x2, x3, x4, x5)
        cons3 = self._Constraint3(x1, x2, x3, x4, x5)
        # constrains 4-6 are same function as 1-3
        cons4 = self._Constraint1(x1, x2, x3, x4, x5)
        cons5 = self._Constraint2(x1, x2, x3, x4, x5)
        cons6 = self._Constraint3(x1, x2, x3, x4, x5)

        return [obj, cons1, cons2, cons3, cons4, cons5, cons6]

    def _Objective(self, x1, x2, x3, x4, x5):
        func = 5.3578547*x3**2 + 0.8356891*x1*x5 + 37.293239*x1 - 40792.141
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x1, x2, x3, x4, x5):
        cons = self._a[0] + self._a[1]*x2*x5 + self._a[2]*x1*x4 - self._a[3]*x3*x5
        return cons

    def _Constraint2(self, x1, x2, x3, x4, x5):
        cons = self._a[4] + self._a[5]*x2*x5 + self._a[6]*x1*x2 + self._a[7]*x3**2 - 90.0
        return cons

    def _Constraint3(self, x1, x2, x3, x4, x5):
        cons = self._a[8] + self._a[9]*x3*x5 + self._a[10]*x1*x3 + self._a[11]*x3*x4 - 20.0
        return cons
