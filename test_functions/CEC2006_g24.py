import numpy as np
from numpy import pi

class CEC2006_g24(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        x1_min = 0.0 
        x1_max = 3.0
        x2_min = 0.0 
        x2_max = 4.0 

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1", "constraint2"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '<=', constraint], ['constraint2', '<=', constraint]]
        
        #best_x --> (2.32952019747762,3.17849307411774)
        self.best_val = 5.50801327159536

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]

        #print(x1)
        #print(x2)
        obj = self._Objective(x1, x2)
        cons1 = self._Constraint1(x1, x2)
        cons2 = self._Constraint2(x1, x2)

        return [obj, cons1, cons2]

    def _Objective(self, x1, x2):
        func = -x1 - x2
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x1, x2):
        cons = -2.0*x1**4 + 8.0*x1**3 - 8.0*x1**2 + x2 -2
        return cons

    def _Constraint2(self, x1, x2):
        cons = -4.0*x1**4 + 32.0*x1**3 - 88.0*x1**2 + 96.0*x1 + x2 - 36
        return cons
