a,b = map(int,input().split())
c = int(input())
d = int(input())
if(b+(a*d) <= c*d and a <= c):
    print(1)
else:
    print(0)
    