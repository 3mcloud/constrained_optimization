import numpy as np

class CEC2006_g04(object):
    
    def __init__(self):

        n = 5
        self.x_labels = ['x%d' % c for c in range(1,n+1)]

        x1_min =  78.0 
        x1_max = 102.0
        x2_min =  33.0 
        x2_max =  45.0 
        x3_min =  27.0 
        x3_max =  45.0
        x4_min =  27.0 
        x4_max =  45.0 
        x5_min =  27.0 
        x5_max =  45.0

        self.bounds = [(x1_min,  x1_max), (x2_min, x2_max), (x3_min,  x3_max), (x4_min, x4_max), (x5_min,  x5_max)]

        self.output_labels = ["objective", "constraint1", "constraint2", "constraint3", "constraint4", "constraint5", "constraint6"]
        self.objective = self.output_labels[0]
        constraint = 0.0
        self.output_constraints = [['constraint1', '<=', constraint], ['constraint2', '<=', constraint], ['constraint3', '<=', constraint], ['constraint4', '<=', constraint],
                                   ['constraint5', '<=', constraint], ['constraint6', '<=', constraint]]
        
        #best_x --> (78, 33, 29.9952560256815985, 45, 36.7758129057882073)
        self.best_val = 3.066553867178332e4

    def evaluate(self, x):

        obj = self._Objective(x)
        cons1 = self._Constraint1(x)
        cons2 = self._Constraint2(x)
        cons3 = self._Constraint3(x)
        cons4 = self._Constraint4(x)
        cons5 = self._Constraint5(x)
        cons6 = self._Constraint6(x)

        return [obj, cons1, cons2, cons3, cons4, cons5, cons6]

    def _Objective(self, x):
        func = 5.3578547*x[2]**2 + 0.8356891*x[0]*x[4] + 37.293239*x[0] - 40792.141
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x):
        cons = 85.334407 + 0.0056858*x[1]*x[4] + 0.0006262*x[0]*x[3] - 0.0022053*x[2]*x[4] - 92
        return cons

    def _Constraint2(self, x):
        cons = -85.334407 - 0.0056858*x[1]*x[4] - 0.0006262*x[0]*x[3] + 0.0022053*x[2]*x[4]
        return cons

    def _Constraint3(self, x):
        cons = 80.51249 + 0.0071317*x[1]*x[4] + 0.0029955*x[0]*x[1] + 0.0021813*x[2]**2 - 110
        return cons

    def _Constraint4(self, x):
        cons = -80.51249 - 0.0071317*x[1]*x[4] - 0.0029955*x[0]*x[1] - 0.0021813*x[2]**2 + 90
        return cons

    def _Constraint5(self, x):
        cons = 9.300961 + 0.0047026*x[2]*x[4] + 0.0012547*x[0]*x[2] + 0.0019085*x[2]*x[3] - 25
        return cons

    def _Constraint6(self, x):
        cons = -9.300961 - 0.0047026*x[2]*x[4] - 0.0012547*x[0]*x[2] - 0.0019085*x[2]*x[3] + 20
        return cons
