import numpy as np
from numpy import pi

class Mystery(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        x1_min = 0.0 
        x1_max = 5.0
        x2_min = 0.0 
        x2_max = 5.0 

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1"]
        self.objective = self.output_labels[0]

        self.output_constraints = [['constraint1', '<=', 0.0]]

        # best_x -> (2.7449510467778606, 2.3522519650791365)
        self.best_val =  1.1742743288663506

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]

        #print(x1)
        #print(x2)
        obj = self._MysteryFunc(x1, x2)
        cons1 = self._MysteryConstraint(x1, x2)

        return [obj, cons1]

    def _MysteryFunc(self, x1, x2):
        func = 2.0 + 0.01*(x2 - x1*x1)**2 + (1.0 - x1)**2 + 2*(2-x2)**2 + 7.0*np.sin(0.5*x1)*np.sin(0.7*x1*x2)
        return -func # paper assumes min - this makes it max

    def _MysteryConstraint(self, x1, x2):
        cons = -np.sin(x1 - x2 - pi/8.0)
        return cons
