car=170
a,b,c=map(int,input().split())
if a<=car :
    print("CRASH %d"%a)
elif b<=car :
    print("CRASH %d"%b)
elif c<=car:
    print("CRASH %d"%c)
else:
    print("PASS")