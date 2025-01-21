import sys
n = int(sys.stdin.readline())
arr = set()
for _ in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == "all":
        arr = set([i for i in range(1, 21)])
        continue;
    elif command[0] == "empty":
        arr = set()
        continue;
    num = int(command[1])
    if command[0] == "add":
        arr.add(num)
    elif command[0] == "remove":
        arr.discard(num)
    elif command[0] == "check":
        print(1 if num in arr else 0)
    elif command[0] == "toggle":
        if num in arr:
            arr.discard(num)
        else:
            arr.add(num)