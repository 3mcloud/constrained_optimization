import numpy as np

class TestFunction2(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        x1_min = 0.0 
        x1_max = 1.0
        x2_min = 0.0 
        x2_max = 1.0 

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1", "constraint2", "constraint3"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '<=', constraint], ['constraint2', '<=', constraint], ['constraint3', '<=', constraint]]

        # best_x -> (0.2016916891014569, 0.8331848610739362)
        self.best_val = 0.7483083108985432

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]

        #print(x1)
        #print(x2)
        obj = self._TestFunc2(x1, x2)
        cons1 = self._TestFunc2Constraint1(x1, x2)
        cons2 = self._TestFunc2Constraint2(x1, x2)
        cons3 = self._TestFunc2Constraint3(x1, x2)

        return [obj, cons1, cons2, cons3]

    def _TestFunc2(self, x1, x2):
        func = -(x1 - 1.0)**2 - (x2 - 0.5)**2
        return -func # paper assumes min - this makes it max

    def _TestFunc2Constraint1(self, x1, x2):
        cons = ((x1 - 3.0)**2 + (x2 + 2.0)**2)*np.exp(-x2**7) - 12.0
        return cons

    def _TestFunc2Constraint2(self, x1, x2):
        cons = 10.0*x1 + x2 - 7.0
        return cons

    def _TestFunc2Constraint3(self, x1, x2):
        cons = (x1 - 0.5)**2 + (x2 - 0.5)**2 - 0.2
        return cons
