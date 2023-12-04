import sys
input = sys.stdin.readline
n = int(input())
b = []
for i in range(n):
    b.append(int(input()))
b.sort()
print = sys.stdout.write
for j in b:
    print("%d\n"%j)
