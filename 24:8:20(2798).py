n,m = map(int,input().split())
a = list(map(int,input().split()))
max = 0
for i in a:
    for j in a:
        for k in a:
            if i+j+k <= m:
                if i != j and i != k and j != k:
                    if i+j+k > max:
                        max = i+j+k
print(max)