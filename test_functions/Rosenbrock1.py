
class Rosenbrock1(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2']

        x1_min = -1.5
        x1_max =  1.5
        x2_min = -0.5 
        x2_max =  2.5 

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max)]

        self.output_labels = ["objective", "constraint1", "constraint2"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '<=', constraint], ['constraint2', '<=', constraint]]

        # x_best -> (1.0, 1.0)
        self.best_val = 0.00

    def evaluate(self, x):
        x1 = x[0]
        x2 = x[1]

        #print(x1)
        #print(x2)
        obj = self._Rosenbrock(x1, x2)
        cons1 = self._Constraint1(x1, x2)
        cons2 = self._Constraint2(x1, x2)
        
        return [obj, cons1, cons2]

    def _Rosenbrock(self, x1, x2):
        func = (1.0 - x1)**2 + 100.0*(x2 - x1**2)**2
        return -func # wiki assumes min - this makes it max

    def _Constraint1(self, x1, x2):
        cons = (x1 - 1.0)**3 - x2 + 1
        return cons

    def _Constraint2(self, x1, x2):
        cons = x1 + x2 - 2
        return cons
