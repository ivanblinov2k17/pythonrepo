n = int(input())
table = []
found = False
for i in range(n):
    temp = input().split(';')
    found = False
    if len(table) > 0:
        for j in range(len(table)):
            if temp[0] == table[j][0]:
                found = True
                table[j][1] += 1
                if temp[1] > temp[3]:
                    table[j][5] += 3
                    table[j][2] += 1
                elif temp[1] == temp[3]:
                    table[j][5] += 1
                    table[j][3] += 1
                else:
                    table[j][4] += 1
    if not found:
        table.append([temp[0], 0, 0, 0, 0, 0])
        table[len(table) - 1][1] += 1
        if temp[1] > temp[3]:
            table[len(table) - 1][5] += 3
            table[len(table) - 1][2] += 1
        elif temp[1] == temp[3]:
            table[len(table) - 1][5] += 1
            table[len(table) - 1][3] += 1
        else:
            table[len(table) - 1][4] += 1
    found = False
    if len(table) > 0:
        for j in range(len(table)):
            if temp[2] == table[j][0]:
                found = True
                table[j][1] += 1
                if temp[1] < temp[3]:
                    table[j][5] += 3
                    table[j][2] += 1
                elif temp[1] == temp[3]:
                    table[j][5] += 1
                    table[j][3] += 1
                else:
                    table[j][4] += 1
    if not found:
        table.append([temp[2], 0, 0, 0, 0, 0])
        table[len(table) - 1][1] += 1
        if temp[1] < temp[3]:
            table[len(table) - 1][5] += 3
            table[len(table) - 1][2] += 1
        elif temp[1] == temp[3]:
            table[len(table) - 1][5] += 1
            table[len(table) - 1][3] += 1
        else:
            table[len(table) - 1][4] += 1
for i in table:
    print(i[0], ':', i[1], ' ', i[2], ' ', i[3], ' ', i[4], ' ', i[5], sep='')
