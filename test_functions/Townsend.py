import numpy as np

class Townsend(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        x1_min = -2.25
        x1_max =  2.25
        x2_min = -2.25
        x2_max =  1.75

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1"]
        self.objective = self.output_labels[0]

        self.output_constraints = [['constraint1', '<=', 0.0]]

        # best_x -> (2.0052938, 1.1944509)
        self.best_val = 2.0239884

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]

        #print(x1)
        #print(x2)
        obj = self._Townsend(x1, x2)
        cons1 = self._Constraint(x1, x2)

        return [obj, cons1]

    def _Townsend(self, x1, x2):
        func = -(np.cos((x1 - 0.1)*x2))**2 - x1*np.sin(3.0*x1 + x2)
        return -func # Wiki assumes min - this makes it max

    def _Constraint(self, x1, x2):
        t = np.arctan2(x1,x2)
        cons = x1*x1 + x2*x2 - (2.0*np.cos(t) - 0.5*np.cos(2.0*t) - 0.25*np.cos(3.0*t) - 0.125*np.cos(4.0*t))**2 - (2.0*np.sin(t))**2 
        return cons
