import random
import math
import pylab
import numpy
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize


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


def f1(_a, _b):
    ans = 0
    for i in range(0, 5):
        ans += (_a*x[i] + _b - y[i])**2
    return ans


def f1_back(_a, _b):
    return f1(_b, _a)


def f2_back(_a, _b):
    return f2(_b, _a)


def f_v_a(alpha, _a, _b):
    return f1(a - alpha * der1a(_a, _b), b)


def f_v_b(alpha, _a, _b):
    return f1(a, b - alpha * der1b(_a, _b))


def f2(_a, _b):
    ans = 0
    for i in range(5):
        ans += abs(_a*x[i] + _b - y[i])
    return ans


ph = (1 + math.sqrt(5))/2


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


def gradient_const_step(_a, _b, f, alpha):
    print(_a, _b, alpha, f(_a, _b))
    a1 = _a - alpha*der1a(_a, _b)
    b1 = _b - alpha*der1b(_a, _b)
    # критерий останова
    if (abs(der1a(_a, _b)) <= eps) and (abs(der1b(_a, _b)) <= eps):
        return _a, _b
    return gradient_const_step(a1, b1, f, alpha)


def gradient_fastest(_a, _b, f):
    res_a = minimize(f_v_a, 0.5, args=(_a, _b))
    alpha_a = res_a.x[0]
    res_b = minimize(f_v_b, 0.5, args=(_a, _b))
    alpha_b = res_b.x[0]
    print(_a, _b, f(_a, _b), alpha_a, alpha_b)

    a1 = _a - alpha_a*der1a(_a, _b)
    b1 = _b - alpha_b*der1b(_a, _b)
    # критерий останова
    if abs(f(a1, b1)-f(_a, _b)) < 10*eps:
        return _a, _b
    return gradient_fastest(a1, b1, f)


def coord_spusk(_a, _b, f, f_back, flag):
    a_old = _a
    b_old = _b
    if flag == 1:
        res = minimize(f, 0, args=(b_old))
        _a = res.x[0]
    else:
        res = minimize(f_back, 0, args=(a_old))
        _b = res.x[0]
    if abs(_a-a_old) < eps and abs(_b-b_old) < eps:
        return _a, _b
    else:
        flag *= -1
        return coord_spusk(_a, _b, f, f_back, flag)


def show_graf(f):
    fig = pylab.figure()
    axes = Axes3D(fig)
    xx, yy, zz = makeData(f)
    axes.plot_surface(xx, yy, zz)

    pylab.show()


show_graf(f1)
show_graf(f2)
print(coord_spusk(0, 0, f1, f1_back, 1), "spusk1")
print(coord_spusk(0, 0, f2, f2_back, 1), "spusk2")
print(gradient(0, 0, f1, 1),"grad")
print(gradient_const_step(0, 0, f1, 0.015625), "const")
print(gradient_fastest(-1.001, -3.001, f1), "fast")

