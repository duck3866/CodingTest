a,b = map(int,input().split())
su = []
for i in range(1,1000):
    for j in range(i):
        su.append(i)
su = su[a-1:b]
hap = 0
for k in su:
    hap += k
print(hap)