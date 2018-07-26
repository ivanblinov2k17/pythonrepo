# -*- coding: utf-8 -*-
text = open("file.txt", 'r', encoding='utf-8')
s = text.read().strip().split('\n')
x = []
for i in s:
    x.append(i.split(';'))
sum1 = 0
sum2 = 0
sum3 = 0
for i in x:
    print(round((int(i[1])+int(i[2])+int(i[3]))/3, 9))
    sum1 += int(i[1])
    sum2 += int(i[2])
    sum3 += int(i[3])
print(round(sum1/len(x), 9), round(sum2/len(x), 9), round(sum3/len(x), 9))
