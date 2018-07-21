import math
n = int(input())
temp_i = 0
temp_j = 0
temp = 1
arr = []
for i in range(n):
    arr.append([0 for j in range(n)])
i = 0
j = 0
while temp < n*n:
    while j < n - temp_j - 1:
        arr[i][j] = temp
        j += 1
        temp += 1
    while i < n - temp_i - 1:
        arr[i][j] = temp
        i += 1
        temp += 1
    while j >= 0 + temp_j + 1:
        arr[i][j] = temp
        j -= 1
        temp += 1
    while i >= 0 + temp_i + 1:
        arr[i][j] = temp
        i -= 1
        temp += 1
    i += 1
    j += 1
    temp_i += 1
    temp_j += 1
if n % 2 == 1:
    arr[math.ceil(n/2)-1][math.ceil(n/2)-1] = n*n
for i1 in range(len(arr)):
    for j1 in range(len(arr[i])):
        print(arr[i1][j1], end=' ')
    print()
