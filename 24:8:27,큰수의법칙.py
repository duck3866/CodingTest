n,m,k = map(int,input().split())
dic = list(map(int,input().split()))
dic.sort(reverse = True)
resultList = []
print(dic)
cnt = 1
result = 0
for i in range(m):
    if cnt <= k:
        result += dic[0]
        resultList.append(dic[0])
        cnt+=1
    elif cnt > k:
        result += dic[1]
        resultList.append(dic[1])
        cnt = 1
print(resultList)
print(result)