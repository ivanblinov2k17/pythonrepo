from sympy import plot_implicit, symbols, Eq, solve
x, y = symbols('x y')
eq = Eq((x**2+y**2-1)**3-(x**2)*(y**3))
plot_implicit(eq)