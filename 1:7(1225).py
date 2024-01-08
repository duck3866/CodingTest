a,b = map(str, input().split())
cnt = 0
for i in a:
    for j in b:
        cnt += int(i)*int(j)
print(cnt)