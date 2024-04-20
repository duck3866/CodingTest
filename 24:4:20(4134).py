import math

n = int(input())
for i in range(n):
    b = int(input())
    if b == 1 or b == 0:
        print(2)
    else:
        for j in range(b, b * 2):
            cnt = 0
            for k in range(2,int(math.sqrt(j))+1):
                if j%k == 0:
                    cnt += 1
                    break
            if cnt == 0:
                print(j)