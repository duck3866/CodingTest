a= list(map(int, input().split()))
if (max(a) < (sum(a)-max(a))):
    print("yes")
else:
    print("no")