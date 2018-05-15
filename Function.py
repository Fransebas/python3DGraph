from sympy.parsing.sympy_parser import parse_expr
from enum import Enum
from sympy.vector import CoordSys3D
from sympy import *


class Function():

    class Types(Enum):
        MULT_FUNC = 1
        PARAMETRIC = 2
        VECTOR = 3

    R = CoordSys3D('R')

    x, y, z, t, i, j, k = symbols('x y z t i j k')
    local_vars = {"i":R.i, "j":R.j, "k":R.k}
    def __init__(self, strf, type = Types.MULT_FUNC):
        self.strf = strf
        self.type = type
        self.e = sympify(self.strf, locals=Function.local_vars)
        print(self.e)
        self.makeFunction()

    def parametric(self, t):
        v = self.e.evalf(subs={
            Function.t: t,
        })

        return list(v.to_matrix(Function.R))

    def vector(self, x,y,z):
        v  = self.e.evalf(subs={
            Function.x:x,
            Function.y:y,
            Function.z:z,
        })

        return list(v.to_matrix(Function.R))

    def getType(self):
        return str(self.type)

    def makeFunction(self):
        if self.type == Function.Types.MULT_FUNC:
            self.f = lambdify([Function.x, Function.y], self.e)
        elif self.type == Function.Types.PARAMETRIC:
            self.f = self.parametric
        elif self.type == Function.Types.VECTOR:
            self.f = self.vector

    def eval(self, *vals):
        return self.f(*vals)

    def __str__(self):
        return str(self.e)

if __name__ == "__main__":
    f = Function("2*x*y")
    print( f.eval(2.4,3) )
