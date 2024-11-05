lit = list(map(int,input().split()))
for i in range(1,len(lit),1):
    test = lit[i]
    j = i-1
    while j >= 0 and lit[j] > test:
        lit[j+1] = lit[j]
        j -= 1
    lit[j+1] = test
    print(lit)