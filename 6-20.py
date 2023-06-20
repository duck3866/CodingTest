a,b,c = map(int,input().split())
cnt = 1
j = 0
j -= a
if b>c:
    print('-1')
        
else:
    while True:
        cnt += 1
        j -= b
        j +=c
        if j>=0:
            print(cnt)
            break

        