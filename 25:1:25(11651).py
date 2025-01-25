arr = []
n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    arr.append([x,y])
x = sorted(arr,key= lambda x :(x[1],x[0]))
for i in x:
    print(i[0],i[1])