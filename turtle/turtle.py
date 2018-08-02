n = int(input())
x = 0
y = 0
for i in range(n):
    temp = input().split()
    temp[1] = int(temp[1])
    if temp[0] == 'север':
        y += temp[1]
    elif temp[0] == 'восток':
        x += temp[1]
    elif temp[0] == 'юг':
        y -= temp[1]
    else:
        x -= temp[1]
print(x, y)
