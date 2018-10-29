def rotate(a):
    if not a:
        return a
    arr = a[:]
    print(arr)
    tmp = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = tmp
    return arr


a = [1, 2, 3]
print(rotate(a))
