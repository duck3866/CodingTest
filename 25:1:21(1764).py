import sys
num = sys.stdin.readline().strip().split()
A = set()
result = []
for _ in range(int(num[0])):
    A.add(input())
for _ in range((int(num[1]))):
    word = input()
    if word in A:
        result.append(word)
print(len(result))
result.sort()
for j in result:
    print(j)

