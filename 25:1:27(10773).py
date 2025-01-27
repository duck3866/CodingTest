k = int(input())
arr = []
for _ in range(k):
    n = int(input().strip())
    if n != 0:
        arr.append(n)
    else:
        if len(arr) != 0:
            arr.pop()
print(sum(arr))