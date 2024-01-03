a = list(map(int,input().split()))
basu = 1
a.sort()
while True:
    cnt = 0
    for i in a:
        if basu % i == 0:
            cnt+=1
    if cnt >= 3:
        break
    basu+=1
print(basu)