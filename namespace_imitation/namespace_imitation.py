dict1 = {'global': 'None'}
dict2 = {'global': []}


def create(namespace, parent):
    global dict1
    global dict2
    dict1[namespace] = parent
    dict2[namespace] = []


def add(namespace, var):
    global dict2
    dict2[namespace].append(var)


def get(name, variable):
    global dict1
    global dict2
    if name == 'None':
        return None
    for temp in dict2[name]:
        if var == temp:
            return name
    else:
        return get(dict1[name], variable)


n = int(input())
for i in range(n):
    command, namespace, var = input().split()
    if command == "create":
        create(namespace, var)
    if command == "add":
        add(namespace, var)
    if command == "get":
        print(get(namespace, var))
