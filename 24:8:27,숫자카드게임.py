n,m = map(int,input().split())
lit = []
for i in range(n):
    lit.append(list(map(int,input().split())))
resultList = []
for j in range(n):
    resultList.append(min(lit[j]))
print(lit,resultList)
print(max(resultList))