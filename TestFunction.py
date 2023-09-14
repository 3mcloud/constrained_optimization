
from .test_functions.NewBranin import NewBranin
from .test_functions.Mystery import Mystery
from .test_functions.TestFunction2 import TestFunction2

from .test_functions.Rosenbrock1 import Rosenbrock1
from .test_functions.Rosenbrock2 import Rosenbrock2
from .test_functions.MishraBird import MishraBird
from .test_functions.Townsend import Townsend
from .test_functions.GomezLevy import GomezLevy
from .test_functions.Simionescu import Simionescu

from .test_functions.CEC2006_g04 import CEC2006_g04
from .test_functions.CEC2006_g24 import CEC2006_g24

from .test_functions.HS_10 import HS_10
from .test_functions.HS_11 import HS_11
from .test_functions.HS_12 import HS_12
from .test_functions.HS_13 import HS_13
from .test_functions.HS_15 import HS_15
from .test_functions.HS_16 import HS_16
from .test_functions.HS_17 import HS_17
from .test_functions.HS_18 import HS_18
from .test_functions.HS_19 import HS_19
from .test_functions.HS_20 import HS_20
from .test_functions.HS_21 import HS_21
from .test_functions.HS_22 import HS_22
from .test_functions.HS_23 import HS_23
from .test_functions.HS_24 import HS_24
from .test_functions.HS_29 import HS_29
from .test_functions.HS_30 import HS_30
from .test_functions.HS_31 import HS_31
from .test_functions.HS_33 import HS_33
from .test_functions.HS_35 import HS_35
from .test_functions.HS_36 import HS_36
from .test_functions.HS_37 import HS_37
from .test_functions.HS_43 import HS_43
from .test_functions.HS_44 import HS_44
from .test_functions.HS_64 import HS_64
from .test_functions.HS_65 import HS_65
from .test_functions.HS_83 import HS_83
from .test_functions.HS_86 import HS_86
from .test_functions.HS_95 import HS_95
from .test_functions.HS_96 import HS_96
from .test_functions.HS_97 import HS_97
from .test_functions.HS_98 import HS_98
from .test_functions.HS_105 import HS_105
from .test_functions.HS_106 import HS_106
from .test_functions.HS_108 import HS_108
from .test_functions.HS_113 import HS_113

MiscDict = { 
              "NewBranin"      : NewBranin,
              "Mystery"        : Mystery,
              "TestFunction2"  : TestFunction2,
              "Rosenbrock1"    : Rosenbrock1,
              "Rosenbrock2"    : Rosenbrock2,
              "MishraBird"     : MishraBird,
              "Townsend"       : Townsend,
              "GomezLevy"      : GomezLevy,
              "Simionescu"     : Simionescu,
              "CEC2006_g04"    : CEC2006_g04,              
              "CEC2006_g24"    : CEC2006_g24
            }

from test_functions.HS_34 import HS_34
from test_functions.HS_66 import HS_66
from test_functions.HS_70 import HS_70
from test_functions.HS_72 import HS_72
from test_functions.HS_84 import HS_84
from test_functions.HS_93 import HS_93
from test_functions.HS_100 import HS_100
from test_functions.HS_101 import HS_101
from test_functions.HS_102 import HS_102
from test_functions.HS_103 import HS_103
from test_functions.HS_104 import HS_104


HockDict = {"HS_10" : HS_10,
            "HS_11" : HS_11,
            "HS_12" : HS_12,
            "HS_13" : HS_13,
            "HS_15" : HS_15,
            "HS_16" : HS_16,
            "HS_17" : HS_17,
            "HS_18" : HS_18,
            "HS_19" : HS_19,
            "HS_20" : HS_20,
            "HS_21" : HS_21,
            "HS_22" : HS_22,
            "HS_23" : HS_23,
            "HS_24" : HS_24,
            "HS_29" : HS_29,
            "HS_30" : HS_30,
            "HS_31" : HS_31,
            "HS_33" : HS_33,
            "HS_35" : HS_35,
            "HS_36" : HS_36,
            "HS_37" : HS_37,
            "HS_43" : HS_43,
            "HS_44" : HS_44,
            "HS_64" : HS_64,
            "HS_65" : HS_65,
            "HS_83" : HS_83,
            "HS_86" : HS_86,
            "HS_95" : HS_95,
            "HS_96" : HS_96,
            "HS_97" : HS_97,
            "HS_98" : HS_98,
            "HS_105" : HS_105,
            "HS_106" : HS_106,
            "HS_108" : HS_108,
            "HS_113" : HS_113
}

FuncDict = MiscDict.copy()
FuncDict.update(HockDict)

class TestFunction(object):

    def __init__(self, func_key):
        self._func = FuncDict[func_key]()

    #-------------------------------------------------------------

    def evaluate(self, x_list):
        eval = []
        for x in x_list:
            #print(x)
            eval.append(self._func.evaluate(x))
        return eval

    #-------------------------------------------------------------

    def eval_obj(self, x):
        try:
            return self._func._Objective(x) # avoids unneeded computation
        except:
            return self._func.evaluate(x)[0] # assumes objective is always first

    #-------------------------------------------------------------

    def eval_obj_negative(self, x):
        try:
            return -self._func._Objective(x) # avoids unneeded computation
        except:
            return -self._func.evaluate(x)[0] # assumes objective is always first
    
    #-------------------------------------------------------------

    # return array with objective and distance from constraint value

    def eval_combined(self, x):
        outout = self._func.evaluate(x)
        obj = outout[0] # assumes objective is always first
        cons_vals = outout[1:] # assumes objective is always first
        out_cons = self._func.output_constraints

        comp_idx = 1
        val_idx = 2
        cons_dist = []
        for idx, cons in enumerate(out_cons):
            val_cons = cons[val_idx]
            val = cons_vals[idx]
            delta = abs(val_cons - val)
            if cons[comp_idx] == '<=':
                if val <= val_cons:
                    delta = 0.0
            elif cons[comp_idx] == '>=':
                if val >= val_cons:
                    delta = 0.0
            else:
                assert False # just break it
            cons_dist.append(delta)

        return [obj] + cons_dist

    #-------------------------------------------------------------

    def feasible(self, x):
        out_cons = self._func.output_constraints
        cons_vals = self._func.evaluate(x)[1:] # assumes objective is always first

        comp_idx = 1
        val_idx = 2
        for idx, cons in enumerate(out_cons):
            val_cons = cons[val_idx]
            val = cons_vals[idx]
            if cons[comp_idx] == '<=':
                if val > val_cons:
                    return False
            elif cons[comp_idx] == '>=':
                if val < val_cons:
                    return False
            else:
                assert False # just break it
                
        return True

    #-------------------------------------------------------------

    def constraint_distance(self, x):
        out_cons = self._func.output_constraints
        cons_vals = self._func.evaluate(x)[1:] # assumes objective is always first

        comp_idx = 1
        val_idx = 2
        cons_dist = []
        for idx, cons in enumerate(out_cons):
            val_cons = cons[val_idx]
            val = cons_vals[idx]
            delta = abs(val_cons - val)
            if cons[comp_idx] == '<=':
                if val <= val_cons:
                    delta = 0.0
            elif cons[comp_idx] == '>=':
                if val >= val_cons:
                    delta = 0.0
            else:
                assert False # just break it and try to fix issue
            cons_dist.append(delta)

        return cons_dist

    #-------------------------------------------------------------

    @property
    def x_labels(self):
        return self._func.x_labels

    @property
    def bounds(self):
        return self._func.bounds

    @property
    def output_labels(self):
        return self._func.output_labels

    @property
    def objective(self):
        return self._func.objective
    
    @property
    def constraints(self):
        return self._func.output_constraints
    
    @property
    def optimal_value(self):
        return self._func.best_val

# END TestFunction
#-------------------------------------------------------------

        
