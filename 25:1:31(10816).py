N = int(input())
result = []
NDic = {}
NArr = list(map(int,input().split()))
for i in NArr:
    if i not in NDic:
        NDic[i] = 1
    else:
        NDic[i] +=1
M = int(input())
MArr = list(map(int,input().split()))
for j in MArr:
    if j in NDic:
        result.append(NDic[j])
    else:
        result.append(0)
print(*result)
