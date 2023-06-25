a = int(input())
arr = list(map(int,input().split()))
s = 0
r = 1
for i in arr:
    if i == 1:
        s += r
        r += 1
    else:
        r = 1
print(s)