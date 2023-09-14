import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_86(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2', 'x3', 'x4', 'x5']

        # use constraints from the problem as the bounds - made up uppper bound
    
        x1_min = 0.0
        x1_max = 2.0

        x2_min = 0.0
        x2_max = 2.0

        x3_min = 0.0
        x3_max = 2.0

        x4_min = 0.0
        x4_max = 2.0

        x5_min = 0.0
        x5_max = 2.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max), (x3_min, x3_max), (x4_min, x4_max), (x5_min, x5_max)]

        self.output_labels = ["objective", "constraint1", "constraint2", "constraint3", "constraint4", "constraint5", 
                                           "constraint6", "constraint7", "constraint8", "constraint9", "constraint10"]
        self.objective = self.output_labels[0]
        cons_lo = 0.0
        self.output_constraints = [['constraint1', '>=', cons_lo], ['constraint2', '>=', cons_lo], ['constraint3', '>=', cons_lo], 
                                   ['constraint4', '>=', cons_lo], ['constraint5', '>=', cons_lo], ['constraint6', '>=', cons_lo],
                                   ['constraint7', '>=', cons_lo], ['constraint8', '>=', cons_lo], ['constraint9', '>=', cons_lo], ['constraint10', '>=', cons_lo]]
        
        #best_x --> (0.3, 0.33346761, 0.4, 0.42831010, 0.22396487)

        self.best_val = 32.34867897

        self._a = [[-16,  2, 0, 1, 0],
                   [  0, -2, 0, 0.4, 2],
                   [-3.5, 0, 2, 0, 0],
                   [0, -2, 0, -4, -1],
                   [0, -9, -2, 1,-2.8],
                   [2, 0, -4, 0, 0],
                   [-1, -1, -1, -1, -1],
                   [-1, -2, -3, -2, -1],
                   [1, 2, 3, 4, 5],
                   [1, 1, 1, 1, 1]]

        self._c = [[30, -20, -10, 32, -10],
                   [-20, 39,  -6, -31, 32],
                   [-10, -6,  10,  -6, -10],
                   [32, -31, -6, 39, -20],
                   [-10,  32, -10, -20 , 30]]

        self._e = [-15, -27, -36, -18, -12]

        self._d = [4, 8, 10, 6, 2]

        self._b = [-40, -2, -0.25, -4, -4, -1, -40, -60, 5, 1]

    def evaluate(self, x):
       
        obj = self._Objective(x)
        ret = [obj]
        for i in range(10):
            ret.append(self._Constraint(x, i))

        return ret

    def _Objective(self, x):
        n = 5
        func =   0.0
        
        for j in range(n):
            func += self._e[j] * x[j]
            
        for i in range(n):
            for j in range(n):
                func += self._c[i][j] * x[i]*x[j]
        for j in range(n):
            func += self._d[j] * x[j]**3

        return -func # paper assumes min - this makes it max

    def _Constraint(self, x, i):
        cons = 0.0
        for j in range(5):
            cons += self._a[i][j] * x[j] 
        cons -= self._b[i]
        return cons
