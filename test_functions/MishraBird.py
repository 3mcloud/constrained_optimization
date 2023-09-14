import numpy as np

class MishraBird(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        x1_min = -10.0 
        x1_max =  0.0
        x2_min = -6.5 
        x2_max =  0.0 

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1"]
        self.objective = self.output_labels[0]

        self.output_constraints = [['constraint1', '<=', 0.0]]

        # best_x -> (-3.1302468062306525, -1.5821421771703572)
        self.best_val = 106.7645367

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]

        #print(x1)
        #print(x2)
        obj = self._MishraBird(x1, x2)
        cons1 = self._Constraint(x1, x2)

        return [obj, cons1]

    def _MishraBird(self, x1, x2):
        func = np.sin(x2)*np.exp((1.0-np.cos(x1))**2) + np.cos(x1)*np.exp((1.0-np.sin(x2))**2) + (x1 - x2)**2
        return -func # paper assumes min - this makes it max

    def _Constraint(self, x1, x2):
        cons = (x1 + 5.0)**2 + (x2 + 5.0)**2 - 25.0
        return cons
