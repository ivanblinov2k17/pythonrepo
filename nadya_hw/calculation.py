def calc(a, operation, b):
    try:
        if operation == '/':
            return a / b
        elif operation == '*':
            return a * b
        elif operation == '-':
            return a - b
        elif operation == '+':
            return a + b
        else:
            raise NameError('this operation is not supported')
    except NameError as e:
        print(e)


a, b = [int(item) for item in input().split()]
op = input()
print(calc(a, op, b))
