import math

a = int(input())
b = list(map(int,input().split()))
for i in b:
    root = int(math.sqrt(i))
    if root*root == i:
        print(1, end=' ')
    else:
        print(0, end=' ')
