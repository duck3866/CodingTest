cnt = 0
c = []
for i in range(10):
    a = int(input())
    c.append(a%42)
c = set(c)
print(len(c))