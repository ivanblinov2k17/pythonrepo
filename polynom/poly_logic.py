def read_poly(_s):
    s = '' + _s
    s = s.replace(' ', '')
    arr = []
    i = 0
    coef = ''
    degree = ''
    sign = 1
    while i < len(s):
        if s[i] == '-':
            sign = -1
            i += 1
        if s[i] == '+':
            i += 1
        while i < len(s) and '0' <= s[i] <= '9':
            coef += s[i]
            i += 1
        if i == len(s):
            degree = 0
        elif i < len(s):
            if s[i] == 'x':
                if i+1 == len(s):
                    degree = 1
                elif s[i+1] == '^':
                    i += 2
                    while i < len(s) and '0' <= s[i] <= '9':
                        degree += s[i]
                        i += 1
                elif s[i+1] == '+' or s[i+1] == '-':
                    degree = 1
        # формирование элемента
        if degree == '':
            degree = 1
        if coef == '':
            coef = 1
        degree = int(degree)
        coef = int(coef)
        while degree >= len(arr):
            arr.append(0)
        arr[degree] = sign * coef
        degree = ''
        coef = ''
        sign = 1
        i += 1
    return arr


def diff(_arr):
    arr = _arr.copy()
    if len(arr) == 1:
        return [0]
    for i in range(1, len(arr)):
        arr[i-1] = i*arr[i]
        arr[i] = 0
    arr.pop()
    return arr


def poly2str(arr):
    s = ''
    for i in range(len(arr)-1, 0, -1):
        if arr[i] != 0:
            s += str(arr[i]) + 'x^' + str(i) + '+'
    s += str(arr[0])
    return s
