import random
import math
import pylab
from matplotlib import mlab


def f1(phi):
    ans = 0
    for i in range(0, 5):
        ans += ((a0+phi*g1)*x[i]+(b0+phi*g2)-y[i]) ** 2
    return ans


def f2(phi):
    ans = 0
    for i in range(5):
        ans += abs((a0+phi*g1)*x[i]+(b0+phi*g2)-y[i])
    return ans


def dichotomia_min(l, r, f):
    current_pos = (l+r)/2
    l_value = f(current_pos - delta)
    r_value = f(current_pos + delta)
    print('dich', l, r, (r-l)/2, current_pos-delta, current_pos+delta, f(current_pos-delta), f(current_pos+delta))
    if r - l < 2 * eps:
        return f(current_pos)
    if l_value < r_value:
        return dichotomia_min(l, current_pos + delta, f)
    else:
        return dichotomia_min(current_pos - delta, r, f)


def golden_section_min(l, r, f):
    x1 = r - (r-l)/ph
    x2 = l + (r-l)/ph
    eps = 10 ** -6
    l_value = f(x1)
    r_value = f(x2)
    print('gold', l, r, (r-l)/2, x1, x2, f(x1), f(x2))
    if (r-l) < 2 * eps:
        return f((r+l)/2)
    else:
        if l_value >= r_value:
            return golden_section_min(x1, r, f)
        else:
            return golden_section_min(l, x2, f)


a0 = random.random() * 3
b0 = random.random() * 3
g1 = random.random()
g2 = math.sqrt(1 - g1 ** 2)
eps = 10 ** -6
delta = random.uniform(0, 2 * eps)
print(a0, b0, g1, g2, eps, delta)
x = [1, 2, 3, 4, 5]
y = [-4, -5, -6, -7, -8]
a = -10
b = 10
ph = (1 + math.sqrt(5))/2
xlist = mlab.frange(a, b, 0.01)
ylist = [f1(x) for x in xlist]
pylab.plot(xlist, ylist)
ylist = [f2(x) for x in xlist]
pylab.plot(xlist, ylist)
print(dichotomia_min(a, b, f1))
print(dichotomia_min(a, b, f2))
print(golden_section_min(a, b, f1))
print(golden_section_min(a, b, f2))
pylab.show()
