# Quadratic funtion factoring

import sympy
from sympy import *

init_printing()
var('x y z')


expand((x + y)**2)
# expands to x**2 + 2xy + y**2

#print(expand((x + y + z)**2))
# expands to x**2 + 2*x*y + 2*x*z + y**2 + 2*y*z + z**2

# Factoring the equation
eq = x**2 + 2*x*y + y**2
a = factor(eq)
print('equation to factor:', eq)
print('factor of equation:', a)
# Factors to (x + y)**2

eq2 = x**3 - x**2 + x - 1
a2 =factor(eq2)
print('\nequation to factor:', eq2)
print('factor of equation:', a2)
# Factors to (x - 1)(x**2 + 1)


