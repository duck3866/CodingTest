n,m = map(int,input().split())

array = [[0 for col in range(n)] for row in range(m)]
for i in range(m):
    for j in range(n):
        array[i][j] = i+1,j+1
for i in range(m):
    print(array[i])
chracter = list(map(int,input().split()))
chracterPos = chracter[0],chracter[1]
chracterDir = chracter[-1]
print(chracterPos,chracterDir) 
for i in range(m):
    ground = list(map(int,input().split()))
print(ground)