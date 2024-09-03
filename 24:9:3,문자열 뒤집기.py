a = input()
lit = []
munja = ""
for i in a:
    if len(munja) < 1:
        munja +=i
    elif munja[-1] == i:
        munja +=i
    else:
        lit.append(munja)
        munja = ""
        munja +=i
lit.append(munja);
print(lit)
check = []
for i in lit:
    if i[0] == '0':
        check.append(0)
    else:
        check.append(1)
zero = check.count(0) 
one = check.count(1) 
flag = 0
cnt = 0

if zero > one:
    
    while flag == 0:
        if 1 not in check:
                flag = 1
        for i in range(0,len(check)-1):
            if check[i] != 0:
                cnt +=1
                check[i] = 0
else:
 
    while flag == 0:
        if 0 not in check:
                flag = 1
        for i in range(0,len(check)-1):
            if check[i] != 1:
                cnt +=1
                check[i] = 1
print(cnt)
    