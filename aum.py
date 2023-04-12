t,a,b=map(int,input().split())
for t in range(t,90,5):
    a+=1
if a>b:
    print("win")
elif b>a:
    print("lose")
else:
    print("same")


