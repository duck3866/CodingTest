c = int(input())
a = list(map(int,input().split()))
b = []
cnt = 0
for i in a:
    if i not in b:
        b.append(i)
    else:
        cnt+=1
print(cnt)