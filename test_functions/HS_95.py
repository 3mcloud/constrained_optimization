import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_95(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']

        # use constraints from the problem as the bounds - made up uppper bound
    
        x1_min = 0.0
        x1_max = 0.31

        x2_min = 0.0
        x2_max = 0.046

        x3_min = 0.0
        x3_max = 0.068

        x4_min = 0.0
        x4_max = 0.042

        x5_min = 0.0
        x5_max = 0.028

        x6_min = 0.0
        x6_max = 0.0134

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max), (x3_min, x3_max), (x4_min, x4_max), (x5_min, x5_max), (x6_min, x6_max)]

        self.output_labels = ["objective", "constraint1", "constraint2", "constraint3", "constraint4"]

        self.objective = self.output_labels[0]
        cons_lo = 0.0
        self.output_constraints = [['constraint1', '>=', cons_lo], ['constraint2', '>=', cons_lo], ['constraint3', '>=', cons_lo], ['constraint4', '>=', cons_lo]]

        #best_x --> (0.0, 0.0, 0.0, 0.0, 0.0, 0.0033233033)

        self.best_val = -0.015619514

        self._b = [4.97, -1.88, -29.08, -78.02]

    def evaluate(self, x):
       
        obj = self._Objective(x)
        cons1 = self._Constraint1(x)
        cons2 = self._Constraint2(x)
        cons3 = self._Constraint3(x)
        cons4 = self._Constraint4(x)

        return [obj, cons1, cons2, cons3, cons4]

    def _Objective(self, x):
        func = 4.3*x[0] + 31.8*x[1] + 63.3*x[2] + 15.8*x[3] + 68.5*x[4] + 4.7*x[5]
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x):
        cons = 17.1*x[0] + 38.2*x[1] + 204.2*x[2] + 212.3*x[3] + 623.4*x[4] + 1495.5*x[5] - \
                169*x[0]*x[2] - 3580*x[2]*x[4] - 3810*x[3]*x[4] - 18500*x[3]*x[5] - \
                24300*x[4]*x[5] - self._b[0]
        return cons

    def _Constraint2(self, x):
        cons = 17.9*x[0] + 36.8*x[1] + 113.9*x[2] + 169.7*x[3] + 337.8*x[4] + 1385.2*x[5] - \
                139*x[0]*x[2] - 2450*x[3]*x[4] - 16600*x[3]*x[5] - 17200*x[4]*x[5] - self._b[1]
        return cons

    def _Constraint3(self, x):
        cons = -273*x[1] - 70*x[3] - 819*x[4] + 26000*x[3]*x[4] - self._b[2]
        return cons

    def _Constraint4(self, x):
        cons = 159.9*x[0] - 311*x[1] + 587*x[3] + 391*x[4] + 2198*x[5] - 14000*x[0]*x[5] - self._b[3]
        return cons
