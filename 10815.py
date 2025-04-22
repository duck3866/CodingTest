def BinarySearch(target, a):
    left = 0
    right = len(a) -1
    while left <= right:
        middle = (left + right) // 2
        if a[middle] == target:
            return True
        elif a[middle] < target:
            left = middle +1
        elif a[middle] > target:
            right = middle -1
    return False
N = int(input())
Narr = list(map(int,input().split()))
M = int(input())
Marr = list(map(int,input().split()))
result = []
Narr.sort()
for i in Marr:
    result.append(1 if BinarySearch(i,Narr) else 0)
print(*result)