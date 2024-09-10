
n = int(input())
controll = list(input().split())
nowposition = 1,1
array = [[0 for col in range(n)] for row in range(n)]
for i in range(n):
    for j in range(n):
        array[i][j] = i+1,j+1
for i in range(n):
    print(array[i])
for i in controll:
    if i == "R":
        if nowposition[1] != 5:
            nowposition = nowposition[0],nowposition[1]+1
    if i == "L":
        if nowposition[1] != 1:
            nowposition = nowposition[0],nowposition[1]-1
    if i == "U":
        if nowposition[0] != 1:
            nowposition = nowposition[0]-1,nowposition[1]
    if i == "D":
        if nowposition[0] != 5:
            nowposition = nowposition[0]+1,nowposition[1]
print(nowposition)