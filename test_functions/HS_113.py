import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_113(object):
    
    def __init__(self):

        self.x_labels = ['x%d' % n for n in range(1,11)]

        # made up range -

        x_min =  0.0
        x_max = 10.0

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
        x10_min = x_min
        x10_max = x_max

        self.bounds = [(x1_min, x1_max), (x2_min, x2_max), (x3_min, x3_max), (x4_min, x4_max), (x5_min, x5_max), 
                       (x6_min, x6_max), (x7_min, x7_max), (x8_min, x8_max), (x9_min, x9_max), (x10_min, x10_max)]

        self.output_labels = ["objective"  , "constraint1", "constraint2", "constraint3", "constraint4", "constraint5", "constraint6",
                              "constraint7", "constraint8"]

        self.objective = self.output_labels[0]
        cons_lo = 0.0
        self.output_constraints = [['constraint%d' % n, '>=', cons_lo] for n in range(1,9)]

        #best_x --> (2.171996, 2.363683, 8.773926, 5.095984, 0.0006548, 1.430574, 1.321644, 9.828726, 8.280092, 8.375927)

        self.best_val = -24.3062091

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


        return [obj, cons1, cons2, cons3, cons4, cons5, cons6, cons7, cons8]

    def _Objective(self, x):
        func = x[0]**2+x[1]**2 + x[0]*x[1] - 14*x[0] - 16*x[1] + (x[2]-10)**2 + 4*(x[3]-5)**2 + \
              (x[4]-3)**2 + 2*(x[5]-1)**2 + 5*x[6]**2 + 7*(x[7]-11)**2 + 2*(x[8]-10)**2 + \
              (x[9]-7)**2 + 45
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x):
        cons = 105 - 4*x[0] -5*x[1] + 3*x[6] - 9*x[7]
        return cons

    def _Constraint2(self, x):
        cons = -10*x[0] + 8*x[1] + 17*x[6]-2*x[7]
        return cons

    def _Constraint3(self, x):
        cons = 8*x[0] - 2*x[1] - 5*x[8] + 2*x[9] + 12
        return cons

    def _Constraint4(self, x):
        cons = -3*(x[0]-2)**2 - 4*(x[1]-3)**2 - 2*x[2]**2 + 7*x[3] + 120
        return cons

    def _Constraint5(self, x):
        cons = -5*x[0]**2 - 8*x[1] - (x[2]-6)**2 + 2*x[3] + 40
        return cons

    def _Constraint6(self, x):
        cons = -0.5*(x[0]-8)**2 - 2*(x[1]-4)**2 - 3*x[4]**2 + x[5] + 30
        return cons

    def _Constraint7(self, x):
        cons = -x[0]**2 - 2*(x[1]-2)**2 + 2*x[0]*x[1] - 14*x[4] + 6*x[5]
        return cons

    def _Constraint8(self, x):
        cons = 3*x[0] - 6*x[1] - 12*(x[8]-8)**2 + 7*x[9]
        return cons

