import sympy 
from sympy import *

# Using python to find limit of functions
# (function, variable, point)
# the point is f(x) as x->0 in this case, change at y = 
# f = equation to be used
# x is the variable

# Equation type 1
x = symbols('x')
f = ((4*(x**3)-2*x-6)/(-x**3+x**2+1))
y = limit(f,x,0)

print('Quad equation: (4*(x**3)-2*x-6)/(-x**3+x**2+1) =\n', y)

# Equation type 2
# square root limit
x = symbols('x')
f = sqrt(x)
y = limit(f,x,0)

print('Square root: sqrt(x) =\n', y)

# Equation type 3
# exponent limit
x = symbols('x')
f = exp(-x)
y = limit(f,x,0)

print('Exponent: e**-x =\n', y)

# Equation type 3
# Showing infinity
x = symbols('x')
f = 1/x**2
y = limit(f,x,0)

print('Standard equation: 1/x**2 =\n', y)

# Equation type 4
# Showing infinity again
x = symbols('x')
f = 1/x
y = limit(f,x,0)

print('Equation: 1/x =\n', y)

# Equation type 5
# Using log in limits
# This shows negative infinity
x = symbols('x')
f = log(x)
y = limit(f,x,0)

print('Log equation: lox(x) =\n', y)

# Equation type 6
# Using sin/cos
x = symbols('x')
f = sin(x)/x
y = limit(f,x,0)

print('sin/cos/tan equation: sin(x)/x =\n', y)

