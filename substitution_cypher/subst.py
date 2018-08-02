in1 = list(input())
in2 = list(input())
res1 = list(input())
res2 = list(input())
d = {}
d2 = {}
for i in range(len(in1)):
    d[in1[i]] = in2[i]
    d2[in2[i]] = in1[i]
for i in res1:
    print(d[i], end='')
print()
for i in res2:
    print(d2[i], end='')
print()
