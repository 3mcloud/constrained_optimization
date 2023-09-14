import numpy as np

class Simionescu(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        x1_min = -1.25
        x1_max =  1.25
        x2_min = -1.25
        x2_max =  1.25

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1"]
        self.objective = self.output_labels[0]

        self.output_constraints = [['constraint1', '<=', 0.0]]

        # best_x --> (+/-0.8485281335497322, -/+0.8485281412979818)
        self.best_val = 0.072

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]

        #print(x1)
        #print(x2)
        obj = self._Simionescu(x1, x2)
        cons1 = self._Constraint(x1, x2)

        return [obj, cons1]

    def _Simionescu(self, x1, x2):
        func = 0.1*x1*x2
        return -func # Wiki assumes min - this makes it max

    def _Constraint(self, x1, x2):
        r_T = 1.0
        r_S = 0.2
        n   = 8
        cons = x1*x1 + x2*x2 - (r_T + r_S*np.cos(n*np.arctan(x1/x2)))**2
        return cons
