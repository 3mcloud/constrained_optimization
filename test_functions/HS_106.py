import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_106(object):
    
    def __init__(self):

        self.x_labels = ['x%d' % n for n in range(1,9)]

        # use constraints as bounds

        x1_min =   100.0
        x1_max = 10000.0

        x_min =  1000.0
        x_max = 10000.0

        x2_min = x_min
        x2_max = x_max
        x3_min = x_min
        x3_max = x_max

        x_min =   10.0
        x_max = 1000.0

        x4_min = x_min
        x4_max = x_max
        x5_min = x_min
        x5_max = x_max
        x6_min = x_min
        x6_max = x_max
        x7_min = x_min
        x7_max = x_max
        x8_min = x_min
        x8_max = x_max

        self.bounds = [(x1_min, x1_max), (x2_min, x2_max), (x3_min, x3_max), (x4_min, x4_max), 
                       (x5_min, x5_max), (x6_min, x6_max), (x7_min, x7_max), (x8_min, x8_max)]

        self.output_labels = ["objective"  , "constraint1", "constraint2", "constraint3", "constraint4", "constraint5", "constraint6"]
        
        self.objective = self.output_labels[0]
        cons_lo = 0.0
        self.output_constraints = [['constraint%d' % n, '>=', cons_lo] for n in range(1,7)]

        #best_x --> (579.3167, 1359.943, 5110.071, 182.0174, 295.5985, 217.9799, 286.4162, 395.5979)
        
        self.best_val = -7049.330923

    def evaluate(self, x):
       
        obj = self._Objective(x)
        cons1 = self._Constraint1(x)
        cons2 = self._Constraint2(x)
        cons3 = self._Constraint3(x)
        cons4 = self._Constraint4(x)
        cons5 = self._Constraint5(x)
        cons6 = self._Constraint6(x)

        return [obj, cons1, cons2, cons3, cons4, cons5, cons6]

    def _Objective(self, x):
        func = x[0] + x[1] + x[2]
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x):
        a = 0.0025
        cons = 1 - a * (x[3] + x[5])
        return cons

    def _Constraint2(self, x):
        a = 0.0025
        cons = 1 - a * (x[4] + x[6] - x[3])
        return cons

    def _Constraint3(self, x):
        b = 0.01
        cons = 1 - b * (x[7] - x[4])
        return cons

    def _Constraint4(self, x):
        c = 833.3325
        d = 100.0
        e = 83333.33
        cons = x[0] * x[5] - c * x[3] - d * x[0] + e
        return cons

    def _Constraint5(self, x):
        f = 1250.0
        cons = x[1] * x[6] - f * x[4] - x[1] * x[3] + f * x[3]
        return cons

    def _Constraint6(self, x):
        g = 1250000
        h = 2500
        cons = x[2] * x[7] - g - x[2] * x[4] + h * x[4]
        return cons
