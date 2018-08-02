s = set()
s2 = set()
n = int(input())
for i in range(n):
        s.add(input().strip().lower())
n = int(input())
for i in range(n):
    for j in input().strip().lower().split():
        s2.add(j)
print(s, s2)
for i in s2:
    if i not in s:
        print(i)
