h, m = map(int, input().split())
mp = int(input())
m += mp
while True:
    if(m >= 60):
        m -= 60
        h += 1
    if(h >= 24):
        h -= 24
        break
    if(h < 24 and m < 60):
        break
print(h, m)