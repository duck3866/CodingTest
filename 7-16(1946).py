n = int(input())
t = list(map(int,input().split()))
cnt = 0
for i in t:
    c = 0
    for j in range(2,i):
        if i % j == 0:
            c += 1
    if c == 0 and i != 1:
        cnt += 1
print(cnt)        