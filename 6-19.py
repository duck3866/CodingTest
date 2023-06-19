s,b,c =map(int,input().split(':'))
s1,b1,c1 = map(int,input().split(':'))
s2=0
b2=0
c2=0
c1 = c1-c
if c1<0:
    b1-=1
    c1+=60
    c2=c1
b1 = b1 -b
if b1<0:
    s1 -=1
    b1+=60
    b2 = b1
s1 -=s
s2 = s1
if len(str(s2))<=1:
    print('0%d:'%s2,end='')
if len(str(b2))<=1:
    print('0%d:'%b2,end='')
if len(str(c2))<=1:
    print("0",end='')
    print(c2)
elif len(str(c2))>=2:
    print(c2)

