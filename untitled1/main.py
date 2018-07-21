arr = [[]]
temp = input()
line = 0
while temp != 'end':
    arr[line] = [int(i) for i in temp.split()]
    line += 1
    temp = input()
