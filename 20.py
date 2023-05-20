a=list(map(int,input().split()))#649 733 643 55 651 915 521 685 215 659 
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
if len(c)>0:
    print(max(c),end=' ')
if len(b)>0:
    print(max(b))

