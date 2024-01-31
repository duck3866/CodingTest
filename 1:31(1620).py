n, m = map(int, input().split())
dogam = {}
c = []
for i in range(1, n+1):
    a = input()
    dogam[a] = i
    dogam[str(i)] = a
for j in range(m):
    print(dogam[input()])
