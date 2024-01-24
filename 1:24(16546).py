a = int(input())
b = set(map(int,input().split()))
c = set(range(1, a+1))

result = c - b
print(*result)
