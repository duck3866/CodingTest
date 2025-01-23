n = int(input())
arr = []
for i in range(n):
    x,y = map(int,input().split())
    arr.append([x,y])
p = sorted(arr, key = lambda x :(x[0],x[1]))
for j in p:
    print(j[0],j[1])