from math import sqrt


def dividers(n):
    ans = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            ans.append(i)
            ans.append(int(n/i))
    if ans[len(ans)-1] == ans[len(ans)-2]:
        ans.pop()
    ans.sort()
    return ans


n = int(input())
print(dividers(n))
