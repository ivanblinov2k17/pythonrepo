import random
import math
import pylab
import numpy
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import mlab

a0 = 0.6787527143921632
b0 = 1.7466293115892506
g1 = 0.6745619858238852
g2 = 0.7382182111553037
eps = 10 ** -6
delta = random.uniform(0, 2 * eps)
print(a0, b0, g1, g2, eps, delta)
x = [1, 2, 3, 4, 5]
y = [-4, -5, -6, -7, -8]
a = -10
b = 10


def dichotomia_min(l, r, f):
    current_pos = (l+r)/2
    l_value = f(current_pos - delta)
    r_value = f(current_pos + delta)
    print('dich', l, r, (r-l)/2, current_pos-delta, current_pos+delta, f(current_pos-delta), f(current_pos+delta))
    if r - l < 2 * eps:
        return current_pos
    if l_value < r_value:
        return dichotomia_min(l, current_pos + delta, f)
    else:
        return dichotomia_min(current_pos - delta, r, f)


def f1(_a, _b):
    ans = 0
    for i in range(0, 5):
        ans += (_a*x[i] + _b - y[i])**2
    return ans


def f2(_a, _b):
    ans = 0
    for i in range(5):
        ans += abs(_a*x[i] + _b - y[i])
    return ans

# Строим сетку в интервале от -10 до 10 с шагом 0.01 по обоим координатам
def makeData(f):
    _x = numpy.arange(-10, 10, 0.01)
    _y = numpy.arange(-10, 10, 0.01)
    xgrid, ygrid = numpy.meshgrid(_x, _y)
    zgrid = f(xgrid, ygrid)
    return xgrid, ygrid, zgrid


# вычисление частной производной 1 функции по а
def der1a(_a, _b):
    return 110*_a + 30*_b + 200


# по б
def der1b(_a, _b):
    return 30*_a + 10*_b + 60


def gradient(_a, _b, f, alpha):
    print(_a, _b, alpha, f(_a, _b))
    a1 = _a - alpha*der1a(_a, _b)
    b1 = _b - alpha*der1b(_a, _b)
    # критерий останова
    if (abs(der1a(_a, _b)) <= eps) and (abs(der1b(_a, _b)) <= eps):
        return _a, _b
    # уменьшение константы
    if f(a1, b1) > f(_a, _b):
        return gradient(_a, _b, f, alpha/2)
    # если нет, то переходим к следующему шагу
    return gradient(a1, b1, f, alpha)


def show_graf(f):
    fig = pylab.figure()
    axes = Axes3D(fig)
    xx, yy, zz = makeData(f)
    axes.plot_surface(xx, yy, zz)

    pylab.show()


show_graf(f1)
show_graf(f2)
print(gradient(a, b, f1, 1))

