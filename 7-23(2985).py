a,b = map(int,input().split())
for i in range(2,a+b):
    if a % i == 0 and b % i == 0:
        so = i

for i in range(1,a*b):
    if i % a == 0 and i % b == 0:
        sosu = i
        break
print(so)
print(sosu)