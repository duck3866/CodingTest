a = int(input())
b = [int(input()) for _ in range(a)]
b.sort(reverse=True)
cnt = 0

for j in range(len(b)):
    cnt += 1
    if cnt == 3:
        b[j] = 0
        cnt = 0
print(sum(b))
