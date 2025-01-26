arr = []
result = []
n = int(input())
for i in range(n):
    kg ,m = map(int,input().split())
    arr.append([kg,m])
for j in arr:
    cnt = 0
    for k in arr:
        if j != k:
            if (j[1] < k[1] and j[0] < k[0]):
                cnt +=1
    result.append(cnt+1)
for j in result:
    print(j)
        