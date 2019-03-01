import math
import numpy as np


def exp(n, eps=1e-6):
    ans = 0
    k = 0
    while(True):
        add = n**k/math.factorial(k)
        if add < eps:
            break
        ans += add
        k += 1
    return ans


def cos(n, eps=1e-6):
    ans = 0
    k = 0
    while(True):
        add = n ** (2 * k) / math.factorial(2 * k)
        if add < eps:
            break
        ans += ((-1) ** k) *add
        k += 1

    return ans


def sqrt(n, eps=1e-15):
    x = 1
    while(True):
        nx = (x + n / x) / 2
        if abs(x - nx) < eps:
            break
        x = nx
    return x


def f(x, eps=1e-6):
    return exp(1+x, eps=eps/1.62)*cos(sqrt(1+x), eps=eps/8.67)


def f_exact(x):
    return math.exp(1+x)*math.cos(math.sqrt(1+x))


print('f')
for x in np.arange(0.1, 0.21, 0.01):
    print('{} & {} \\\\'.format(x, f(x)))


print('f_exact')
for x in np.arange(0.1, 0.21, 0.01):
    print('{} & {} \\\\'.format(x, f_exact(x)))


print('max difference')
res = -1
for x in np.arange(0.1, 0.21, 0.01):
    res = max(res, abs(f_exact(x) - f(x)))
print(res)

