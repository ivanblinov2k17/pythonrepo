f = open("file.txt", "r", encoding='utf-8')
res = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
for line in f:
    temp = line.strip().split('\t')
    print(temp)
    res[int(temp[0])-1][0] += int(temp[2])
    res[int(temp[0])-1][1] += 1
for i in range(len(res)):
    if res[i][1] == 0:
        print(i+1, '-')
    else:
        print(i+1, res[i][0]/res[i][1])
f.close()
