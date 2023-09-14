import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_108(object):
    
    def __init__(self):

        self.x_labels = ['x%d' % n for n in range(1,10)]

        # made up range - only a lower bound on x9 is given

        x_min = 0.0
        x_max = 2.0

        x1_min = x_min
        x1_max = x_max
        x2_min = x_min
        x2_max = x_max
        x3_min = x_min
        x3_max = x_max
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
        x9_min = x_min
        x9_max = x_max

        self.bounds = [(x1_min, x1_max), (x2_min, x2_max), (x3_min, x3_max), (x4_min, x4_max), 
                       (x5_min, x5_max), (x6_min, x6_max), (x7_min, x7_max), (x8_min, x8_max), (x9_min, x9_max)]

        self.output_labels = ["objective"  , "constraint1", "constraint2", "constraint3", "constraint4", "constraint5", "constraint6",
                              "constraint7", "constraint8", "constraint9", "constraint10", "constraint11", "constraint12", "constraint13"]

        self.objective = self.output_labels[0]
        cons_lo = 0.0
        self.output_constraints = [['constraint%d' % n, '>=', cons_lo] for n in range(1,14)]

        #best_x --> (0.8841292, 0.4672425, 0.03742076, 0.9992996, 0.8841292, 0.4672425, 0.03742076, 0.9992996, 0.0)

        self.best_val = 0.8660254038

    def evaluate(self, x):
       
        obj = self._Objective(x)
        cons1 = self._Constraint1(x)
        cons2 = self._Constraint2(x)
        cons3 = self._Constraint3(x)
        cons4 = self._Constraint4(x)
        cons5 = self._Constraint5(x)
        cons6 = self._Constraint6(x)
        cons7 = self._Constraint7(x)
        cons8 = self._Constraint8(x)
        cons9 = self._Constraint9(x)
        cons10 = self._Constraint10(x)
        cons11 = self._Constraint11(x)
        cons12 = self._Constraint12(x)
        cons13 = self._Constraint13(x)

        return [obj, cons1, cons2, cons3, cons4, cons5, cons6, cons7, cons8, cons9, cons10, cons11, cons12, cons13]

    def _Objective(self, x):
        func = -0.5*(x[0]*x[3]-x[1]*x[2]+x[2]*x[8]-x[4]*x[8]+x[4]*x[7]-x[5]*x[6])
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x):
        cons = 1.0 - x[2]**2-x[3]**2
        return cons

    def _Constraint2(self, x):
        cons = 1.0 - x[4]**2-x[5]**2
        return cons

    def _Constraint3(self, x):
        cons = 1.0 - x[8]**2
        return cons

    def _Constraint4(self, x):
        cons = 1.0 - x[0]**2 - (x[1]-x[8])**2
        return cons

    def _Constraint5(self, x):
        cons = 1.0 - (x[0]-x[4])**2 - (x[1]-x[5])**2
        return cons

    def _Constraint6(self, x):
        cons = 1.0 - (x[0]-x[6])**2-(x[1]-x[7])**2
        return cons

    def _Constraint7(self, x):
        cons = 1.0 - (x[2]-x[6])**2 - (x[3]-x[7])**2
        return cons

    def _Constraint8(self, x):
        cons = 1.0 - (x[2]-x[4])**2-(x[3]-x[7])**2
        return cons

    def _Constraint9(self, x):
        cons = 1.0 - x[6]**2-(x[7]-x[8])**2
        return cons

    def _Constraint10(self, x):
        cons = x[0]*x[3] - x[1]*x[2]
        return cons

    def _Constraint11(self, x):
        cons = x[2]*x[8]
        return cons

    def _Constraint12(self, x):
        cons = -x[4]*x[8]
        return cons

    def _Constraint13(self, x):
        cons = x[4]*x[7] - x[5]*x[6]
        return cons
