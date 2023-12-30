a = int(input())
d = a
cnt = 0
while True:
    b = d//10 + d%10
    c = (d%10)*10 + b%10
    d = c
    cnt+=1
    if d == a:
        break
print(cnt)