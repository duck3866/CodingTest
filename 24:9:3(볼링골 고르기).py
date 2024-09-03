n,m = map(int,input().split())
lit = list(map(int,input().split()))
dic = []
for i in lit:
    for j in lit:
        if i != j:
            if str(j)+":"+str(i) not in dic:
                dic.append(str(i)+":"+str(j))
print(len(dic))
                
                