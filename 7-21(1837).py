
p,k = map(int,input().split())
s1 = 0
for i in range(2,p+1):
    if p % i == 0 and i < k:
        s1 = i
        print('BAD %d'%s1)
        exit()

print('GOOD')
