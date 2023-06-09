mony=[]
c=int(input())
for i in range(c):
    a,b,d=map(int,input().split())
    cnt=0
    if a==b:
        cnt+=1
    if a==d:
        cnt+=1
    if b==d:
        cnt+=1
    if cnt==3:
        mony.append(10000+(a*1000))
    elif cnt==1:
        if a==b:
            mony.append(1000+(a*100))
        elif b==d:
            mony.append(1000+(b*100))
        elif a==d:
            mony.append(1000+(a*100))
    if cnt==0:
        if a>b and a>d:
            mony.append(a*100)
        elif b>a and b>d:
            mony.append(b*100)
        elif d>b and d>a:
            mony.append(d*100)
print(max(mony))
        
# 3
# 3 3 6
# 2 2 2
# 6 2 5