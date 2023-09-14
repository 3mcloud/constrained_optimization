import numpy as np
from numpy import pi

# problem from Hock Schittkowski collection
# "Test Examples for Nonlinear Programming Codes", Willi Hock, Klaus Schittkowski, Springer, Lecture
# Notes in Economics and Mathematical Systems, Vol. 187

class HS_105(object):
    
    def __init__(self):

        self.x_labels = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']

        # use constraints from the problem as the bounds 
    
        x1_min = 0.001
        x1_max = 0.499
        x2_min = 0.001
        x2_max = 0.499
        x3_min = 100.0
        x3_max = 180.0
        x4_min = 130.0
        x4_max = 210.0
        x5_min = 170.0
        x5_max = 240.0
        x6_min =  5.0
        x6_max = 25.0
        x7_min =  5.0
        x7_max = 25.0
        x8_min =  5.0
        x8_max = 25.0

        self.bounds = [(x1_min, x1_max), (x2_min, x2_max), (x3_min, x3_max), (x4_min, x4_max), 
                       (x5_min, x5_max), (x6_min, x6_max), (x7_min, x7_max), (x8_min, x8_max)]


        self.output_labels = ["objective", "constraint1"]

        self.objective = self.output_labels[0]
        cons_lo = 0.0
        self.output_constraints = [['constraint1', '>=', cons_lo]]

        #best_x --> (0.4128928, 0.4033526, 131.2613, 164.3135, 217.4222, 12.28018, 15.77170, 20.74682)

        self.best_val = -1136.36 # HS gives 1138.416240, but https://vanderbei.princeton.edu/ampl/nlmodels/hs/hs105.mod seems to disagree

        self._y = [95, 105]
        self._y += [110 for _ in range(3,7)]
        self._y += [115 for _ in range(7,11)]
        self._y += [120 for _ in range(11,26)]
        self._y += [125 for _ in range(26,41)]
        self._y += [130 for _ in range(41,56)]
        self._y += [135 for _ in range(56,69)]
        self._y += [140 for _ in range(69,90)]
        self._y += [145 for _ in range(90,102)]
        self._y += [150 for _ in range(102,119)]
        self._y += [155 for _ in range(119,123)]
        self._y += [160 for _ in range(123,143)]
        self._y += [165 for _ in range(143,151)]
        self._y += [170 for _ in range(151,168)]
        self._y += [175 for _ in range(168,176)]
        self._y += [180 for _ in range(176,182)]
        self._y += [185 for _ in range(182,188)]
        self._y += [190 for _ in range(188,195)]
        self._y += [195 for _ in range(195,199)]
        self._y += [200 for _ in range(199,202)]
        self._y += [205 for _ in range(202,205)]
        self._y += [210 for _ in range(205,213)]
        self._y += [215]
        self._y += [220 for _ in range(214,220)]
        self._y += [230 for _ in range(220,225)]
        self._y += [235]
        self._y += [240 for _ in range(226,233)]
        self._y += [245]
        self._y += [250 for _ in range(234,236)]

    def evaluate(self, x):
       
        obj = self._Objective(x)
        cons1 = self._Constraint1(x)

        return [obj, cons1] 

    def _Objective(self, x):
        func =  0.0
        for idx in range(235):
            func -= np.log((self._a_i(x,idx) + self._b_i(x,idx) + self._c_i(x,idx))/np.sqrt(2.0*pi))
        return -func # paper assumes min - this makes it max

    def _Constraint1(self, x):
        cons = 1 - x[0] - x[1]
        return cons

    def _a_i(self, x, i):
        return x[0] / x[5] * np.exp(-(self._y[i] - x[2])**2 / (2 * x[5]**2))

    def _b_i(self, x, i):
        return x[1] / x[6] * np.exp(-(self._y[i] - x[3])**2 / (2 * x[6]**2))

    def _c_i(self, x, i):
        return (1 - x[1] - x[0]) / x[7] * np.exp(-(self._y[i] - x[4])**2 / (2 * x[7]**2))
