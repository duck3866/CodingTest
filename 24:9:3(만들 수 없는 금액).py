a = int(input())
lit = list(map(int,input().split()))
if 1 not in lit:
    print(1)
else:
    b = list(lit)
    b.sort()
    no_lit = []
    for i in range(0,len(b)):
        if i not in no_lit:
            no_lit.append(b[i])
            for j in b:
                for k in b:
                    if i != j and i != k and j!= k:
                        if i+j+k not in no_lit:
                            no_lit.append(i+j+k)
    for i in range(1,len(b)):
        if sum(b[0:i]) not in no_lit:
            no_lit.append(sum(b[0:i]))
no_lit.sort()
minn = 100
for i in range(min(no_lit),max(no_lit)):
    if i not in no_lit:
        if i< minn:
            minn = i
print(minn)
        
                
        
