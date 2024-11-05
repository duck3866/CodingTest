
n = int(input())
arr = [[0,0]] * n
for i in range(n):
    word = input().split()
    arr[i] = word
for i in range(0,len(arr),1):
    first = arr[i][1]
    min = 100
    num = 0
    for j in range(i+1,len(arr),1):
        if int(arr[j][1]) < min:
            min = arr[j][i]
            num = j
    if arr[i][1] < arr[num][1]:
        dksl = arr[i]
        arr[i] = arr[num]
        arr[num] = dksl
    print(arr)
for i in range(len(arr)):
    print(arr[i][0])
