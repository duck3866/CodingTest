a = int(input())
yr = list(map(int,input().split()))
yr.sort()
cs = yr[0]
cd = yr[-1]
we = 0
for i in range(1,cd*cs,+1):
    cnt = 0
    for j in yr:
        if cnt == a:
            break
        if i % j == 0:
            cnt += 1
print(i+1)