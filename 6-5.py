a=int(input())
b=[int(input()) for _ in range(a)]
maxx = max(b)
cnt = 0
for i in b[::-1]:
    if i == maxx:
        cnt = 0
    cnt += 1
print(cnt)
for i in b:
    if i == maxx:
        cnt = 0
    cnt += 1
print(cnt)