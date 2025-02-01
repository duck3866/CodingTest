n = int(input())
arr = []
for i in range(n):
    nanum = input().split()
    if nanum[0] == "push":
        arr.append(nanum[1])
    elif nanum[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(0))
    elif nanum[0] == "size":
        print(len(arr))
    elif nanum[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif nanum[0] == "front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif nanum[0] == "back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
