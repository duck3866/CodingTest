import math
flag = False
m,n = map(int,input().split())#1,10
for i in range(m,n+1):
    if i == 0 or i == 1 or i == 2:
        if flag == False:
            print(2)
            flag = True
    else:
        cnt = 0
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                cnt +=1
                break
        if cnt == 0:
            print(i)