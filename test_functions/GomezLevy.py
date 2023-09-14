import numpy as np

class GomezLevy(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        x1_min = -1.00
        x1_max =  0.75
        x2_min = -1.00
        x2_max =  1.00

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1"]
        self.objective = self.output_labels[0]

        self.output_constraints = [['constraint1', '<=', 0.0]]

        # best_x --> (0.08984201311218148, -0.7126564033520919)
        self.best_val = 1.031628453

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]

        #print(x1)
        #print(x2)
        obj = self._GomezLevy(x1, x2)
        cons1 = self._Constraint(x1, x2)

        return [obj, cons1]

    def _GomezLevy(self, x1, x2):
        func = 4.0*x1*x1 - 2.1*x1**4 + 1.0/3.0*x1**6 + x1*x2 - 4.0*x2*x2 + 4.0*x2**4
        return -func # Wiki assumes min - this makes it max

    def _Constraint(self, x1, x2):
        cons = -np.sin(4.0*np.pi*x1) + 2.0*(np.sin(2.0*np.pi*x2))**2 - 1.5
        return cons
