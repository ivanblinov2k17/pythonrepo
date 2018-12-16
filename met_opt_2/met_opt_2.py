import random
import math
import pylab
import numpy
from matplotlib import mlab
import sys
sys.setrecursionlimit(5000)
from scipy.misc import derivative
s1 = []


def lomanyh(f, L, _x, p):
    print("%.6f" % _x, "%.6f" % f(_x), "%.6f" % p, "%.6f" % (f(_x)-p))
    d = (1/(2*L))*(f(_x)-p)
    if 2*d*L < eps:
        return _x
    x1 = _x - d
    x2 = _x + d
    p1 = (1/2)*(f(_x)+p)
    s1.append([x1, p1])
    s1.append([x2, p1])
    temp = 1000000
    t = []
    for i in s1:
        if i[1] < temp:
            t = i
            temp = i[1]
    s1.remove(t)
    return lomanyh(f, L, t[0], t[1])


def f1(phi):
    ans = 0
    for i in range(0, 5):
        ans += ((a0+phi*g1)*x[i]+(b0+phi*g2)-y[i]) ** 2
    return ans


def f2(phi):
    ans = []
    for i in range(0, 5):
        ans.append(abs((a0+phi*g1)*x[i]+(b0+phi*g2)-y[i]))
    return max(ans)


def f_1(_x):
    return derivative(f1, _x, 10**-6)


def newton(f, _x):
    print(_x, f(_x), f_1(_x))
    x1 = _x - f_1(_x)/(derivative(f_1, _x, 10**-6))
    if abs(f_1(_x)/(derivative(f_1, _x, 10**-6))) < eps:
        return _x
    return newton(f, x1)


def show_graf(f):
    xlist = mlab.frange(a, b, 0.001)
    ylist = [f(x) for x in xlist]
    pylab.plot(xlist, ylist)
    pylab.show()


a0 = 0.6787527143921632
b0 = 1.7466293115892506
g1 = 0.6745619858238852
g2 = 0.7382182111553037
eps = 10 ** -6
delta = random.uniform(0, 2 * eps)
print(a0, b0, g1, g2, eps, delta)
x = [1, 2, 3, 4, 5]
y = [-4, -5, -6, -7, -8]
l1 = 1146.66066922115416
l2 = 4.11102814027473
a = -10
b = 10
ph = (1 + math.sqrt(5))/2

show_graf(f1)
show_graf(f2)


x_start = (1/(2*l2))*(f2(a)-f2(b)+l2*(a+b))
p_start = (1/2)*(f2(a)+f2(b)+l2*(a-b))
print(newton(f1, 0))
print(lomanyh(f2, l2, x_start, p_start))
