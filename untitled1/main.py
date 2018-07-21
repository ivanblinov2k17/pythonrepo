arr = [[]]
temp = input()
line = 0
while temp != 'end':
    arr[line] = [int(i) for i in temp.split()]
    line += 1
    temp = input()
arr1 = arr
for i in range(len(arr[0])):
    for j in range(len(arr)):
        print(1)
