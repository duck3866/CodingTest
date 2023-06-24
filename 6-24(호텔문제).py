t = int(input())
for i in range(t):
    h,w,n = map(int,input().split())
    h1 = 0
    w1 = 0
    cnt = 1
    for j in range(1,n+1):
        h1 += 1
        w1 += 1
        if h1 > h:
            h1 = 1
            cnt +=1
        if w1 > w:
            w = 1
    print('%d%02d'%(h1,cnt))
#30 50 72