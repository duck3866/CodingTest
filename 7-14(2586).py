def isSosu(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = int(input())
m = int(input())
arr = []
for i in range(n, m + 1):
    if i == 1:
        continue
    if isSosu(i):
        arr.append(i)
if len(arr) == 0:
    print(-1)
    exit()
print(sum(arr))
print(min(arr))