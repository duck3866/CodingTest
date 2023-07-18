
n,k = map(int,input().split())

c = 1
d = 1

for i in range(n, n-k, -1) :
    c *= i
for i in range(1, k+1) :
    d *= i
print(c//d)