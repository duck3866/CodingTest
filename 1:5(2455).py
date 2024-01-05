cnt = 0
Dic = []
for i in range(4):
    a,b = map(int,input().split())
    cnt -= a
    cnt +=b
    Dic.append(cnt)
print(max(Dic))