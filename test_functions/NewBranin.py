import numpy as np
from numpy import pi

class NewBranin(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        x1_min = -5.0
        x1_max =  10.0
        x2_min =  0.0
        x2_max =  15.0    

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1"]
        self.objective = self.output_labels[0]

        self.output_constraints = [['constraint1', '<=', 0.0]]

        # best_x --> (3.2730237792921457, 0.04886975518980821)
        self.best_val = 268.78850467124704

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]

        #print(x1)
        #print(x2)
        obj = self._NewBraninFunc(x1, x2)
        cons1 = self._NewBraninConstraint(x1, x2)

        return [obj, cons1]

    def _NewBraninFunc(self, x1, x2):
        func = -(x1 - 10.0)**2 - (x2 - 15.0)**2
        return -func # paper assumes min - this makes it max

    def _NewBraninConstraint(self, x1, x2):
        cons = (x2 - 5.1/(4.0*pi**2)*x1**2 + 5.0/pi*x1 -6.0)**2 + 10.0*(1.0 - 1.0/(8.0*pi))*np.cos(x1) + 5.0
        return cons
