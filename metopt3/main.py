import random
from sympy import *
a0 = 0.6787527143921632
b0 = 1.7466293115892506
g1 = 0.6745619858238852
g2 = 0.7382182111553037
eps = 10 ** -6
delta = random.uniform(0, 2 * eps)
a, b = symbols('a b')
f1 = (a+b+4)**2 + (2*a+b+5)**2 + (3*a+b+6)**2 \
     + (4*a+b+7)**2 + (5*a+b+8)**2
f2 = Abs(a+b+4) + Abs(2*a+b+5) + Abs(3*a+b+6) \
     + Abs(4*a+b+7) + Abs(5*a+b+8)

